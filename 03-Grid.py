from tkinter import *
root = Tk()

root.title("Tkinter The Thinker !")
root.geometry("400x400")

my_label = Label(root, text = "My new GUI app !" ).grid(row = 0, column = 1)
my_label2 = Label(root, text = "The line two ?" ) ## .grid(row = 1, column = 2)

## my_label.grid(row = 0, column = 1)
my_label2.grid(row = 1, column = 2)


root.mainloop()