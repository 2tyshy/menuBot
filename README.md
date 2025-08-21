# Telegram Café Bot (aiogram v3)

"Из коробки" Telegram-бот для кафе: Меню → Корзина → Доставка → Оплата (моки), Связаться. 
Без БД, все данные в памяти. Готов для быстрого демо.

## Запуск
1. Python 3.11+
2. `python -m venv .venv && source .venv/bin/activate`  (Windows: `.venv\\Scripts\\activate`)
3. `pip install -r requirements.txt`
4. Скопируйте `.env.example` в `.env` и вставьте токен бота
5. `python run.py`

## Разделы
- 🍽 Меню (категории: Первое блюдо / Второе блюдо / Компот) → карточки блюд → добавление в корзину
- 🧺 Корзина (удаление, очистка, оформить доставку)
- 🚚 Доставка (FSM: адрес → имя → телефон → подтверждение)
- 💳 Оплата (мок: Наличными / Онлайн)
- 📞 Связаться (контакты, “Написать администратору”)

## Структура
```
/app
  __init__.py
  config.py
  logger.py
  storage.py
  /keyboards
    __init__.py
    reply.py
    inline.py
  /handlers
    __init__.py
    common.py
    menu.py
    cart.py
    delivery.py
    payment.py
    contact.py
run.py
```
