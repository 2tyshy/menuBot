from aiogram import Dispatcher
from . import menu_handler


def register_handlers(dp: Dispatcher):
    menu_handler.register_menu_handlers(dp)
