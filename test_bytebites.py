import unittest

from models import Customer, FoodItem, Menu, Order


def make_sample_menu() -> Menu:
    """Build a small menu with items across three categories."""
    menu = Menu()
    menu.add_item(FoodItem("Spicy Burger", 8.50, "Food", 4.2))
    menu.add_item(FoodItem("Large Soda", 2.00, "Drinks", 3.9))
    menu.add_item(FoodItem("Brownie", 3.25, "Desserts", 4.8))
    menu.add_item(FoodItem("Iced Tea", 1.75, "Drinks", 4.5))
    return menu


class TestSampleMenu(unittest.TestCase):
    """Checks that the sample menu is built as expected."""

    def test_sample_menu_holds_all_items(self) -> None:
        menu = make_sample_menu()
        self.assertEqual(len(menu.items), 4)


class TestOrder(unittest.TestCase):
    """Behaviors of an order's total cost."""

    def test_calculate_total_with_multiple_items(self) -> None:
        menu = make_sample_menu()
        order = Order()
        order.add_item(menu.items[0])  # Spicy Burger 8.50
        order.add_item(menu.items[1])  # Large Soda 2.00
        order.add_item(menu.items[1])  # second Large Soda 2.00
        self.assertEqual(order.calculate_total(), 12.50)

    def test_order_total_is_zero_when_empty(self) -> None:
        self.assertEqual(Order().calculate_total(), 0.0)


class TestMenu(unittest.TestCase):
    """Behaviors of filtering and sorting the menu."""

    def setUp(self) -> None:
        self.menu = make_sample_menu()

    def test_filter_by_category(self) -> None:
        drinks = self.menu.filter_by_category("Drinks")
        self.assertEqual([item.name for item in drinks], ["Large Soda", "Iced Tea"])

    def test_filter_by_category_ignores_case(self) -> None:
        drinks = self.menu.filter_by_category("drinks")
        self.assertEqual(len(drinks), 2)

    def test_filter_by_unknown_category_returns_empty_list(self) -> None:
        self.assertEqual(self.menu.filter_by_category("Pizza"), [])

    def test_sort_by_popularity_orders_descending(self) -> None:
        ratings = [item.popularity_rating for item in self.menu.sort_by_popularity()]
        self.assertEqual(ratings, [4.8, 4.5, 4.2, 3.9])

    def test_sort_by_popularity_does_not_change_menu_order(self) -> None:
        self.menu.sort_by_popularity()
        self.assertEqual(self.menu.items[0].name, "Spicy Burger")


class TestCustomer(unittest.TestCase):
    """Behaviors of a customer's purchase history."""

    def test_customer_records_order_history(self) -> None:
        customer = Customer("Ana")
        order = Order()
        order.add_item(make_sample_menu().items[0])
        customer.add_order(order)
        self.assertEqual(customer.purchase_history, [order])

    def test_customer_rejects_empty_order(self) -> None:
        customer = Customer("Ana")
        with self.assertRaises(ValueError):
            customer.add_order(Order())
        self.assertEqual(customer.purchase_history, [])

    def test_customers_do_not_share_history(self) -> None:
        ana = Customer("Ana")
        ben = Customer("Ben")
        order = Order()
        order.add_item(make_sample_menu().items[0])
        ana.add_order(order)
        self.assertEqual(len(ana.purchase_history), 1)
        self.assertEqual(ben.purchase_history, [])

"""python3 -m unittest test_bytebites -v """
if __name__ == "__main__":
    unittest.main()
