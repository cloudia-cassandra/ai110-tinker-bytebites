"""
ByteBites - backend models
Four classes model the campus food-ordering domain described in `bytebites_spec.md`:


  - Customer   : a real user, tracked by name and past orders.
  - FoodItem   : a single sellable item (name, price, category, popularity).
  - Menu       : the full catalog of FoodItems, with a filter helper.
  - Order      : one transaction — the FoodItems a customer is buying now.

Relationships are composition, not inheritance: a Menu *contains* FoodItems,
an Order *contains* FoodItems, and a Customer *has* a history of Orders. No
class inherits from another. Scope is intentionally limited to the spec — no
authentication, database, or discount logic.
"""

from __future__ import annotations


class Customer:
    """A real user, tracked by name and past orders."""

    def __init__(self, name: str) -> None:
        self.name = name
        self.purchase_history: list[Order] = []

    def add_order(self, order: Order) -> None:
        """Record a completed order in this customer's purchase history."""
        pass


class FoodItem:
    """A single sellable item on the menu."""

    def __init__(
        self, name: str, price: float, category: str, popularity_rating: float
    ) -> None:
        self.name = name
        self.price = price
        self.category = category
        self.popularity_rating = popularity_rating


class Menu:
    """The full catalog of food items."""

    def __init__(self) -> None:
        self.items: list[FoodItem] = []

    def add_item(self, item: FoodItem) -> None:
        """Add a food item to the menu."""
        pass

    def filter_by_category(self, category: str) -> list[FoodItem]:
        """Return the menu items that belong to the given category."""
        pass


class Order:
    """One transaction grouping the food items a customer is buying."""

    def __init__(self) -> None:
        self.items: list[FoodItem] = []

    def add_item(self, item: FoodItem) -> None:
        """Add a food item to this order."""
        pass

    def calculate_total(self) -> float:
        """Return the total cost of the items in this order."""
        pass
