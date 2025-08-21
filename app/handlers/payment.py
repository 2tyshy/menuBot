from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext

from app.keyboards.inline import inline_payment_online, inline_payment_methods
from app.keyboards.reply import reply_main_menu
from app.storage import get_cart, commit_order
from .delivery import DeliveryFSM

router = Router()

@router.callback_query(DeliveryFSM.confirm, F.data == "pay:cash")
async def pay_cash(call: CallbackQuery, state: FSMContext) -> None:
    data = await state.get_data()
    payment = {"method": "cash", "status": "to_collect"}
    order = commit_order(call.from_user.id, delivery=data, payment=payment)
    await state.clear()
    await call.message.edit_text(
        f"<b>Заказ оформлен!</b>\nНомер позиций: {len(order['lines'])}\nИтого к оплате при доставке: {order['total']} VND",
        reply_markup=None,
    )
    await call.message.answer("Вы в главном меню", reply_markup=reply_main_menu())
    await call.answer("Оплата при получении")

@router.callback_query(DeliveryFSM.confirm, F.data == "pay:online")
async def pay_online(call: CallbackQuery) -> None:
    await call.message.edit_text(
        "Онлайн-оплата (мок). Нажмите кнопку, чтобы имитировать успешный платёж.",
        reply_markup=inline_payment_online(),
    )
    await call.answer()

@router.callback_query(F.data == "pay:online:confirm")
async def pay_online_confirm(call: CallbackQuery, state: FSMContext) -> None:
    data = await state.get_data()
    payment = {"method": "online", "status": "paid"}
    order = commit_order(call.from_user.id, delivery=data, payment=payment)
    await state.clear()
    await call.message.edit_text(
        f"<b>Оплата прошла успешно (мок)!</b>\nЗаказ подтверждён. Сумма: {order['total']} VND",
        reply_markup=None,
    )
    await call.answer("Оплачено")
