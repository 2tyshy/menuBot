from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def reply_main_menu() -> ReplyKeyboardMarkup:
    kb = [
        [KeyboardButton(text="🍽 Меню"), KeyboardButton(text="🧺 Корзина")],
        [KeyboardButton(text="🚚 Доставка"), KeyboardButton(text="📞 Связаться")],
    ]
    return ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
