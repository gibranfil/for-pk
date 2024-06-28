from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 
import textwrap

def generate_text(image, message, font, fontColor, offset = (0,0), font_size = 36):
    if type(image) is str :
        image= Image.open(image)
        
    W, H = image.size
    draw = ImageDraw.Draw(image)
    myFont = ImageFont.truetype(font, font_size)

    para = textwrap.wrap (message, width=16)
    
    current_h, pad = H/5, 10
    if len (para) > 1 :
        current_h = 10
    for line in para:

        w, h = draw.textsize(line, font=myFont)
        draw.text(((W - w) / 2 + offset[0] , current_h + offset[1]), line, font=myFont)
        current_h += h + pad
    return image



def generate_text2(image, message, font, fontColor, offset = (0,0), font_size = 36):
    if type(image) is str :
        image= Image.open(image)
        
    W, H = image.size
    para = textwrap.wrap (message, width=16)

    if len (para) > 1 :
        
        current_h = 0
        font_size = font_size-20

    draw = ImageDraw.Draw(image)
    myFont = ImageFont.truetype(font, font_size)

    
    print (len(para))
    current_h, pad = 0, -1

    for line in para:

        w, h = draw.textsize(line, font=myFont)
        draw.text(((W - w) / 2 + offset[0] , current_h + offset[1]), line, font=myFont)
        current_h += h + pad
    return image
