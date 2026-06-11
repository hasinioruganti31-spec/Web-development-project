from fastapi import FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from typing import Optional

app = FastAPI(
    title="Food Delivery API",
    version="1.0.0"
)

# ---------------- CORS ----------------

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],      # Frontend URLs
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------------- DATA ----------------

menu = [
    {"id": 1, "name": "Pizza", "price": 200, "category": "Food", "is_available": True},
    {"id": 2, "name": "Burger", "price": 120, "category": "Food", "is_available": True},
    {"id": 3, "name": "Fries", "price": 80, "category": "Food", "is_available": True},
    {"id": 4, "name": "Coke", "price": 40, "category": "Drink", "is_available": True},
    {"id": 5, "name": "IceCream", "price": 60, "category": "Dessert", "is_available": True},
]

orders = []
cart = []
order_counter = 1


# ---------------- HELPERS ----------------

def find_item(item_id):
    for item in menu:
        if item["id"] == item_id:
            return item
    return None


def calculate_bill(price, qty, order_type):
    total = price * qty

    if order_type.lower() == "delivery":
        total += 30

    return total


# ---------------- MODELS ----------------

class OrderRequest(BaseModel):
    customer_name: str
    item_id: int
    quantity: int = Field(gt=0)
    delivery_address: str
    order_type: str = "delivery"


class MenuItem(BaseModel):
    name: str
    price: int = Field(gt=0)
    category: str
    is_available: bool = True


class CheckoutRequest(BaseModel):
    customer_name: str
    delivery_address: str


# ---------------- HOME ----------------

@app.get("/")
def home():
    return {
        "message": "Welcome to Food Delivery API"
    }


# ---------------- MENU ----------------

@app.get("/menu")
def get_menu():
    return menu


@app.get("/menu/{item_id}")
def get_item(item_id: int):

    item = find_item(item_id)

    if not item:
        raise HTTPException(
            status_code=404,
            detail="Item not found"
        )

    return item


@app.post("/menu", status_code=status.HTTP_201_CREATED)
def add_item(item: MenuItem):

    new_item = item.dict()

    new_item["id"] = len(menu) + 1

    menu.append(new_item)

    return new_item


@app.put("/menu/{item_id}")
def update_item(
    item_id: int,
    price: Optional[int] = None
):

    item = find_item(item_id)

    if not item:
        raise HTTPException(
            status_code=404,
            detail="Item not found"
        )

    if price is not None:
        item["price"] = price

    return item


@app.delete("/menu/{item_id}")
def delete_item(item_id: int):

    item = find_item(item_id)

    if not item:
        raise HTTPException(
            status_code=404,
            detail="Item not found"
        )

    menu.remove(item)

    return {
        "message": "Item deleted successfully"
    }


# ---------------- SEARCH ----------------

@app.get("/menu/search")
def search_menu(keyword: str):

    result = [
        item for item in menu
        if keyword.lower() in item["name"].lower()
    ]

    return result


# ---------------- FILTER ----------------

@app.get("/menu/filter")
def filter_menu(
    category: Optional[str] = None,
    max_price: Optional[int] = None,
    is_available: Optional[bool] = None
):

    result = menu

    if category:
        result = [
            item for item in result
            if item["category"].lower() == category.lower()
        ]

    if max_price is not None:
        result = [
            item for item in result
            if item["price"] <= max_price
        ]

    if is_available is not None:
        result = [
            item for item in result
            if item["is_available"] == is_available
        ]

    return result


# ---------------- SORT ----------------

@app.get("/menu/sort")
def sort_menu(
    sort_by: str = "price",
    order: str = "asc"
):

    valid_fields = [
        "id",
        "name",
        "price",
        "category"
    ]

    if sort_by not in valid_fields:
        return {
            "error": "Invalid sort field"
        }

    reverse = order == "desc"

    return sorted(
        menu,
        key=lambda x: x[sort_by],
        reverse=reverse
    )


# ---------------- PAGINATION ----------------

@app.get("/menu/page")
def paginate(
    page: int = 1,
    limit: int = 2
):

    start = (page - 1) * limit

    end = start + limit

    return menu[start:end]


# ---------------- ORDERS ----------------

@app.post("/orders")
def place_order(req: OrderRequest):

    global order_counter

    item = find_item(req.item_id)

    if not item:
        raise HTTPException(
            status_code=404,
            detail="Item not found"
        )

    total = calculate_bill(
        item["price"],
        req.quantity,
        req.order_type
    )

    order = {
        "order_id": order_counter,
        "customer_name": req.customer_name,
        "item": item["name"],
        "quantity": req.quantity,
        "order_type": req.order_type,
        "delivery_address": req.delivery_address,
        "total_amount": total
    }

    orders.append(order)

    order_counter += 1

    return order


@app.get("/orders")
def get_orders():
    return orders


# ---------------- CART ----------------

@app.post("/cart/add")
def add_to_cart(
    item_id: int,
    quantity: int = 1
):

    item = find_item(item_id)

    if not item:
        raise HTTPException(
            status_code=404,
            detail="Item not found"
        )

    cart.append({
        "item_id": item["id"],
        "name": item["name"],
        "price": item["price"],
        "qty": quantity
    })

    return {
        "message": "Added to cart",
        "cart": cart
    }


@app.get("/cart")
def view_cart():

    total = sum(
        item["price"] * item["qty"]
        for item in cart
    )

    return {
        "cart": cart,
        "total": total
    }


@app.delete("/cart/{item_id}")
def remove_from_cart(item_id: int):

    for item in cart:
        if item["item_id"] == item_id:
            cart.remove(item)
            return {
                "message": "Item removed"
            }

    raise HTTPException(
        status_code=404,
        detail="Item not found in cart"
    )


# ---------------- CHECKOUT ----------------

@app.post("/cart/checkout")
def checkout(req: CheckoutRequest):

    global order_counter

    if not cart:
        return {
            "error": "Cart is empty"
        }

    for item in cart:

        order = {
            "order_id": order_counter,
            "customer_name": req.customer_name,
            "item": item["name"],
            "quantity": item["qty"],
            "delivery_address": req.delivery_address,
            "total": item["price"] * item["qty"]
        }

        orders.append(order)

        order_counter += 1

    cart.clear()

    return {
        "message": "Checkout successful",
        "orders": orders
    }