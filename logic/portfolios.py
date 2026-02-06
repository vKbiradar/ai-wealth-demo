import json
from pathlib import Path
from typing import Dict

PORTFOLIO_STORE = Path(__file__).resolve().parents[1] / "data" / "portfolios.json"
DEFAULT_ALLOCATION = {"equity": 60, "debt": 30, "gold": 10}


def _ensure_store() -> None:
    PORTFOLIO_STORE.parent.mkdir(parents=True, exist_ok=True)
    if not PORTFOLIO_STORE.exists():
        PORTFOLIO_STORE.write_text("{}", encoding="utf-8")


def load_portfolios() -> Dict[str, Dict[str, int]]:
    _ensure_store()
    return json.loads(PORTFOLIO_STORE.read_text(encoding="utf-8"))


def save_portfolios(portfolios: Dict[str, Dict[str, int]]) -> None:
    _ensure_store()
    PORTFOLIO_STORE.write_text(
        json.dumps(portfolios, indent=2, sort_keys=True), encoding="utf-8"
    )


def get_allocation(username: str) -> Dict[str, int]:
    portfolios = load_portfolios()
    allocation = portfolios.get(username)
    if allocation is None:
        return DEFAULT_ALLOCATION.copy()
    return {
        "equity": int(allocation.get("equity", DEFAULT_ALLOCATION["equity"])),
        "debt": int(allocation.get("debt", DEFAULT_ALLOCATION["debt"])),
        "gold": int(allocation.get("gold", DEFAULT_ALLOCATION["gold"])),
    }


def set_allocation(username: str, allocation: Dict[str, int]) -> None:
    portfolios = load_portfolios()
    portfolios[username] = {
        "equity": int(allocation["equity"]),
        "debt": int(allocation["debt"]),
        "gold": int(allocation["gold"]),
    }
    save_portfolios(portfolios)
