from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from app.keyboards.reply import reply_main_menu

router = Router()

@router.message(F.text == "/start")
@router.message(F.text.regexp("^/start"))
async def cmd_start(message: Message, state: FSMContext) -> None:
    await state.clear()
    await message.answer(
        "👋 Добро пожаловать в кафе! Выберите раздел:",
        reply_markup=reply_main_menu(),
    )

@router.message(F.text == "🍽 Меню")
async def go_menu(message: Message) -> None:
    from .menu import show_menu_root
    await show_menu_root(message)

@router.message(F.text == "🧺 Корзина")
async def go_cart(message: Message) -> None:
    from .cart import show_cart
    await show_cart(message)

@router.message(F.text == "🚚 Доставка")
async def go_delivery(message: Message, state: FSMContext) -> None:
    from .delivery import start_delivery
    await start_delivery(message, state)

@router.message(F.text == "📞 Связаться")
async def go_contact(message: Message) -> None:
    from .contact import show_contacts
    await show_contacts(message)
