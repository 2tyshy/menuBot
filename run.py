from aiogram import Bot, Dispatcher
from aiogram.client.bot import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import BotCommand
import asyncio

from app.config import load_settings
from app.logger import setup_logging
from app.handlers import register_handlers

async def set_commands(bot: Bot) -> None:
    commands = [
        BotCommand(command="start", description="Перезапуск бота / главное меню"),
    ]
    await bot.set_my_commands(commands)

async def main() -> None:
    setup_logging()
    settings = load_settings()

    bot = Bot(token=settings.BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp = Dispatcher(storage=MemoryStorage())

    register_handlers(dp)
    await set_commands(bot)

    try:
        await dp.start_polling(bot)
    except KeyboardInterrupt:
        print("\nBot stopped by user")

if __name__ == "__main__":
    asyncio.run(main())
