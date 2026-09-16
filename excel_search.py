# excel_search.py
import openpyxl
import os

# Кэш: файл читается один раз при первом запросе
_teachers_cache = None

# Соответствие дней недели колонкам Excel
# D = понедельник, F = вторник, H = среда, J = четверг, L = пятница, N = суббота
# В openpyxl нумерация колонок с 1, поэтому: D=4, E=5, F=6, G=7, H=8, I=9, J=10, K=11, L=12, M=13, N=14, O=15
DAY_COLUMNS = {
    "понедельник": (4, 5),
    "вторник":     (6, 7),
    "среда":       (8, 9),
    "четверг":     (10, 11),
    "пятница":     (12, 13),
    "суббота":     (14, 15),
}


def load_teachers():
    """Загружает всех преподавателей из Excel в кэш."""
    global _teachers_cache
    if _teachers_cache is not None:
        return _teachers_cache
    
    file_path = "zanyatost.xlsx"
    if not os.path.exists(file_path):
        raise FileNotFoundError(
            f"Файл {file_path} не найден. Положите его рядом с bot.py"
        )
    
    wb = openpyxl.load_workbook(file_path, data_only=True)
    ws = wb.active
    
    teachers = {}  # {ФИО: {день: [(пара, группа, аудитория), ...]}}
    
    # Пропускаем первую строку (заголовки)
    for row in ws.iter_rows(min_row=2, values_only=True):
        fio = row[0]  # колонка A
        para = row[2]  # колонка C
        if not fio or not para:
            continue
        
        fio = str(fio).strip()
        if fio not in teachers:
            teachers[fio] = {}
        
        # Проходим по всем дням недели
        for day, (group_col, aud_col) in DAY_COLUMNS.items():
            group_value = row[group_col - 1]  # -1, потому что values_only даёт индексы с 0
            aud_value = row[aud_col - 1]
            
            if group_value and str(group_value).strip():
                if day not in teachers[fio]:
                    teachers[fio][day] = []
                teachers[fio][day].append({
                    "para": para,
                    "group": str(group_value).strip(),
                    "aud": str(aud_value).strip() if aud_value else ""
                })
    
    _teachers_cache = teachers
    return teachers


def find_teacher(query, day):
    """
    Ищет преподавателя по фамилии и дню.
    query — часть ФИО (например, "Галкин")
    day — день недели (например, "вторник")
    Возвращает: (полное_ФИО, список_занятий) или (None, None)
    """
    teachers = load_teachers()
    day = day.lower().strip()
    query = query.lower().strip()
    
    # Ищем всех, чьё ФИО содержит запрос
    matches = [fio for fio in teachers.keys() if query in fio.lower()]
    
    if not matches:
        return None, None
    
    # Если несколько совпадений — вернём все, пользователь уточнит
    if len(matches) > 1:
        return matches, "multiple"
    
    fio = matches[0]
    schedule = teachers[fio].get(day, [])
    return fio, schedule