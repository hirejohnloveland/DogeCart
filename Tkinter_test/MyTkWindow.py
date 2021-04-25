from tkinter import *
from Panel import *
from Form_Items import *
from Buttons import *


class MyTkWindow:
    def __init__(self):

        self.root = Tk()  # Makes the window
        # Makes the title that will appear in the top left
        self.root.wm_title("Window Title")
        self.root.config(background="light green")

        self.rightFrame = Frame(self.root, width=700, height=500)
        self.rightFrame.grid(row=0, column=10, padx=10, pady=2)

        self.rightPanel = Panel(self.root, self.rightFrame)

        def GenButtons(button_dict):
            buttons = {}
            for k, v in items_dict.items():
                buttons[f"btn{k}"] = ColorButton(
                    self.rightPanel.btnFrame, v, print(self))
            return buttons

        buttons = GenButtons(items_dict)
        print(buttons["btn2"])
        buttons["btn2"].destroy_button()

        # redBtn = ColorButton(self.rightPanel.btnFrame, "red",
        #                      "")
        # yellowBtn = ColorButton(self.rightPanel.btnFrame,
        #                         "yellow", "")
        # greenBtn = ColorButton(self.rightPanel.btnFrame,
        #                        "green", "")

    def start(self):
        self.root.mainloop()  # start monitoring and updating the GUI
