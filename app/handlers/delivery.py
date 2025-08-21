from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

from app.keyboards.reply import reply_main_menu
from app.keyboards.inline import inline_payment_methods
from app.storage import get_cart

router = Router()

class DeliveryFSM(StatesGroup):
    address = State()
    name = State()
    phone = State()
    confirm = State()

async def start_delivery(message: Message, state: FSMContext) -> None:
    await state.set_state(DeliveryFSM.address)
    await message.answer("Введите адрес доставки или нажмите ⬅ Назад для отмены")

async def start_delivery_from_cart(call: CallbackQuery) -> None:
    state: FSMContext = call.bot._dispatcher.fsm.get_context(call.from_user.id, call.message.chat.id)  # type: ignore
    cart = get_cart(call.from_user.id)
    if cart.total() == 0:
        await call.answer("Корзина пуста", show_alert=True)
        return
    await state.set_state(DeliveryFSM.address)
    await call.message.edit_text("Введите адрес доставки:")
    await call.answer()

@router.message(DeliveryFSM.address)
async def delivery_address(message: Message, state: FSMContext) -> None:
    await state.update_data(address=message.text.strip())
    await state.set_state(DeliveryFSM.name)
    await message.answer("Ваше имя:")

@router.message(DeliveryFSM.name)
async def delivery_name(message: Message, state: FSMContext) -> None:
    await state.update_data(name=message.text.strip())
    await state.set_state(DeliveryFSM.phone)
    await message.answer("Телефон (+84...):")

@router.message(DeliveryFSM.phone)
async def delivery_phone(message: Message, state: FSMContext) -> None:
    phone = message.text.strip()
    # Простая проверка
    import re
    if not re.fullmatch(r"\+?\d{7,15}", phone):
        await message.answer("Введите телефон в формате +XXXXXXXXX")
        return
    await state.update_data(phone=phone)
    data = await state.get_data()
    preview = (
        "<b>Проверьте данные доставки</b>\n"
        f"Адрес: {data['address']}\n"
        f"Имя: {data['name']}\n"
        f"Телефон: {data['phone']}\n\n"
        "Выберите способ оплаты:"
    )
    await state.set_state(DeliveryFSM.confirm)
    await message.answer(preview, reply_markup=inline_payment_methods())

@router.callback_query(DeliveryFSM.confirm, F.data == "pay:back")
async def pay_back(call: CallbackQuery) -> None:
    await call.answer("Выберите способ оплаты на экране")
