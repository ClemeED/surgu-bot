# schedule_data.py
# институт -> направление -> file_id PDF

SCHEDULE = {
    "Медицинский институт": {
        "Лечебное дело": "BQACAgIAAxkBAAM6aqnBiD2dRnC8pVbIWh3BdWxYeVUAAgunAALWOVBJJm2C7N6YHgY9BA",
        "Педиатрия": "BQACAgIAAxkBAANRaqnF_wTGC-cuKK69sQepaedUmnwAAk-yAAKcLFFJwcRJAVGoqzQ9BA",
        "Лечебное дело (на английском языке)": "BQACAgIAAxkBAAM5aqnBfm99M3hA6o5GEOsQp4eYopoAAgqnAALWOVBJoTCeOz-0QcE9BA",
        "Цикловое расписание": "BQACAgIAAxkBAANTaqnGFREJimI7pqo5s7ZZq8sgs04AAlCyAAKcLFFJowVK2uxhCcc9BA",
    },
    "Политехнический институт": {
        "Программная инженерия": "BQACAgIAAxkBAANPaqnCD0vFPMQz0g5PSmj8L_emL7oAAhenAALWOVBJb9weKtPQ-5Q9BA",
        "Информатика и вычислительная техника": "BQACAgIAAxkBAANHaqnCA-58kliiEZ-9qV6c7qO2JIYAAhKnAALWOVBJaYgBt88oJY89BA",
        "Информационные системы и технологии": "BQACAgIAAxkBAANJaqnCB0J431VM5S2ygsasY0dVfxkAAhSnAALWOVBJ28Q-YOxn70Q9BA",
        "Прикладная математика и информатика": "BQACAgIAAxkBAANLaqnCCf-Qvveozqk2fGyykfV5IuAAAhWnAALWOVBJCoELqgr6gh89BA",
        "Строительство": "BQACAgIAAxkBAANNaqnCDCqhvpjWpSOQKz2y_UY02ncAAhanAALWOVBJtFwZQMo2u-k9BA",
        "Электроэнергетика и электротехника": "BQACAgIAAxkBAAM9aqnBq-oQwLoubcBCOn7qLxjfx9QAAgynAALWOVBJqGlwHnMptWc9BA",
        "Теплоэнергетика и теплотехника": "BQACAgIAAxkBAANBaqnBweBYGlFilYtTNdINpgyOOogAAg6nAALWOVBJljSSqdw0h5w9BA",
        "Инфокоммуникационные технологии и системы связи": "BQACAgIAAxkBAAM_aqnBt3SluoAEbKeX9Fe11dtkUU0AAg2nAALWOVBJpIIgFOWLdmY9BA",
        "Управление в технических системах": "BQACAgIAAxkBAANDaqnBzGIBQvlaOUlXbdVcF3XP5H0AAg-nAALWOVBJt7u2I25jMPo9BA",
        "Физика": "BQACAgIAAxkBAANFaqnCAAEKhXoNpxx9Okx76c3bu6DVAAIRpwAC1jlQSX3-FU3EGp8xPQQ",
    },
    "Институт экономики и управления": {
        "Бизнес-информатика": "BQACAgIAAxkBAANeaqnGjCPhhC1n2UZcR2J0rqSqLisAAlayAAKcLFFJQrDXT5-hwXI9BA",
        "Экономика": "BQACAgIAAxkBAANdaqnGfd_eUpVYdfn2nWsc5xJnPggAAlWyAAKcLFFJ6cXY45uJXpw9BA",
        "Экономическая безопасность": "BQACAgIAAxkBAANbaqnGbuP0IEY2EsODjCmSe03xvEMAAlSyAAKcLFFJeVLFPnCj7QY9BA",
        "Менеджмент": "BQACAgIAAxkBAANZaqnGYRtQ3rMI5tYrasL6odNDCM8AAlOyAAKcLFFJkiz_wwPcqCE9BA",
        "Управление персоналом": "BQACAgIAAxkBAANXaqnGUVCaYVUJviFp8qu6JOkLSi4AAlKyAAKcLFFJS9-O2ObKQ8M9BA",
        "Государственное и муниципальное управление": "BQACAgIAAxkBAANVaqnGQwhDT1-owMysXtVkqFTlGc4AAlGyAAKcLFFJAAFnov2qvn3dPQQ",
    },
    "Институт государства и права": {
        "Политология": "BQACAgIAAxkBAAN3aqnHd6BPrnsbrcIF5WwuRV1Gxk8AAmSyAAKcLFFJYeiaq1xMS7M9BA",
        "Юриспруденция": "BQACAgIAAxkBAAN5aqnHhEoBIhQdmtsShqcjDg_Y_BUAAmayAAKcLFFJObMur4clnlE9BA",
    },
    "Институт гуманитарного образования и спорта": {
	"Режиссура театрализованных представлений и праздников": "BQACAgIAAxkBAANxaqnHDdXES8a-hp1qfpgofqGr0U8AAmCyAAKcLFFJm_zkb9Yjw849BA",
        "Спорт": "BQACAgIAAxkBAAODaqnHtr7thQTnrVvS2a6nHhJDlXIAAmuyAAKcLFFJX930RYMWRnI9BA",
        "История": "BQACAgIAAxkBAAOBaqnHtAx-ZnUwN0Kfit8pFrIusyMAAmqyAAKcLFFJI5HpvDkT-ME9BA",
        "Физическая культура": "BQACAgIAAxkBAAN7aqnHlGAZCmNBVt8-I9_GRb40Pt8AAmeyAAKcLFFJeduAekC6Cvw9BA",
        "Лингвистика": "BQACAgIAAxkBAAN_aqnHqfzqnkAy-oihg3uX3ZrtVrsAAmmyAAKcLFFJ0eatzBVVceI9BA",
	"Физическая культура для лиц с отклонениями в состоянии здоровья (Адаптивная физическая культура)": "BQACAgIAAxkBAAN9aqnHnvyb3FcaCaudKSGZecKHywEAAmiyAAKcLFFJi2bR1REcAAFNPQQ",
        "Педагогическое образование": "BQACAgIAAxkBAAN1aqnHLqft0Rna-PRDuTyb0pbzhZcAAmOyAAKcLFFJ3_Xz39YM2Vo9BA",
        "Медиакоммуникации": "BQACAgIAAxkBAANzaqnHGdVqUkYouD5g4hD6Sx3AnCwAAmKyAAKcLFFJ8EqphsG2gD89BA",
        "Реклама и связи с общественностью": "BQACAgIAAxkBAANvaqnHAAFxMBpL0Yf4S9ifcrubjyqwAAJfsgACnCxRSe_taX0cZ1r-PQQ",
        "Клиническая психология": "BQACAgIAAxkBAANtaqnG9sjFV5rVl-ypw-maqNKE1QsAAl6yAAKcLFFJFJk4Z0kk2Fg9BA",
        "Психология служебной деятельности": "BQACAgIAAxkBAANraqnG5hwk-pExi-qRFXUeuyBDxSIAAlyyAAKcLFFJJReny7JSiOU9BA",
    },
    "Институт естественных и технических наук": {
        "Биология": "BQACAgIAAxkBAANpaqnG118fQGeHAW31TsFTtoOjUGIAAluyAAKcLFFJgA_sHpzNGoY9BA",
        "Экология и природопользование": "BQACAgIAAxkBAANnaqnGyaweWF5_27Nc7eFv3oJIftQAAlqyAAKcLFFJMo5KM3tt3wU9BA",
        "Техносферная безопасность": "BQACAgIAAxkBAANlaqnGvWJSW0r0_GC5IHoJpbbDefYAAlmyAAKcLFFJwfGxOvLGNRc9BA",
        "Химия": "BQACAgIAAxkBAANjaqnGtPgw_w6eyN8gblvei0nWo1AAAliyAAKcLFFJCkwL2qtxZeg9BA",
        "Фундаментальная и прикладная химия": "BQACAgIAAxkBAANhaqnGqodD6CQMCRVZOgy-MJYeC3sAAleyAAKcLFFJeChnd7g9Z4I9BA",
    },
}