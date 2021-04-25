import dictionary_data
from tkinter import *


# Driver code
if __name__ == "__main__":
    # create a GUI window
    gui = Tk()

    # set the background colour of GUI window
    gui.configure(background="light green")

    # set the title of GUI window
    gui.title("Shopping Cart")

    # set the configuration of GUI window
    gui.geometry("500x300")


    
    


    #Function to refresh each section when items are added or removed#
    def refresher (command, key, qty, pr, subt):
        if command == "Remove":
            dictionary_data.remove_item(key)
        elif command == "Add":
            dictionary_data.add_item(key)
        else:
            pass

        qty["state"] = NORMAL
        qty.delete("1.0", END)
        qty.insert("1.0", dictionary_data.get_qty(key))
        qty['state'] = DISABLED

        pr["state"] = NORMAL
        pr.delete("1.0", END)
        pr.insert("1.0", dictionary_data.get_pr(key))
        pr['state'] = DISABLED

        subt["state"] = NORMAL
        subt.delete("1.0",END)
        subt.insert("1.0", dictionary_data.item_total(key))
        subt.tag_add("all", "1.0", END)
        subt.tag_configure("all", justify="right")
        subt['state'] = DISABLED

        total_box["state"] = NORMAL
        total_box.delete("1.0", END)
        total_box.insert("1.0", dictionary_data.get_total())
        total_box.tag_add("all1", "1.0", END)
        total_box.tag_configure("all1", justify="right")
        total_box["state"] = DISABLED

    def destroy_cart():
        dictionary_data.clear_cart()
        refresher("","Onions", qty1, pr1, subt1)
        refresher("","Tomatoes", qty2, pr2, subt2)
        refresher("","Eggs", qty3, pr3, subt3)
        refresher("","Ice Cream", qty4, pr4, subt4)



    # Column Headings #
    tlabel1 = Label(gui, text="Remove Items", fg='black', bg='light green',
                    height=1, width=10)
    tlabel1.grid(row=1, column=0)

    tlabel2 = Label(gui, text="Add Items", fg='black', bg='light green',
                    height=1, width=10)
    tlabel2.grid(row=1, column=2)

    tlabel3 = Label(gui, text="Qty.", fg='black', bg='light green',
                    height=1, width=10)
    tlabel3.grid(row=1, column=4)

    tlabel4 = Label(gui, text="Price", fg='black', bg='light green',
                    height=1, width=10)
    tlabel4.grid(row=1, column=5)

    tlabel5 = Label(gui, text="Subtotal", fg='black', bg='light green',
                    height=1, width=10)
    tlabel5.grid(row=1, column=6)





    # Onion Section / Buttons
    button1 = Button(gui, text="-", fg='black', bg='red',
                    command=lambda: refresher("Remove","Onions",qty1,pr1,subt1), height=1, width=7)
    button1.grid(row=4, column=0)

    label1 = Label(gui, text="Onions", fg='black', bg='red',
                    height=1, width=8)
    label1.grid(row=4, column=1)

    button3 = Button(gui, text="+", fg='black', bg='red',
                    command=lambda: refresher("Add","Onions",qty1,pr1,subt1), height=1, width=7)
    button3.grid(row=4, column=2)
    
    #Onion (qty)
    qty1 = Text(gui, height=1, width=4)
    qty1.grid(row=4, column =4)
    qty1.insert("1.0", dictionary_data.get_qty("Onions"))
    qty1['state'] = DISABLED
    

    #Onion (pr)
    pr1 = Text(gui, height=1, width=5)
    pr1.grid(row=4, column =5)
    pr1.insert("1.0", dictionary_data.get_pr("Onions"))
    pr1['state'] = DISABLED

    #Onion (subt)
    subt1 = Text(gui, height=1, width=6)
    subt1.grid(row=4, column =6)
    subt1.insert("1.0", dictionary_data.item_total("Onions"))
    subt1.tag_add("all", "1.0", END)
    subt1.tag_configure("all", justify="right")
    subt1['state'] = DISABLED


    # Tomato Section
    button4 = Button(gui, text="-", fg='black', bg='red',
                    command=lambda: refresher("Remove","Tomatoes",qty2,pr2,subt2), height=1, width=7)
    button4.grid(row=5, column=0)

    label2 = Label(gui, text="Tomatoes", fg='black', bg='red',
                    height=1, width=8)
    label2.grid(row=5, column=1)

    button6 = Button(gui, text="+", fg='black', bg='red',
                    command=lambda: refresher("Add","Tomatoes",qty2,pr2,subt2), height=1, width=7)
    button6.grid(row=5, column=2)

    #Tomatoes (qty)
    qty2 = Text(gui, height=1, width=4)
    qty2.grid(row=5, column =4)
    qty2.insert("1.0", dictionary_data.get_qty("Tomatoes"))
    qty2['state'] = DISABLED
    

    #Tomatoes (pr)
    pr2 = Text(gui, height=1, width=5)
    pr2.grid(row=5, column =5)
    pr2.insert("1.0", dictionary_data.get_pr("Tomatoes"))
    pr2['state'] = DISABLED

    #Tomatoes (subt)
    subt2 = Text(gui, height=1, width=6)
    subt2.grid(row=5, column =6)
    subt2.insert("1.0", dictionary_data.item_total("Tomatoes"))
    subt2.tag_add("all", "1.0", END)
    subt2.tag_configure("all", justify="right")
    subt2['state'] = DISABLED




    # Egg Section
    button7 = Button(gui, text="-", fg='black', bg='red',
                    command=lambda: refresher("Remove","Eggs",qty3,pr3,subt3), height=1, width=7)
    button7.grid(row=6, column=0)

    label3 = Label(gui, text="Eggs", fg='black', bg='red',
                    height=1, width=8)
    label3.grid(row=6, column=1)

    button9 = Button(gui, text="+", fg='black', bg='red',
                    command=lambda: refresher("Add","Eggs",qty3,pr3,subt3), height=1, width=7)
    button9.grid(row=6, column=2)

    #Eggs (qty)
    qty3 = Text(gui, height=1, width=4)
    qty3.grid(row=6, column =4)
    qty3.insert("1.0", dictionary_data.get_qty("Eggs"))
    qty3['state'] = DISABLED
    

    #Eggs (pr)
    pr3 = Text(gui, height=1, width=5)
    pr3.grid(row=6, column =5)
    pr3.insert("1.0", dictionary_data.get_pr("Eggs"))
    pr3['state'] = DISABLED

    #Eggs (subt)
    subt3 = Text(gui, height=1, width=6)
    subt3.grid(row=6, column =6)
    subt3.insert("1.0", dictionary_data.item_total("Eggs"))
    subt3.tag_add("all", "1.0", END)
    subt3.tag_configure("all", justify="right")
    subt3['state'] = DISABLED



    # Ice Cream Section
    button0 = Button(gui, text="-", fg='black', bg='red',
                    command=lambda: refresher("Remove","Ice Cream",qty4,pr4,subt4), height=1, width=7)
    button0.grid(row=7, column=0)

    label4 = Label(gui, text="Ice Cream", fg='black', bg='red',
                height=1, width=8)
    label4.grid(row=7, column=1)
    button11 = Button(gui, text="+", fg='black', bg='red',
                command=lambda: refresher("Add","Ice Cream",qty4,pr4,subt4), height=1, width=7)
    button11.grid(row=7, column=2)

    #Ice Cream (qty)
    qty4 = Text(gui, height=1, width=4)
    qty4.grid(row=7, column =4)
    qty4.insert("1.0", dictionary_data.get_qty("Ice Cream"))
    qty4['state'] = DISABLED
    

    #Ice Cream (pr)
    pr4 = Text(gui, height=1, width=5)
    pr4.grid(row=7, column =5)
    pr4.insert("1.0", dictionary_data.get_pr("Ice Cream"))
    pr4['state'] = DISABLED

    #Ice Cream (subt)
    subt4 = Text(gui, height=1, width=6)
    subt4.grid(row=7, column =6)
    subt4.insert("1.0", dictionary_data.item_total("Ice Cream"))
    subt4.tag_add("all", "1.0", END)
    subt4.tag_configure("all", justify="right")
    subt4['state'] = DISABLED




    # Checkout / Clear Items Buttons 
    Decimal= Button(gui, text='Clear Cart', fg='black', bg='red',
                    command=lambda: destroy_cart(), height=2, width=9)
    Decimal.grid(row=8, column=0)

    Decimal= Button(gui, text='Checkout (Quit)', fg='black', bg='red',
                    command=lambda: gui.destroy(), height=2, width=9, wraplength=80)
    Decimal.grid(row=8, column=2)



    # Total Section
    label6 = Label(gui, text="Total", fg='black', bg='light green',
                height=1, width=7)
    label6.grid(row=8, column=5)

    total_box = Text(gui, height=1, width=7)
    total_box.grid(row=8, column =6)
    total_box.insert("1.0", dictionary_data.get_total())
    total_box.tag_add("all1", "1.0", END)
    total_box.tag_configure("all1", justify="right")
    total_box['state'] = DISABLED


    

    
    gui.mainloop()
