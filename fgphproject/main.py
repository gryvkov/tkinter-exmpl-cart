import tkinter as tk
from fgphproject.App import App
from fgphproject.model.order import Order

if __name__ == "__main__":
    # take id from db
    order_id = 1
    order = Order("Greg", "Haifa, Morgan-Guerrero st 28 - 6", order_id)

    # unroll order form
    root = tk.Tk()
    root.title("Order " + str(order_id) + " " + order.name + " " + order.address)

    # Set the form theme
    root.tk.call("source", "azure.tcl")
    root.tk.call("set_theme", "light")

    # App context
    app = App(root)
    app.pack(fill="both", expand=True)

    # Set a minsize for the window
    root.update()
    root.minsize(root.winfo_width(), root.winfo_height())

    root.mainloop()
