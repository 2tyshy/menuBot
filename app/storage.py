"""In-memory хранилище мок-данных: меню, склад, корзины, заказы."""
from __future__ import annotations
from dataclasses import dataclass, field
from typing import Dict, List, Optional

# Категории меню
CATEGORIES = [
    ("first", "Первое блюдо"),
    ("second", "Второе блюдо"),
    ("drink", "Компот"),
]

# Мок-товары (sku должны быть уникальны)
MENU_ITEMS = {
    "first": [
        {
            "sku": "soup_01",
            "title": "Суп дня",
            "desc": "Ароматный суп с овощами и специями",
            "price": 45000,
            "photo": "https://picsum.photos/seed/soup/800/600",
            "stock": 20,
        },
        {
            "sku": "borsch_01",
            "title": "Борщ",
            "desc": "Классический борщ со сметаной",
            "price": 55000,
            "photo": "https://picsum.photos/seed/borsch/800/600",
            "stock": 15,
        },
    ],
    "second": [
        {
            "sku": "steak_01",
            "title": "Стейк",
            "desc": "Мраморная говядина средней прожарки",
            "price": 145000,
            "photo": "https://picsum.photos/seed/steak/800/600",
            "stock": 10,
        },
        {
            "sku": "pasta_01",
            "title": "Паста",
            "desc": "Паста с соусом из вяленых томатов",
            "price": 89000,
            "photo": "https://picsum.photos/seed/pasta/800/600",
            "stock": 18,
        },
    ],
    "drink": [
        {
            "sku": "compote_01",
            "title": "Компот",
            "desc": "Домашний ягодный компот",
            "price": 25000,
            "photo": "https://picsum.photos/seed/juice/800/600",
            "stock": 50,
        },
        {
            "sku": "morse_01",
            "title": "Морс",
            "desc": "Освежающий клюквенный морс",
            "price": 27000,
            "photo": "https://picsum.photos/seed/morse/800/600",
            "stock": 40,
        },
    ],
}

# Простейший индекс sku -> товар
SKU_INDEX: Dict[str, Dict] = {it["sku"]: it for arr in MENU_ITEMS.values() for it in arr}

@dataclass
class CartItem:
    sku: str
    qty: int = 1

@dataclass
class Cart:
    items: Dict[str, CartItem] = field(default_factory=dict)

    def add(self, sku: str, qty: int = 1) -> None:
        # проверка запаса
        stock = SKU_INDEX.get(sku, {}).get("stock", 0)
        current = self.items.get(sku, CartItem(sku, 0)).qty
        if current + qty > stock:
            raise ValueError("Недостаточно на складе")
        self.items[sku] = CartItem(sku, current + qty)

    def remove(self, sku: str) -> None:
        if sku in self.items:
            del self.items[sku]

    def clear(self) -> None:
        self.items.clear()

    def total(self) -> int:
        s = 0
        for ci in self.items.values():
            price = SKU_INDEX[ci.sku]["price"]
            s += price * ci.qty
        return s

    def as_lines(self) -> List[str]:
        lines = []
        for ci in self.items.values():
            data = SKU_INDEX[ci.sku]
            lines.append(f"• {data['title']} x{ci.qty} — {data['price']*ci.qty} VND")
        if not lines:
            lines.append("Корзина пуста")
        return lines

# user_id -> Cart
CARTS: Dict[int, Cart] = {}

# Заказы (мок)
ORDERS: List[Dict] = []


def get_cart(user_id: int) -> Cart:
    if user_id not in CARTS:
        CARTS[user_id] = Cart()
    return CARTS[user_id]


def commit_order(user_id: int, delivery: Dict, payment: Dict) -> Dict:
    """Создать мок-заказ и списать склад."""
    cart = get_cart(user_id)
    # списание склада
    for ci in cart.items.values():
        SKU_INDEX[ci.sku]["stock"] -= ci.qty
    order = {
        "user_id": user_id,
        "lines": [{"sku": sku, "qty": ci.qty} for sku, ci in cart.items.items()],
        "total": cart.total(),
        "delivery": delivery,
        "payment": payment,
        "status": "CONFIRMED",
    }
    ORDERS.append(order)
    cart.clear()
    return order
