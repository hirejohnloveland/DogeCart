import tkinter as tk
import PyPDF2
from PIL import Image, ImageTk
import shopping_cart
import form_items


def generate_row_items(rows):
    """Generates a dynamic number of rows with buttons and boxes to match the number of items in the price list dictionary."""
    index = 1
    for key in my_cart.dict_prices.keys():
        rows[index] = form_items.Row_Items(root, index, my_cart, key)
        index += 1


def refresh_row_items(command, key):
    "Refreshes the rows once the bound buttons are clicked"
    if command == "Remove":
        my_cart.remove_item(key)
    elif command == "Add":
        my_cart.add_item(key)
    else:
        pass
    for row in rows.keys():
        rows[row].Row_Items_refresh()


# Start of Window
root = tk.Tk()

canvas = tk.Canvas(root, width=900, height=400)
canvas.grid(columnspan=10)

my_cart = shopping_cart.ShoppingCart()

# Generate rows and associated objects
rows = {}
generate_row_items(rows)


# End of Window
root.mainloop()


##########################################################
################ Enabling Functions ######################
##########################################################
