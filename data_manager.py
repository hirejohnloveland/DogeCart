import json
from os import path
import csv


class Data_Manager():
    # This class provides the IO / storage for the application and is responsible for serving up the pricelist and the cartlist, which
    # are respectively saved as .csv (for easy administration of the pricelist) and JSON (for the back-end data when the user saves their cart)
    def __init__(self):
        self.pricelist = self.__get_price_list()
        self.saved_cart = self.__load_saved_cart()
        self.cartlist = self.__populate_cart()

    def __get_price_list(self):
        """Load the pricelist from the CSV file"""
        with open('data_files/pricelist.csv', mode='r') as inp:
            reader = csv.reader(inp)
            pricelist = {rows[0]: float(rows[1]) for rows in reader}
        return pricelist

    def __load_saved_cart(self):
        """load the JSON data from the previous saved cart"""
        if path.isfile("data_files/my_cart.json"):
            with open("data_files/my_cart.json", "r") as save_file:
                data = json.load(save_file)
            return data

    def __populate_cart(self):
        """generate an empty cart from the pricelist"""
        # Even though the cart is saved to JSON, it is ALWAYS initialized from the price list.  The reason is that if the
        # price list was changed and we simply loaded the cart from the JSON file without adding the price list items,
        # they would not be able to be added to the cart. Conversely, if items are no longer available on the pricelist,
        # they would otherwise need to be purged from the cart once loaded.
        cart = {}
        for items in self.pricelist.keys():
            cart[items] = 0
        if not self.saved_cart:
            return cart
        else:
            return self.__add_saved_items(cart)

    def __add_saved_items(self, cart):
        """add saved items to the cart, if they exist in the pricelist"""
        for items, quantities in self.saved_cart.items():
            if items in cart:
                cart[items] = quantities
        return cart

    def save_current_cart(self):
        """save the cart as a JSON file"""
        with open("data_files/my_cart.json", "w") as save_file:
            json.dump(self.cartlist, save_file)
