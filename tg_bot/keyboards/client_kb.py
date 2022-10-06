from aiogram.types import ReplyKeyboardMarkup,KeyboardButton#,ReplyKeyboardRemove

b1 = KeyboardButton('/Стиль_тренировки')
b2 = KeyboardButton('/Время')
b3 = KeyboardButton('/Длительность')
b4 = KeyboardButton('/Меню')
b5 = KeyboardButton('Поделиться номером',request_contact=True)
b6 = KeyboardButton('Отправить где я',request_location=True)

kb_clint = ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True)

# kb_clint.add(b1).add(b2).add(b3).add(b4)
kb_clint.add(b1).insert(b2).add(b3).insert(b4).add(b5).insert(b6)