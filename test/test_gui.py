import unittest
from module_name.gui import RestaurantMenuApp

class TestRestaurantMenuApp(unittest.TestCase):
    def test_order_summary(self):
        # Create a mock Tkinter root window
        root = tk.Tk()

        # Create an instance of RestaurantMenuApp
        app = RestaurantMenuApp(root)

        # Set some values for testing
        app.pizza_quantity.set("2")
        app.pizza_size.set("Large")
        app.burger_quantity.set("1")
        app.burger_size.set("Classic")
        app.soft_drink_quantity.set("3")
        app.order_type.set("Dine In")
        app.extra_cheese_var.set(1)
        app.extra_ketchup_var.set(0)

        # Call the show_order_summary method
        app.show_order_summary()

        # Test the messagebox content (can't be directly tested)
        # Ensure all the details are correctly displayed in the summary

if __name__ ==
