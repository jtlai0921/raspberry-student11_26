from tkinter import *

if __name__ == '__main__':
    window = Tk()
    window.title('First window')
    runWindow = True
    if runWindow:
        for relief in [RAISED, SUNKEN, FLAT, RIDGE, GROOVE, SOLID]:
            f = Frame(window, borderwidth=2, relief=relief)
            Label(f, text=relief, width=10).pack(side=LEFT)
            f.pack(side=LEFT, padx=5, pady=5)

    window.mainloop()

