# -------------------------------------------------------------CORE-------------------------------------------------------------
from PIL import ImageDraw, ImageFont, Image
import PIL
from tkinter import *

#create an image object
def image_processing(image_file):
    image = PIL.Image.open(image_file)
    watermarked_image= image.copy()
    return watermarked_image


def watermark_text(watermarked_image,position,text):

    #watermark text needs input
    pen= ImageDraw.Draw(watermarked_image)

    text=str(text)
    font= ImageFont.truetype(
        font=r'C:\Users\Dell\Downloads\Source_Sans_Pro\SourceSansPro-BoldItalic.ttf',
        size=50
    )

    #define default LOCATION of watermark (bottom right corner)
    width, height= watermarked_image.size
    textwidth, textheight = pen.textsize(text, font)
    margin = 20
    a = width - textwidth - margin
    b = height - textheight - margin

    # bottom left corner
    c= margin
    d= height - textheight - margin

    #top right corner
    e= width - textwidth - margin
    f= margin

    # top left corner
    g= margin
    h= margin

    if position==1:
        coordinate=(a,b)
    elif position==2:
        coordinate=(c,d)
    elif position==3:
        coordinate=(e,f)
    elif position==4:
        coordinate=(g,h)

    pen.text(coordinate,
             text= text,
             fill='#CDDEFF',
             font=font)

    # watermarked_image.show()
    return watermarked_image




def watermark_img(watermarked_image,position, watermark):
    # image watermark
    size = (500, 100)
    crop_image = watermark
    crop_image.thumbnail(size)


    # define default LOCATION of watermark (bottom right corner)
    width, height = watermarked_image.size
    img_width, img_height= crop_image.size

    margin = 20
    a = width - img_width - margin
    b = height - img_height - margin

    # bottom left corner
    c = margin
    d = height - img_height - margin

    # top right corner
    e = width - img_width - margin
    f = margin

    # top left corner
    g = margin
    h = margin

    if position==1:
        coordinate=(a,b)
    elif position==2:
        coordinate=(c,d)
    elif position==3:
        coordinate=(e,f)
    elif position==4:
        coordinate=(g,h)

    #add watermark
    watermarked_image.paste(crop_image, coordinate)

    # watermarked_image.show()
    return watermarked_image


# fp is also an input from user
# fp=filepath+filename
# watermarked_image.save(fp=r'C:\Users\Dell\Downloads\hoho.png')

