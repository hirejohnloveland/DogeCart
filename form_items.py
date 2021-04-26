import tkinter as tk
import shopping_cart
# Currently attempting to test refresh after callback with a call to the main_window and a refresher function located there.
# This seems like a workable first implementation, but objects in the classes below shoould be decoupled from the interface.
# Ultimately, I need the refresher function to be in the main window, activated by an event listener that listens for the click
# events on the buttons below and then exectues refresh functions on each text box.


class Row_Items():
    # Generate the Row_Items class, which in turn generates all of it's necessary objects via it's class constructor.
    def __init__(self, tkwindow, row_number, cart, dict_key):
        self.gui = tkwindow
        self.row_number = row_number
        self.cart = cart
        self.dict_key = dict_key
        self.parent_row = self
        self.remove_button = Remove_Button(self.gui, self.row_number,
                                           self.cart, self.dict_key)
        # self.label = Row_Label(self.gui, self.row_number,
        #                        self.cart, self.dict_key)
        self.label = self.make_label()
        self.add_button = Add_Button(self.gui, self.row_number,
                                     self.cart, self.dict_key, self.parent_row)
        self.qty_box = Qty_Box(self.gui, self.row_number,
                               self.cart, self.dict_key)
        self.pr_box = Pr_Box(self.gui, self.row_number,
                             self.cart, self.dict_key)
        self.sbtl_box = Sbtl_Box(self.gui, self.row_number,
                                 self.cart, self.dict_key)

    def make_label(self):
        label = tk.Label(self.gui, text=self.dict_key, fg='black', bg='red',
                         height=1, width=8)
        label.grid(row=self.row_number, column=1)
        return label

    def Row_Items_refresh(self):
        self.qty_box.qty_box_refresh()
        self.pr_box.pr_box_refresh()
        self.sbtl_box.sbtl_box_refresh()


class Remove_Button():
    def __init__(self, gui, row_number, cart, dict_key):
        self.gui = gui
        self.row_number = row_number
        self.cart = cart
        self.dict_key = dict_key
        self.button = tk.Button(self.gui, text="-", fg='black', bg='red',
                                height=1, width=7)
        self.button.grid(row=self.row_number, column=0)


class Row_Label():
    def __init__(self, gui, row_number, cart, dict_key):
        self.gui = gui
        self.row_number = row_number
        self.cart = cart
        self.dict_key = dict_key
        # self.label = tk.Label(self.gui, text=self.dict_key, fg='black', bg='red',
        #                       height=1, width=8)
        # self.label.grid(row=self.row_number, column=1)


class Add_Button():
    def __init__(self, gui, row_number, cart, dict_key, parent):
        self.gui = gui
        self.row_number = row_number
        self.cart = cart
        self.dict_key = dict_key
        self.parent = parent
        self.button = tk.Button(self.gui, text="+", fg='black', bg='red', command=lambda: self.add_action(),
                                height=1, width=7)
        self.button.grid(row=self.row_number, column=2)

    def add_action(self):
        self.cart.add_item(self.dict_key)
        self.parent.Row_Items_refresh()
        # def add_action(self):
        #     # add item
        #     # parent.row_items.refresh()
        # self.parent.refresh


class Qty_Box():

    def __init__(self, gui, row_number, cart, dict_key):
        self.gui = gui
        self.row_number = row_number
        self.cart = cart
        self.dict_key = dict_key
        self.box = tk.Text(self.gui, height=1, width=4)
        self.box.grid(row=self.row_number, column=4)
        self.box.insert("1.0", self.cart.get_qty(self.dict_key))
        self.box['state'] = tk.DISABLED

    def qty_box_refresh(self):
        self.box['state'] = tk.NORMAL
        self.box.delete("1.0", tk.END)
        self.box.insert("1.0", self.cart.get_qty(self.dict_key))
        self.box['state'] = tk.DISABLED


class Pr_Box():
    def __init__(self, gui, row_number, cart, dict_key):
        self.gui = gui
        self.row_number = row_number
        self.cart = cart
        self.dict_key = dict_key
        self.box = tk.Text(self.gui, height=1, width=5)
        self.box.grid(row=self.row_number, column=5)
        self.box.insert("1.0", self.cart.get_pr(self.dict_key))
        self.box['state'] = tk.DISABLED

    def pr_box_refresh(self):
        self.box['state'] = tk.NORMAL
        self.box.delete("1.0", tk.END)
        self.box.insert("1.0", self.cart.get_pr(self.dict_key))
        self.box['state'] = tk.DISABLED


class Sbtl_Box():
    def __init__(self, gui, row_number, cart, dict_key):
        self.gui = gui
        self.row_number = row_number
        self.cart = cart
        self.dict_key = dict_key
        self.box = tk.Text(self.gui, height=1, width=6)
        self.box.grid(row=self.row_number, column=6)
        self.box.insert("1.0", self.cart.item_total(self.dict_key))
        self.box.tag_add("all", "1.0", tk.END)
        self.box.tag_configure("all", justify="right")
        self.box['state'] = tk.DISABLED

    def sbtl_box_refresh(self):

        self.box["state"] = tk.NORMAL
        self.box.delete("1.0", tk.END)
        self.box.insert("1.0", self.cart.item_total(self.dict_key))
        self.box.tag_add("all", "1.0", tk.END)
        self.box.tag_configure("all", justify="right")
        self.box['state'] = tk.DISABLED
