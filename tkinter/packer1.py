#!evn01/Scripts/python3.
from tkinter import *

if __name__ == "__main__":
    window = Tk()
    window.title("Pack-Example1")
    mainFrame = Frame(window, borderwidth=2, relief=GROOVE)
    Button(mainFrame, text='Left', padx=10, pady=10).pack(side=LEFT, padx=10, pady=10)
    Button(mainFrame, text='This is the Center button', padx=10, pady=10).pack(side=LEFT, padx=10, pady=10)
    Button(mainFrame, text='Right', padx=10, pady=10).pack(side=LEFT, padx=10, pady=10)
    mainFrame.pack(padx=20, pady=20)
    window.mainloop()