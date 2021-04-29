import data_manager


class ShoppingCart():
    #  This class is responsible for the shopping cart mechanics and the interface between the GUI and the data files.

    def __init__(self):
        self.data_manager = data_manager.Data_Manager()
        self.pricelist = self.data_manager.pricelist
        self.cartlist = self.data_manager.cartlist

    def add_item(self, key):
        """Adds qty 1 of item (key) to the cart"""
        self.cartlist[key] += 1

    def remove_item(self, key):
        """Removes qty 1 of item (key) to the cart"""
        if self.cartlist[key] == 0:
            return
        else:
            self.cartlist[key] -= 1

    def clear_cart(self):
        """Empties all items in the cart"""
        for keys in self.cartlist.keys():
            self.cartlist[keys] = 0

    def get_qty(self, key):
        """Returns the quantity of an item (key) in the cart"""
        return self.cartlist[key]

    def get_pr(self, key):
        """Returns the unit price of and item (key) in the pricelist as a formatted string"""
        return '${:,.2f}'.format(self.pricelist[key])

    def item_total(self, key):
        """Returns the total sales (qty * pr) for an individual item (key) in the cart as a formatted string"""
        return '${:,.2f}'.format(self.pricelist[key] * self.cartlist[key])

    def subtotal(self):
        """Returs a dictionary of all of the items and their totals"""
        dict_subtotal = {}
        for k, v in self.pricelist.items():
            dict_subtotal[k] = v * self.cartlist[k]
        return dict_subtotal

    def get_total(self):
        """Returns the total value of the shopping cart as a formatted string"""
        total = 0
        subtotals = self.subtotal()
        for values in subtotals.values():
            total += values
        return '${:,.2f}'.format(total)

    def save(self):
        """saves the shopping cart on exit"""
        self.data_manager.save_current_cart()
