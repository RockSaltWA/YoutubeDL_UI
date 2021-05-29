import tkinter as tk

root = tk.Tk()

img = tk.PhotoImage(file='FunkyLogo.png')

can = tk.Canvas(root, width=300, height=300, bg='lightGrey')
can.grid()

# can.create_rectangle(0, 0, 200, 200, fill='darkGreen')
# can.create_rectangle(100, 100, 300, 300, fill='navy')
# can.create_text(150, 150, text='TKINTER', font=('', 32), fill='orange')
can.create_image(150, 150, image=img)

root.mainloop()