from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, InputMediaPhoto

from app.keyboards.inline import inline_menu_root, inline_item_actions
from app.storage import CATEGORIES, MENU_ITEMS

router = Router()

async def show_menu_root(message: Message) -> None:
    text = "<b>Меню</b> — выберите категорию:"
    await message.answer(text, reply_markup=inline_menu_root())

@router.callback_query(F.data == "back:root")
@router.callback_query(F.data == "menu:back")
async def back_to_menu_root(call: CallbackQuery) -> None:
    await call.message.edit_text("<b>Меню</b> — выберите категорию:", reply_markup=inline_menu_root())
    await call.answer()

@router.callback_query(F.data.startswith("menu:cat:"))
async def open_category(call: CallbackQuery) -> None:
    _, _, cat = call.data.split(":", 2)
    # Покажем карточки по одной (проще для демо)
    items = MENU_ITEMS.get(cat, [])
    if not items:
        await call.answer("Пусто", show_alert=True)
        return
    # Показать первую карточку, далее пользователь может жать Назад вверху
    it = items[0]
    caption = f"<b>{it['title']}</b>\n{it['desc']}\nЦена: {it['price']} VND"
    await call.message.edit_media(
        media=InputMediaPhoto(media=it["photo"], caption=caption),
        reply_markup=inline_item_actions(it["sku"]),
    )
    await call.answer()

# Для краткости в демо обрабатываем добавление в корзину тут, а навигацию назад — общим хэндлером выше
