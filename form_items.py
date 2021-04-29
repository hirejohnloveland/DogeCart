import tkinter as tk
import shopping_cart

# This module is responsible for the rows and buttons and textboxes that the GUI must display, as well as the callback
# of the buttons and the refreshing of the form.  Notably, the buttons on the total_row do not have callback here, but are
# bound to an event listenier in the tkGUI_main_window instead, as these buttons trigger global events in the app that must
# be passed down to all the modules.


class Header():
    # Genearte the Header row with labels
    def __init__(self, root, row_number):
        self.root = root
        self.row_number = row_number
        self.remove_items_label = self.make_remove_items_label()
        self.add_items_label = self.make_add_items_label()
        self.qty_label = self.make_qty_label()
        self.price_label = self.make_price_label()
        self.subtotal_label = self.make_subtotal_label()

    def make_remove_items_label(self):
        label = tk.Label(self.root, text="Remove Items", fg='black', bg='light green',
                         height=1, width=10)
        label.grid(row=self.row_number, column=0)
        return label

    def make_add_items_label(self):
        label = tk.Label(self.root, text="Add Items", fg='black', bg='light green',
                         height=1, width=10)
        label.grid(row=self.row_number, column=2)
        return label

    def make_qty_label(self):
        label = tk.Label(self.root, text="Qty.", fg='black', bg='light green',
                         height=1, width=10)
        label.grid(row=self.row_number, column=4)
        return label

    def make_price_label(self):
        label = tk.Label(self.root, text="Price", fg='black', bg='light green',
                         height=1, width=10)
        label.grid(row=self.row_number, column=5)

    def make_subtotal_label(self):
        label = tk.Label(self.root, text="Subtotal", fg='black', bg='light green',
                         height=1, width=10)
        label.grid(row=self.row_number, column=6)


class Row_Items():
    def __init__(self, root, row_number, total_row, cart, dict_key):
        self.root = root
        self.row_number = row_number
        self.total_row = total_row
        self.cart = cart
        self.dict_key = dict_key
        self.remove_button = self.make_remove_button()
        self.label = self.make_label()
        self.add_button = self.make_add_button()
        self.qty_box = self.make_qty_box()
        self.pr_box = self.make_pr_box()
        self.sbtl_box = self.make_sbtl_box()

    def make_remove_button(self):
        button = tk.Button(self.root, text="-", fg='black', bg='red', command=lambda: self.remove_onclick(),
                           height=1, width=7)
        button.grid(row=self.row_number, column=0)
        return button

    def make_label(self):
        label = tk.Label(self.root, text=self.dict_key, fg='black', bg='red',
                         height=1, width=8)
        label.grid(row=self.row_number, column=1)
        return label

    def make_add_button(self):
        button = tk.Button(self.root, text="+", fg='black', bg='red', command=lambda: self.add_onclick(),
                           height=1, width=7)
        button.grid(row=self.row_number, column=2)
        return button

    def make_qty_box(self):
        box = tk.Text(self.root, height=1, width=4)
        box.grid(row=self.row_number, column=4)
        box.insert("1.0", self.cart.get_qty(self.dict_key))
        box['state'] = tk.DISABLED
        return box

    def make_pr_box(self):
        box = tk.Text(self.root, height=1, width=5)
        box.grid(row=self.row_number, column=5)
        box.insert("1.0", self.cart.get_pr(self.dict_key))
        box['state'] = tk.DISABLED
        return box

    def make_sbtl_box(self):
        box = tk.Text(self.root, height=1, width=6)
        box.grid(row=self.row_number, column=6)
        box.insert("1.0", self.cart.item_total(self.dict_key))
        box.tag_add("all", "1.0", tk.END)
        box.tag_configure("all", justify="right")
        box['state'] = tk.DISABLED
        return box

    ####### Functions for the button click events and refreshing the form after items are added / removed #######

    def add_onclick(self):
        """Add selected item to the cart then refresh form"""
        self.cart.add_item(self.dict_key)
        self.row_items_refresh()

    def remove_onclick(self):
        """Remove selected from the cart then refresh form"""
        self.cart.remove_item(self.dict_key)
        self.row_items_refresh()

    def row_items_refresh(self):
        """Refresh the text boxes on this row and also the total row"""
        self.qty_box_refresh()
        self.pr_box_refresh()
        self.sbtl_box_refresh()
        self.total_row.total_row_refresh()

    def qty_box_refresh(self):
        self.qty_box['state'] = tk.NORMAL
        self.qty_box.delete("1.0", tk.END)
        self.qty_box.insert("1.0", self.cart.get_qty(self.dict_key))
        self.qty_box['state'] = tk.DISABLED

    def pr_box_refresh(self):
        self.pr_box['state'] = tk.NORMAL
        self.pr_box.delete("1.0", tk.END)
        self.pr_box.insert("1.0", self.cart.get_pr(self.dict_key))
        self.pr_box['state'] = tk.DISABLED

    def sbtl_box_refresh(self):

        self.sbtl_box["state"] = tk.NORMAL
        self.sbtl_box.delete("1.0", tk.END)
        self.sbtl_box.insert("1.0", self.cart.item_total(self.dict_key))
        self.sbtl_box.tag_add("all", "1.0", tk.END)
        self.sbtl_box.tag_configure("all", justify="right")
        self.sbtl_box['state'] = tk.DISABLED


class Total_Row():
    def __init__(self, root, row_number, cart):
        self.root = root
        self.row_number = row_number
        self.cart = cart
        self.clear_cart_button = self.make_clear_cart_button()
        self.save_and_close_button = self.make_save_and_close_button()
        self.checkout_button = self.make_checkout_button()
        self.total_label = self.make_total_label()
        self.total_box = self.make_total_box()

    def make_clear_cart_button(self):
        """Clear all the items out of the shopping cart, set all quantities to zero and redraw main form"""
        # this button is bound in tkGUI_main_window, the lack of a callback
        # method here
        button = tk.Button(self.root, text='Clear Cart', fg='black', bg='red',
                           height=2, width=9)
        button.grid(row=self.row_number, column=0)
        return button

    def make_save_and_close_button(self):
        """Saves the cart to a JSON file and then closes the program"""
        # this button is bound in tkGUI_main_window, note the lack of a callback
        # method here
        button = tk.Button(self.root, text='Save and close', fg='black', bg='red',
                           height=2, width=9, wraplength=60)
        button.grid(row=self.row_number, column=1)
        return button

    def make_checkout_button(self):
        """Destroys the root tk window which clears the cart and closes the program"""
        # this button is bound in tkGUI_main_window, note the lack of a callback method here
        button = tk.Button(self.root, text='Checkout (Quit)', fg='black', bg='red',
                           height=2, width=9, wraplength=80)
        button.grid(row=self.row_number, column=2)
        return button

    def make_total_label(self):
        label = tk.Label(self.root, text="Total", fg='black', bg='light green',
                         height=1, width=7)
        label.grid(row=self.row_number, column=5)
        return label

    def make_total_box(self):
        total_box = tk.Text(self.root, height=1, width=7)
        total_box.grid(row=self.row_number, column=6)
        total_box.insert("1.0", self.cart.get_total())
        total_box.tag_add("all1", "1.0", tk.END)
        total_box.tag_configure("all1", justify="right")
        total_box['state'] = tk.DISABLED
        return total_box

    def total_row_refresh(self):
        self.total_box["state"] = tk.NORMAL
        self.total_box.delete("1.0", tk.END)
        self.total_box.insert("1.0", self.cart.get_total())
        self.total_box.tag_add("all1", "1.0", tk.END)
        self.total_box.tag_configure("all1", justify="right")
        self.total_box["state"] = tk.DISABLED
