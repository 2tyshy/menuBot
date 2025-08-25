from aiogram import Router, types
from aiogram.filters import CommandStart, Command
from aiogram.utils.keyboard import InlineKeyboardBuilder

from typing import List
from dataclasses import dataclass
from aiogram import types

@dataclass
class MenuItem:
    name: str
    description: str
    price: float
    image_url: str

def generate_menu_items() -> List[MenuItem]:
    # Implementation of generate_menu_items
    items = [
        MenuItem(
            name="Пицца 'Маргарита'",
            description="Классическая пицца с томатами, моцареллой и базиликом.",
            price=350.00,
            image_url="https://example.com/images/margarita.jpg"
        ),
        MenuItem(
            name="Паста 'Карбонара'",
            description="Паста с беконом, яйцом, пармезаном и черным перцем.",
            price=420.00,
            image_url="https://example.com/images/carbonara.jpg"
        ),
        MenuItem(
            name="Салат 'Цезарь'",
            description="Салат с курицей, листьями салата ромэн, гренками и соусом 'Цезарь'.",
            price=380.00,
            image_url="https://example.com/images/caesar.jpg"
        ),
        MenuItem(
            name="Бургер 'Чизбургер'",
            description="Бургер с говяжьей котлетой, сыром чеддер, луком, солеными огурцами и соусом.",
            price=450.00,
            image_url="https://example.com/images/cheeseburger.jpg"
        ),
        MenuItem(
            name="Суп 'Том Ям'",
            description="Традиционный тайский суп с креветками, грибами, помидорами и кокосовым молоком.",
            price=500.00,
            image_url="https://example.com/images/tom_yum.jpg"
        ),
        MenuItem(
            name="Ролл 'Филадельфия'",
            description="Ролл с лососем, сливочным сыром и авокадо.",
            price=600.00,
            image_url="https://example.com/images/philadelphia.jpg"
        ),
    ]

    return items


router = Router()

@router.message(Command("menu"))
async def menu_command(message: types.Message):
    menu_items = generate_menu_items()

    builder = InlineKeyboardBuilder()
    for item in menu_items:    
        builder.button(text=item.name, callback_data=f"menu_item:{item.name}")

    builder.adjust_cols(2)
    await message.answer("Menu:", reply_markup=builder.as_markup())

def register_menu_handlers(dp):
    dp.include_router(router)