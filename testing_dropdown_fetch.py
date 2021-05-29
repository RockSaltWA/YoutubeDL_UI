from tkinter import *

root = Tk()
root.title("Title")
root.geometry("400x400")

def selected():
    myLabel = Label(root, text = dropdown_variable1.get()).grid(row=4)

options = [
    "mp4",
    "mp3",
    "png"
]
dropdown_variable1 = StringVar()
dropdown_variable1.set(options[0])

dropdown_filetype = OptionMenu(root, dropdown_variable1, *options)
dropdown_filetype.grid(row=2, column=2)

myButton = Button(root, text="Select", command = selected).grid(row=3)

root.mainloop()