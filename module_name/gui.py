import tkinter as tk
from tkinter import messagebox

class RestaurantMenuApp:
    def __init__(self, master):
        self.master = master
        master.title("Restaurant Menu Application")

        # Create labels
        self.pizza_label = tk.Label(master, text="Pizza:")
        self.burger_label = tk.Label(master, text="Burger:")
        self.soft_drink_label = tk.Label(master, text="Soft Drink:")
        self.order_type_label = tk.Label(master, text="Order Type:")
        self.extras_label = tk.Label(master, text="Extras:")

        # Create dropdowns
        self.pizza_quantity = tk.StringVar(master)
        self.pizza_quantity.set("1")
        self.pizza_size = tk.StringVar(master)
        self.pizza_size.set("Small")
        self.pizza_options = ["Small", "Medium", "Large"]
        self.pizza_quantity_dropdown = tk.OptionMenu(master, self.pizza_quantity, *range(1, 11))
        self.pizza_size_dropdown = tk.OptionMenu(master, self.pizza_size, *self.pizza_options)

        self.burger_quantity = tk.StringVar(master)
        self.burger_quantity.set("1")
        self.burger_size = tk.StringVar(master)
        self.burger_size.set("Classic")
        self.burger_options = ["Classic", "Big"]
        self.burger_quantity_dropdown = tk.OptionMenu(master, self.burger_quantity, *range(1, 11))
        self.burger_size_dropdown = tk.OptionMenu(master, self.burger_size, *self.burger_options)

        self.soft_drink_quantity = tk.StringVar(master)
        self.soft_drink_quantity.set("1")
        self.soft_drink_quantity_dropdown = tk.OptionMenu(master, self.soft_drink_quantity, *range(1, 11))

        # Create radio buttons
        self.order_type = tk.StringVar(master)
        self.order_type.set("Takeaway")
        self.order_type_takeaway = tk.Radiobutton(master, text="Takeaway", variable=self.order_type, value="Takeaway")
        self.order_type_dine_in = tk.Radiobutton(master, text="Dine In", variable=self.order_type, value="Dine In")

        # Create checkboxes
        self.extra_cheese_var = tk.IntVar(master)
        self.extra_ketchup_var = tk.IntVar(master)
        self.extra_cheese_checkbox = tk.Checkbutton(master, text="Extra Cheese", variable=self.extra_cheese_var)
        self.extra_ketchup_checkbox = tk.Checkbutton(master, text="Extra Ketchup", variable=self.extra_ketchup_var)

        # Create order summary button
        self.order_summary_button = tk.Button(master, text="Order Summary", command=self.show_order_summary)

        # Grid layout
        self.pizza_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.pizza_quantity_dropdown.grid(row=0, column=1, padx=5, pady=5)
        self.pizza_size_dropdown.grid(row=0, column=2, padx=5, pady=5)

        self.burger_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.burger_quantity_dropdown.grid(row=1, column=1, padx=5, pady=5)
        self.burger_size_dropdown.grid(row=1, column=2, padx=5, pady=5)

        self.soft_drink_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.soft_drink_quantity_dropdown.grid(row=2, column=1, padx=5, pady=5)

        self.order_type_label.grid(row=3, column=0, padx=5, pady=5, sticky="w")
        self.order_type_takeaway.grid(row=3, column=1, padx=5, pady=5, sticky="w")
        self.order_type_dine_in.grid(row=3, column=2, padx=5, pady=5, sticky="w")

        self.extras_label.grid(row=4, column=0, padx=5, pady=5, sticky="w")
        self.extra_cheese_checkbox.grid(row=4, column=1, padx=5, pady=5, sticky="w")
        self.extra_ketchup_checkbox.grid(row=4, column=2, padx=5, pady=5, sticky="w")

        self.order_summary_button.grid(row=5, column=0, columnspan=3, padx=5, pady=10)

    def show_order_summary(self):
        summary = f"Order Summary:\n\n"
        summary += f"Pizza: {self.pizza_quantity.get()} x {self.pizza_size.get()}\n"
        summary += f"Burger: {self.burger_quantity.get()} x {self.burger_size.get()}\n"
        summary += f"Soft Drink: {self.soft_drink_quantity.get()}\n"
        summary += f"Order Type: {self.order_type.get()}\n"
        if self.extra_cheese_var.get():
            summary += "Extra Cheese: Yes\n"
        if self.extra_ketchup_var.get():
            summary += "Extra Ketchup: Yes\n"

        messagebox.showinfo("Order Summary", summary)

def run_app():
    root = tk.Tk()
    app = RestaurantMenuApp(root)
    root.mainloop()

if __name__ == "__main__":
    run_app()
