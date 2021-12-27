# --------------------------------------------------------------UI----------------------------------------------------
# importing all files  from tkinter
from tkinter import *
from tkinter import ttk
from io import BytesIO
from tkinter.filedialog import asksaveasfile

import PIL
from PIL import ImageTk

root = Tk()
root.minsize(width=500, height=500)
root.title('Morse Converter')


#canvas
canvas= Canvas(width=500, height=500, highlightthickness=0)
image=PIL.Image.open("Screenshot (214).png")
img = ImageTk.PhotoImage(image)
# displayed_img = PhotoImage('Screenshot (214).png')
image_canvas= canvas.create_image(250, 250, image=img)
big_title= canvas.create_text(250,
                   250,
                    fill="#F5E8C7",
                   font="Courier 35 bold",
                    text="LET'S HAVE YOUR MESSAGE ENCRYPTED.")

canvas.grid(column=0,columnspan=2,row=0)

mainloop()

