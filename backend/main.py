"""FastAPI application exposing menu, cart, delivery and payment endpoints.

These endpoints mirror the business logic of the Telegram bot handlers
implemented in :mod:`app.handlers` and use the in-memory storage from
``app.storage``.  The API is intentionally simple and stores cart and delivery
information in memory for demonstration purposes.
"""

from __future__ import annotations

from typing import Dict, List
from uuid import uuid4

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from app.storage import MENU_ITEMS, SKU_INDEX, get_cart, commit_order


app = FastAPI(title="menuBot API")


@app.get("/api/menu")
def api_menu() -> Dict[str, List[Dict]]:
    """Return available menu items grouped by category."""
    return MENU_ITEMS


class CartItem(BaseModel):
    sku: str
    qty: int = 1


@app.get("/api/cart")
def api_get_cart(user_id: int = 1) -> Dict:
    """Return current cart contents for ``user_id``."""
    cart = get_cart(user_id)
    items = []
    for ci in cart.items.values():
        data = SKU_INDEX.get(ci.sku)
        if not data:
            continue
        items.append({**data, "qty": ci.qty})
    return {"items": items, "total": cart.total()}


@app.post("/api/cart")
def api_add_cart(item: CartItem, user_id: int = 1) -> Dict:
    """Add an item to the cart."""
    cart = get_cart(user_id)
    try:
        cart.add(item.sku, item.qty)
    except ValueError as exc:  # pragma: no cover - simple error propagation
        raise HTTPException(status_code=400, detail=str(exc)) from exc
    return api_get_cart(user_id)


@app.delete("/api/cart/{sku}")
def api_remove_cart(sku: str, user_id: int = 1) -> Dict:
    """Remove an item from the cart by SKU."""
    cart = get_cart(user_id)
    cart.remove(sku)
    return api_get_cart(user_id)


class DeliveryInfo(BaseModel):
    address: str
    name: str
    phone: str


_delivery_data: Dict[int, DeliveryInfo] = {}


@app.post("/api/delivery")
def api_delivery(info: DeliveryInfo, user_id: int = 1) -> Dict[str, str]:
    """Store delivery information for ``user_id``."""
    _delivery_data[user_id] = info
    return {"status": "ok"}


class PaymentRequest(BaseModel):
    method: str  # "cash" or "online"


@app.post("/api/payment")
def api_payment(req: PaymentRequest, user_id: int = 1) -> Dict:
    """Mock payment processing and create an order."""
    delivery = _delivery_data.get(user_id, DeliveryInfo(address="", name="", phone=""))
    payment = {
        "method": req.method,
        "transaction_id": f"TX-{uuid4().hex[:8]}",
    }
    order = commit_order(user_id, delivery.model_dump(), payment)
    return {"status": "ok", "order": order}

