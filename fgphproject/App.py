import tkinter as tk
from tkinter import ttk

from fgphproject.model.product import Product


class App(ttk.Frame):
    def __init__(self, parent):
        # Create value lists
        self.item_list = ["Выбрать товар"]
        self.fillItemList()

        # Create control variables
        self.var_4 = tk.StringVar(value=self.item_list[1])

        # main frame attributes
        ttk.Frame.__init__(self)
        # cart
        self.addition_frame = ttk.LabelFrame(self, text="Заполнение корзины", padding=(20, 10))
        self.spinbox = ttk.Spinbox(self.addition_frame, from_=0, to=99999, increment=1)
        self.item_menu = ttk.OptionMenu(self.addition_frame, self.var_4, *self.item_list)
        self.widgets_frame = ttk.Frame(self, padding=(0, 0, 0, 10))
        self.addToCart_button = ttk.Button(self.widgets_frame, text="В корзину", style="Accent.TButton")
        self.addToOrder_button = ttk.Button(self.widgets_frame, text="Перенести в заказ", style="Accent.TButton")
        self.paned_1 = ttk.PanedWindow(self.addition_frame)
        self.pane_cart = ttk.Frame(self.paned_1, padding=5)

        # comment section
        self.comment_frame = ttk.LabelFrame(self, text="Комментарий", padding=(20, 10))
        self.comment = ttk.Entry(self.comment_frame)
        self.switch = ttk.Checkbutton(self.comment_frame, text="Switch theme", style="Switch.TCheckbutton")
        # order
        self.paned = ttk.PanedWindow(self)
        self.pane_order = ttk.Frame(self.paned, padding=5)
        self.scrollbarOrder = ttk.Scrollbar(self.pane_order)
        self.tree = ttk.Treeview(self.pane_order, selectmode="browse", yscrollcommand=self.scrollbarOrder.set,
                                 columns=(1, 2, 3), height=10, )

        # Make the app responsive
        for index in [0, 1, 2]:
            self.columnconfigure(index=index, weight=1)
            self.rowconfigure(index=index, weight=1)

        # Create widgets :)
        self.setup_widgets()

    def fillItemList(self):
        for item in Product().getItems():
            self.item_list.append(item)

    # Process event

    def setup_widgets(self):
        # Frame for the fill the cart
        self.addition_frame.grid(
            row=0, column=0, padx=(20, 10), pady=(20, 10), sticky="nsew"
        )

        # Frame for the Comment
        self.comment_frame.grid(row=2, column=0, padx=(20, 10), pady=10, sticky="nsew")

        # Comment field
        self.comment.insert(0, "Введите комментарий к заказу")
        self.comment.grid(row=0, column=0, padx=5, pady=(0, 10), sticky="ew")

        # Create a Frame for input widgets
        self.widgets_frame.grid(
            row=0, column=1, padx=10, pady=(30, 10), sticky="nsew", rowspan=1
        )
        self.widgets_frame.columnconfigure(index=0, weight=1)

        # Item_menu
        self.item_menu.grid(row=0, column=0, padx=5, pady=10, sticky="nsew")

        # Spinbox
        self.spinbox.insert(0, "0", )
        self.spinbox.grid(row=0, column=1, padx=5, pady=10, sticky="ew")

        # Buttons
        self.addToOrder_button.grid(row=1, column=0, padx=5, pady=10, sticky="nsew")
        self.addToCart_button.grid(row=0, column=0, padx=5, pady=10, sticky="nsew")

        # Switch
        self.switch.grid(row=2, column=0, padx=5, pady=10, sticky="nsew")

        # Panedwindow
        self.paned.grid(row=0, column=2, pady=(25, 5), sticky="nsew", rowspan=3)
        self.paned_1.grid(row=1, column=0, pady=(25, 5), sticky="nsew", rowspan=3)

        # Panes
        self.paned.add(self.pane_order, weight=1)

        # Scrollbars
        self.scrollbarOrder.pack(side="right", fill="y")

        # TreeOrder
        self.tree.pack(expand=True, fill="both")
        self.scrollbarOrder.config(command=self.tree.yview)

        self.tree.column("#0", anchor="w", width=120)
        self.tree.column(1, anchor="w", width=120)
        self.tree.column(2, anchor="w", width=120)
        self.tree.column(3, anchor="w", width=120)

        # TreeviewOrder headings
        self.tree.heading("#0", text="item", anchor="center")
        self.tree.heading(1, text="price per piece", anchor="center")
        self.tree.heading(2, text="count", anchor="center")
        self.tree.heading(3, text="total price", anchor="center")
