from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from typing import Iterable

BACK = "back:root"


def inline_menu_root() -> InlineKeyboardMarkup:
    kb = [
        [InlineKeyboardButton(text="Первое блюдо", callback_data="menu:cat:first")],
        [InlineKeyboardButton(text="Второе блюдо", callback_data="menu:cat:second")],
        [InlineKeyboardButton(text="Компот", callback_data="menu:cat:drink")],
        [InlineKeyboardButton(text="⬅ Назад", callback_data=BACK)],
    ]
    return InlineKeyboardMarkup(inline_keyboard=kb)


def inline_items_list(category: str, item_skus: Iterable[str]) -> InlineKeyboardMarkup:
    rows = [[InlineKeyboardButton(text="⬅ Назад", callback_data="menu:back")]]
    # Кнопки на карточках будут отдельными
    return InlineKeyboardMarkup(inline_keyboard=rows)


def inline_item_actions(sku: str) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="➕ В корзину", callback_data=f"cart:add:{sku}")],
        [InlineKeyboardButton(text="⬅ Назад", callback_data="menu:back")],
    ])


def inline_cart_controls() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🗑 Очистить", callback_data="cart:clear")],
        [InlineKeyboardButton(text="🚚 Оформить доставку", callback_data="cart:checkout")],
    ])


def inline_cart_item_remove(sku: str) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="❌ Удалить", callback_data=f"cart:rm:{sku}")],
    ])


def inline_payment_methods() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Наличными", callback_data="pay:cash")],
        [InlineKeyboardButton(text="Онлайн (мок)", callback_data="pay:online")],
        [InlineKeyboardButton(text="⬅ Назад", callback_data="pay:back")],
    ])


def inline_payment_online() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Оплатить (мок)", callback_data="pay:online:confirm")],
        [InlineKeyboardButton(text="⬅ Назад", callback_data="pay:back")],
    ])
