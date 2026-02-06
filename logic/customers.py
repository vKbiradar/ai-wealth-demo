import json
from pathlib import Path
from typing import List, Dict

CUSTOMER_STORE = Path(__file__).resolve().parents[1] / "data" / "customers.json"


def _ensure_store() -> None:
    CUSTOMER_STORE.parent.mkdir(parents=True, exist_ok=True)
    if not CUSTOMER_STORE.exists():
        CUSTOMER_STORE.write_text("[]", encoding="utf-8")


def load_customers() -> List[Dict[str, str]]:
    _ensure_store()
    return json.loads(CUSTOMER_STORE.read_text(encoding="utf-8"))


def save_customers(customers: List[Dict[str, str]]) -> None:
    _ensure_store()
    CUSTOMER_STORE.write_text(
        json.dumps(customers, indent=2, sort_keys=True), encoding="utf-8"
    )


def register_customer(username: str, password: str) -> bool:
    customers = load_customers()
    if any(customer["username"].lower() == username.lower() for customer in customers):
        return False
    customers.append({"username": username, "password": password})
    save_customers(customers)
    return True


def authenticate_customer(username: str, password: str) -> bool:
    customers = load_customers()
    return any(
        customer["username"].lower() == username.lower()
        and customer["password"] == password
        for customer in customers
    )
