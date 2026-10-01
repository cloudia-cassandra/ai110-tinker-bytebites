"""
ByteBites - backend models
Four classes model the campus food-ordering domain described in `bytebites_spec.md`:


  - Customer   : a real user, tracked by name and past orders.
  - FoodItem   : a single sellable item (name, price, category, popularity).
  - Menu       : the full catalog of FoodItems, with filter/sort helpers.
  - Order      : one transaction — the FoodItems a customer is buying now.

Relationships are composition, not inheritance: a Menu *contains* FoodItems,
an Order *contains* FoodItems, and a Customer *has* a history of Orders. No
class inherits from another. Scope is intentionally limited to the spec — no
authentication, database, or discount logic.
"""

class Customer:


class FoodItem:


class Menu:


class Order:


