import tkinter
from buttonClick import buttonclick
from buttonClick import buttons


def startGUI():
    root = tkinter.Tk()
    root.title("Connect Four")
    titleLab = tkinter.Label(root, text="Welcome to Connect Four")
    titleLab.grid(row=1, column=0)
    shapeLab = tkinter.Label(root, text="You are X")
    shapeLab.grid(row=2, column=0)

    rightFrame = tkinter.Frame(root)
    rightFrame.grid(row=2, column=0, sticky='n')

    for r in range(6):
        for c in range(7):
            button = tkinter.Button(rightFrame, text=" ", padx=30, pady=30)
            button.grid(row=6 - r, column=c)
            buttons[5 - r].append(button)
    for c in range(7):
        button = tkinter.Button(rightFrame, text=" ", padx=30, pady=30, background='blue',
                                command=lambda num=c: buttonclick(num))
        button.grid(row=0, column=c)

    root.mainloop()
