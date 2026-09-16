import os
import telebot
from telebot import types
from schedule_data import SCHEDULE
from gigachat import GigaChat
from excel_search import find_teacher

# ↓↓↓ ЗАМЕНИТЕ НА ВАШ FILE_ID СХЕМЫ КОРПУСОВ ↓↓↓
MAP_FILE_ID = "BQACAgIAAxkBAAOTaqnPk51eB9ntugVE87gmFwVux6gAAnGyAAKcLFFJHh-aZM956fU9BA"

# ↓↓↓ ЗАМЕНИТЕ НА ВАШ ТОКЕН ИЗ @BotFather ↓↓↓
bot = telebot.TeleBot("TELEGRAM_BOT_TOKEN")

# ↓↓↓ ЗАМЕНИТЕ НА ВАШ КЛЮЧ GIGACHAT ↓↓↓
GIGACHAT_CREDENTIALS = "GIGACHAT_CREDENTIALS"

# Инициализация GigaChat
giga = GigaChat(
    credentials=GIGACHAT_CREDENTIALS,
    scope="GIGACHAT_API_PERS",
    model="GigaChat-2",
    verify_ssl_certs=False
)

user_state = {}

DAYS = ["понедельник", "вторник", "среда", "четверг", "пятница", "суббота"]


def ask_gigachat(user_text):
    try:
        response = giga.chat(user_text)
        return response.choices[0].message.content
    except Exception as e:
        return f"Ошибка ИИ: {e}"


def main_menu(chat_id, text="Выберите раздел:"):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(types.KeyboardButton("📅 Расписание"))
    markup.add(types.KeyboardButton("🔔 Изменения пар"))
    markup.add(types.KeyboardButton("🗺️ Схема корпусов"))
    markup.add(types.KeyboardButton("🤖 Спроси GigaChat"))
    markup.add(types.KeyboardButton("🔍 Найти преподавателя"))
    bot.send_message(chat_id, text, reply_markup=markup)


@bot.message_handler(commands=['start'])
def start(message):
    user_state.pop(message.chat.id, None)
    main_menu(message.chat.id)


# ============ РАСПИСАНИЕ ============

@bot.message_handler(func=lambda m: m.text == "📅 Расписание")
def show_institutes(message):
    user_state.pop(message.chat.id, None)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    for institute in SCHEDULE.keys():
        markup.add(types.KeyboardButton(institute))
    markup.add(types.KeyboardButton("⬅ Назад"))
    bot.send_message(message.chat.id, "Выберите институт:", reply_markup=markup)


@bot.message_handler(func=lambda m: m.text in SCHEDULE)
def choose_institute(message):
    institute = message.text
    user_state[message.chat.id] = {"institute": institute}
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    for direction in SCHEDULE[institute].keys():
        markup.add(types.KeyboardButton(direction))
    markup.add(types.KeyboardButton("⬅ Назад"))
    bot.send_message(message.chat.id, f"{institute}\nВыберите направление:", reply_markup=markup)


@bot.message_handler(func=lambda m:
    m.chat.id in user_state
    and "institute" in user_state[m.chat.id]
    and m.text in SCHEDULE[user_state[m.chat.id]["institute"]]
)
def send_schedule(message):
    institute = user_state[message.chat.id]["institute"]
    direction = message.text
    file_id = SCHEDULE[institute][direction]
    bot.send_document(
        message.chat.id,
        file_id,
        caption=f"Расписание: {institute}\n{direction}"
    )


# ============ ПРОЧЕЕ ============

@bot.message_handler(func=lambda m: m.text == "🔔 Изменения пар")
def changes_info(message):
    bot.send_message(message.chat.id, "Информация об изменениях пар отсутствует.")


@bot.message_handler(func=lambda m: m.text == "🗺️ Схема корпусов")
def send_map(message):
    bot.send_document(
        message.chat.id,
        MAP_FILE_ID,
        caption="Схема корпусов СурГУ"
    )


# ============ GIGACHAT ============

@bot.message_handler(func=lambda m: m.text == "🤖 Спроси GigaChat")
def enter_ai_mode(message):
    user_state[message.chat.id] = {"mode": "ai"}
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(types.KeyboardButton("⬅ Выйти из чата с ИИ"))
    bot.send_message(
        message.chat.id,
        "🤖 Режим GigaChat включён.\n\n"
        "Задайте любой вопрос текстом или отправьте фото для анализа.\n"
        "Для выхода нажмите кнопку ниже.",
        reply_markup=markup
    )


@bot.message_handler(func=lambda m: m.text == "⬅ Выйти из чата с ИИ")
def exit_ai_mode(message):
    user_state.pop(message.chat.id, None)
    main_menu(message.chat.id, "Вы вышли из чата с ИИ. Выберите раздел:")


# --- Обработка ТЕКСТА в режиме ИИ ---
@bot.message_handler(func=lambda m:
    m.chat.id in user_state
    and user_state[m.chat.id].get("mode") == "ai"
    and m.content_type == 'text'
)
def ai_handler(message):
    bot.send_chat_action(message.chat.id, 'typing')
    answer = ask_gigachat(message.text)
    bot.send_message(message.chat.id, answer)


# --- Обработка ФОТО в режиме ИИ ---
@bot.message_handler(func=lambda m:
    m.chat.id in user_state
    and user_state[m.chat.id].get("mode") == "ai"
    and m.content_type == 'photo'
)
def ai_photo_handler(message):
    bot.send_chat_action(message.chat.id, 'typing')

    try:
        # 1. Скачиваем фото в максимальном качестве
        file_info = bot.get_file(message.photo[-1].file_id)
        downloaded = bot.download_file(file_info.file_path)

        # 2. Сохраняем во временный файл
        temp_path = f"temp_photo_{message.chat.id}.jpg"
        with open(temp_path, "wb") as f:
            f.write(downloaded)

        # 3. Загружаем в GigaChat и получаем ID
        with open(temp_path, "rb") as f:
            uploaded = giga.upload_file(f, purpose="general")

        # 4. Отправляем в чат с текстом (если есть подпись к фото)
        prompt = message.caption if message.caption else "Что на этом изображении?"

        # 5. Формируем запрос с изображением
        response = giga.chat({
            "messages": [
                {
                    "role": "user",
                    "content": prompt,
                    "attachments": [uploaded.id]
                }
            ]
        })

        answer = response.choices[0].message.content
        bot.send_message(message.chat.id, answer)

        # 6. Удаляем временный файл
        os.remove(temp_path)

    except Exception as e:
        bot.send_message(message.chat.id, f"Ошибка анализа фото: {e}")


# ============ ПОИСК ПРЕПОДАВАТЕЛЯ ============

@bot.message_handler(func=lambda m: m.text == "🔍 Найти преподавателя")
def ask_teacher(message):
    user_state[message.chat.id] = {"mode": "teacher_search"}
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(types.KeyboardButton("⬅ Выйти из поиска"))
    bot.send_message(
        message.chat.id,
        "🔍 Режим поиска преподавателя.\n\n"
        "Введите ФИО и день недели.\n"
        "Формат: Фамилия День\n"
        "Например: Иванов Понедельник\n\n"
        "Дни недели: Понедельник, Вторник, Среда, Четверг, Пятница, Суббота\n\n"
        "Можно искать нескольких преподавателей подряд.",
        reply_markup=markup
    )


@bot.message_handler(func=lambda m: m.text == "⬅ Выйти из поиска")
def exit_teacher_search(message):
    user_state.pop(message.chat.id, None)
    main_menu(message.chat.id, "Вы вышли из поиска. Выберите раздел:")


@bot.message_handler(func=lambda m:
    m.chat.id in user_state
    and user_state[m.chat.id].get("mode") == "teacher_search"
)
def handle_teacher_query(message):
    parts = message.text.strip().split()

    if len(parts) < 2:
        bot.send_message(
            message.chat.id,
            "Не понял запрос. Введите в формате: Фамилия День\n"
            "Например: Иванов Понедельник"
        )
        return

    day = parts[-1].lower()
    name_query = " ".join(parts[:-1])

    if day not in DAYS:
        bot.send_message(
            message.chat.id,
            f"День недели «{day}» не распознан.\n"
            f"Доступные дни: Понедельник, Вторник, Среда, Четверг, Пятница, Суббота"
        )
        return

    try:
        result, schedule = find_teacher(name_query, day)
    except Exception as e:
        bot.send_message(message.chat.id, f"Ошибка чтения Excel: {e}")
        return

    if result is None:
        bot.send_message(
            message.chat.id,
            f"Преподаватель «{name_query}» не найден.\n"
            f"Проверьте написание фамилии."
        )
        return

    if schedule == "multiple":
        bot.send_message(
            message.chat.id,
            "Найдено несколько преподавателей:\n" +
            "\n".join(f"• {fio}" for fio in result) +
            "\n\nУточните фамилию (например, добавьте инициалы)."
        )
        return

    if not schedule:
        bot.send_message(
            message.chat.id,
            f"📚 {result}\n📅 {day.capitalize()}\n\nЗанятий в этот день нет."
        )
        return

    lines = [f"📚 {result}", f"📅 {day.capitalize()}", ""]
    for item in schedule:
        para = item["para"]
        group = item["group"]
        aud = item["aud"]
        if aud:
            lines.append(f"{para} пара — {group} — ауд. {aud}")
        else:
            lines.append(f"{para} пара — {group}")

    bot.send_message(message.chat.id, "\n".join(lines))


# ============ НАВИГАЦИЯ ============

@bot.message_handler(func=lambda m: m.text == "⬅ Назад")
def go_back(message):
    user_state.pop(message.chat.id, None)
    main_menu(message.chat.id)


@bot.message_handler(commands=['reset'])
def reset(message):
    user_state.pop(message.chat.id, None)
    main_menu(message.chat.id)


print("Бот запущен...")
bot.polling(none_stop=True, timeout=60, long_polling_timeout=60)