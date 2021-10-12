# DogeCart - TO THE MOON!

DogeCart was my first forray into the TKinter GUI framework.  It is an object oriented shopping cart program with a Doge themed GUI.  It consists of the following elements:

Data Files - 

pricelist.csv - .csv file where a non-programmer can add or remove products and adjust their prices.
 
my_cart.json - storage file which tracks the users cart for data persistance.
 
Modules

main - entry point
  
tkGUI_main_window - GUI event loop and global event listeners
  
form_items - classes for displaying the data on the gui and handling events
  
shopping_cart - respoonsible for the mechanics of the shopping cart (adds, deletes, checkout, etc.)
  
data_manager - storage and I / O with data files
