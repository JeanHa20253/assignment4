from main import image_processing, watermark_img, watermark_text
import PIL
image_testing= PIL.Image.open('Screenshot (420).png')

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


# #canvas
# canvas = Canvas(width=500, height=500, highlightthickness=0)
# img = ImageTk.PhotoImage(PIL.Image.open('Screenshot (420).png'))
# print(type(img))
# displayed_image = canvas.create_image(250, 250, image=img)
# label= canvas.create_text(250,250, text='minhanh')
# canvas.grid(column=0, columnspan=2, row=0)


#SET UP TEXT WATERMARK INPUT
text=''
label = Label(text="Watermark text: ")
label.grid(column=0 ,row=6)

entry = Entry(width=30)
entry.grid(column=1,row=6)
#Gets text in entry
def get_text():
    global text
    text=entry.get()

save_text= Button(root, text='OK', command=get_text)
save_text.grid(column=2,row=6)


#SET UP IMAGE WATERMARK INPUT
img=''
def get_img_wtm():
    global img
    filename = filedialog.askopenfilename()
    print('Selected Watermark:', filename)
    # image= image_processing(image_file=filename)
    # print(image)
    img = PIL.Image.open(filename)
    img.show()




get_img= Button(root, text='Get Image', command=get_img_wtm)
get_img.grid(column=0,row=7)

#SET UP LOCATION CHOICE FOR USERS
location=''

label = Label(text="Please tick in the position for your watermark")
label.grid(column=0, columnspan=4,row=3)

#Radiobutton
def radio_used():
    global location
    location= radio_state.get()
    print(location)
#Variable to hold on to which radio button value is checked.
radio_state = IntVar()
radiobutton1 = Radiobutton(text="Bottom Right", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Bottom Left", value=2, variable=radio_state, command=radio_used)
radiobutton3 = Radiobutton(text="Top Right", value=3, variable=radio_state, command=radio_used)
radiobutton4 = Radiobutton(text="Top Left", value=4, variable=radio_state, command=radio_used)
radiobutton1.grid(column=0,row=4)
radiobutton2.grid(column=1,row=4)
radiobutton3.grid(column=2,row=4)
radiobutton4.grid(column=3,row=4)








# USER UPLOAD FILE
from tkinter import filedialog

product=''
image=''

def browse_and_open(event=None):
    global product, image
    filename = filedialog.askopenfilename()
    print('Selected:', filename)
    # image= image_processing(image_file=filename)
    # print(image)
    image = PIL.Image.open(filename)
    image.show()



open_button = ttk.Button(root, text='Open', command=browse_and_open)
open_button.grid(column=0,row=0)

#USER HAVE THEIR PICTURE WATERMARKED
def watermarked_txt():
    global image, product

    product = watermark_text(watermarked_image=image, position=location,text= text)
    product.show()

def watermarked_img():
    global image, product
    product = watermark_img(watermarked_image=image,watermark=img,position=location)
    product.show()

txt_watermarked_button= Button(root, text='Text Watermark', command=watermarked_txt)
img_watermarked_button= Button(root, text='Image Watermark', command=watermarked_img)

txt_watermarked_button.grid(column= 0,row=1)
img_watermarked_button.grid(column= 1,row=1)

# #USER DOWNLOAD FILE (PNG) ONTO ANY PLACE THEY WISH

def save_file():
    file = asksaveasfile(mode="wb", title="Save Figure", defaultextension=".png",
                                 filetypes=(("png files", "*.png"), ("all files", "*.*")))
    if file is None:
        return 'hello'

    # img_to_save = open("Screenshot (420).png", "rb").read()
    #CONVERT AN IMAGE OBJECT TO A BYTE-ARRAY TO SAVE INTO USERS' COMPUTER
    global product
    img_byte_arr = BytesIO()
    product.save(img_byte_arr,format='PNG')
    img_to_save = img_byte_arr.getvalue()

    file.write(img_to_save)
    file.close()


save_button = ttk.Button(root, text='Save', command=save_file)
save_button.grid(column=1,row=0)


mainloop()
