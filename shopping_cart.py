import json
# import os.path
from os import path


class ShoppingCart():
    def __init__(self):
        # Pricelist needs to move to it's own class, then added to the shopping cart class as an attribute.
        # Upload / update via CSV so administrative personel can update the pricelist without needed to know Python.
        self.dict_prices = {
            "Onions": .50,
            "Tomatoes": .99,
            "Eggs": 2.99,
            "Ice Cream": 4.99
        }
        # This needs to save to a JSON file.  BUT, the ditcionary needs to be initialized from the price list,
        # then quantity checked against the JSON file.  Otherwise, a mismatch could occur where new items are in the
        # price list but don't exist in the quantity dictionary and therefore will display but will not be able to
        # be added to the cart
        self.dict_quant = {
            "Onions": 0,
            "Tomatoes": 0,
            "Eggs": 0,
            "Ice Cream": 0
        }
        self.restore()

    def add_item(self, key):
        """Adds qty 1 of item (key) to the cart"""
        self.dict_quant[key] += 1

    def remove_item(self, key):
        """Removes qty 1 of item (key) to the cart"""
        if self.dict_quant[key] == 0:
            return
        else:
            self.dict_quant[key] -= 1

    def clear_cart(self):
        """Empties all items in the cart"""
        for keys in self.dict_quant.keys():
            self.dict_quant[keys] = 0

    def get_qty(self, key):
        """Returns the quantity of an item (key) in the cart"""
        return self.dict_quant[key]

    def get_pr(self, key):
        """Returns the unit price of and item (key) in the pricelist as a formatted string"""
        return '${:,.2f}'.format(self.dict_prices[key])

    def item_total(self, key):
        """Returns the total sales (qty * pr) for an individual item (key) in the cart as a formatted string"""
        return '${:,.2f}'.format(self.dict_prices[key] * self.dict_quant[key])

    def subtotal(self):
        """Returs a dictionary of all of the items and their totals"""
        dict_subtotal = {}
        for k, v in self.dict_prices.items():
            dict_subtotal[k] = v * self.dict_quant[k]
        return dict_subtotal

    def get_total(self):
        """Returns the total value of the shopping cart as a formatted string"""
        total = 0
        subtotals = self.subtotal()
        for values in subtotals.values():
            total += values
        return '${:,.2f}'.format(total)

    def restore(self):
        if path.isfile("my_cart.json"):
            with open("my_cart.json", "r") as save_file:
                data = json.load(save_file)
                self.dict_quant = data
            pass

    def save(self):
        with open("my_cart.json", "w") as save_file:
            json.dump(self.dict_quant, save_file)
