from aiogram import Router, F
from aiogram.types import Message, CallbackQuery

from app.keyboards.inline import inline_cart_controls, inline_cart_item_remove
from app.storage import get_cart, SKU_INDEX

router = Router()

async def show_cart(message: Message | CallbackQuery) -> None:
    if isinstance(message, CallbackQuery):
        user_id = message.from_user.id
    else:
        user_id = message.from_user.id

    cart = get_cart(user_id)
    lines = cart.as_lines()
    total_line = f"\n<b>Итого: {cart.total()} VND</b>"

    text = "<b>Корзина</b>\n" + "\n".join(lines) + total_line

    if isinstance(message, CallbackQuery):
        await message.message.edit_text(text, reply_markup=inline_cart_controls())
        await message.answer()
    else:
        await message.answer(text, reply_markup=inline_cart_controls())

@router.callback_query(F.data.startswith("cart:add:"))
async def add_to_cart(call: CallbackQuery) -> None:
    sku = call.data.split(":")[-1]
    cart = get_cart(call.from_user.id)
    try:
        cart.add(sku, 1)
        await call.answer("Добавлено в корзину (мок)")
    except ValueError as e:
        await call.answer(str(e), show_alert=True)

@router.callback_query(F.data == "cart:clear")
async def clear_cart(call: CallbackQuery) -> None:
    cart = get_cart(call.from_user.id)
    cart.clear()
    await show_cart(call)

@router.callback_query(F.data.startswith("cart:rm:"))
async def remove_item(call: CallbackQuery) -> None:
    sku = call.data.split(":")[-1]
    cart = get_cart(call.from_user.id)
    cart.remove(sku)
    await show_cart(call)

@router.callback_query(F.data == "cart:checkout")
async def cart_checkout(call: CallbackQuery) -> None:
    # Переходим в доставку (FSM)
    from .delivery import start_delivery_from_cart
    await start_delivery_from_cart(call)
