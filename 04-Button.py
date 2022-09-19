from tkinter import *
root = Tk()

root.title("MY BUTTON !")
root.geometry("400x400")

def myClick():
    my_label = Label(root, text = "You clicked the button !", fg="red").pack()

## "fg = foreground" ---> color of the text in the label, button etc. ! fg="red","#3371FF"
## "bg = background" ---> color of the background of the label, button etc. ! bg="red","#3371FF"
## padx ---> padding in x axis (padx=30)
## pady ---> padding in y axis (pady=30)

mybutton = Button(root, text = "click me !", command = myClick, fg="green", bg="#33FFCA", padx=30,pady=30).pack()


root.mainloop()