from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from app.keyboards.reply import reply_main_menu

router = Router()

async def show_contacts(message: Message) -> None:
    text = (
        "<b>Контакты кафе</b>\n"
        "Телефон: +84 900 000 000\n"
        "Адрес: 123 Beach St, Nha Trang\n"
        "Карта: https://maps.app.goo.gl/\n"
        "Часы: Пн-Вс 10:00–22:00\n\n"
        "Напишите нам: просто отправьте это сообщение — и мы ответим!"
    )
    await message.answer(text)

@router.message(F.text)
async def contact_any_text(message: Message) -> None:
    # Мок: логируем, как будто отправили админу
    print(f"[CONTACT] User {message.from_user.id} wrote: {message.text}")
    await message.answer("Сообщение отправлено администратору (мок). Для меню — /start")
