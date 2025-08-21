from aiogram import Dispatcher
from .common import router as common_router
from .menu import router as menu_router
from .cart import router as cart_router
from .delivery import router as delivery_router
from .payment import router as payment_router
from .contact import router as contact_router


def register_handlers(dp: Dispatcher) -> None:
    dp.include_router(common_router)
    dp.include_router(menu_router)
    dp.include_router(cart_router)
    dp.include_router(delivery_router)
    dp.include_router(payment_router)
    dp.include_router(contact_router)
