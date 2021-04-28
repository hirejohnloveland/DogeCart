import tkinter as tk
import shopping_cart
import form_items


class GUI():
    def __init__(self, cart):
        self.cart = cart
        self.root = ""  # Placeholder for class level variable that hosts the tkinter window.  This is set by mainloop_launch#
        # assign a rownumber for each row in the price list
        self.rowcount = len(self.cart.dict_prices)

    def mainloop_launch(self):
        """Launch GUI main window."""
        # This is the main even loop of tkinter, it hosts the window and is the gateway for all code to execute.  When the window is
        # destroyed, the loop exits and the program ends.
        self.root = tk.Tk()  # Start of Window
        # Size of the window
        canvas = tk.Canvas(self.root, width=900, height=400)
        canvas.grid(columnspan=10)  # Number of columns on the grid
        self.__draw_form()  # Entry into program###
        self.root.mainloop()  # End of Window

    def __draw_form(self):
        # Generate the header, total, and item rows
        self.__make_header_row(row_number=1)
        total_row = self.__make_total_row(row_number=self.rowcount + 2)
        self.__make_row_items(rows := {}, total_row)
        # Bind the clear cart button to reset the form entirely if clicked
        self.__make_event_listeners(total_row)

    def __make_header_row(self, row_number=1):
        """Generates a header row at row position 1"""
        header_row = form_items.Header(self.root, row_number)

    def __make_row_items(self, rows, total_row):
        """Generates a dynamic number of rows with buttons and boxes to match the number of items in the price list dictionary."""
        index = 2  # This is the first row the data will display on.  2 assumes that there is a header row, otherwise set to 1.
        for key in self.cart.dict_prices.keys():
            rows[index] = form_items.Row_Items(
                self.root, index, total_row, self.cart, key)
            index += 1

    def __make_total_row(self, row_number):
        """Geneartes the last row on the form with totals."""
        # This function MUST be called before the rows are generated with
        # generate_row_items, because the total_row object is passed an argument in order to allow the buttons on each row to see
        # the total row and refresh it's output on callback after items are added or removed to the cart."""
        total_row = form_items.Total_Row(self.root, row_number, self.cart)
        return total_row

    ############################################################################
    ################### Event Listeners and actions ############################
    ############################################################################

    def __make_event_listeners(self, total_row):
        """Defines the click events that the window needs to listen for"""
        # clear the cart and re-draw the form
        total_row.clear_cart_button.bind(
            "<Button>", lambda x: self.__reset_form())
        # Save the cart to a JSON file and end the program
        total_row.save_and_close_button.bind(
            "<Button>", lambda x: self.__exit_save())
        # Clear the cart, save the cart, destroy the window, ends program
        total_row.checkout_button.bind(
            "<Button>", lambda x: self.__checkout())

    def __reset_form(self):
        """Removes all the items from the cart, re-draws all of the items on the form"""
        self.cart.clear_cart()
        self.__draw_form()

    def __checkout(self):
        self.cart.clear_cart()
        self.cart.save()
        self.root.destroy()

    def __exit_save(self):
        self.cart.save()
        self.root.destroy()
