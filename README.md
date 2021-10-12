# DogeCart - TO THE MOON!

DogeCart was my first forray into the TKinter GUI framework.  It is an object oriented shopping cart program with a Doge themed GUI.  It consists of the following elements:

1. Data Files - 

a. pricelist.csv is a .csv file where a non-programmer can add or remove products and adjust their prices.
 
b. my_cart.json is the storage file which tracks the users cart for data persistance.
 
2. Modules

a. main - entry point
  
b. tkGUI_main_window - GUI event loop and global event listeners
  
c. form_items - classes for displaying the data on the gui and handling events
  
d. shopping_cart - respoonsible for the mechanics of the shopping cart (adds, deletes, checkout, etc.)
  
e. data_manager - storage and I / O with data files
