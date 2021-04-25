from tkinter import *


class Panel:
    def __init__(self, root, frame):
        self.root = root
        self.frame = frame

        self.btnFrame = Frame(self.frame, width=1000,
                              height=1000, borderwidth=1)
        self.btnFrame.grid(row=1, column=0, padx=10, pady=2)

        self.colorLog = Text(self.frame, width=30, height=10, takefocus=0)
        self.colorLog.grid(row=3, column=0, padx=10, pady=2)
