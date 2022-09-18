from tkinter import *
root = Tk()

root.title("Tkinter the thinker !")

## first, find a website to download icons ( iconarchive.com )
## second, download the icons as ICO FILE ( apple.ico )
## third, in the codes, type --> root.iconbitmap("apple.ico")  

root.iconbitmap("rocket.ico")

root.geometry("400x400")

my_label = Label(root, text = "Hello there internet !" ).pack()
my_label2 = Label(root, text= "How are you dude ?").pack()


root.mainloop()
