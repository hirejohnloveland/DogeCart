import shopping_cart
import tkGUI_main_window

cart = shopping_cart.ShoppingCart()

gui = tkGUI_main_window.GUI(cart)
gui.mainloop_launch()
