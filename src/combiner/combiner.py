from PIL import Image, ImageOps

def combine_image (bg,fg,coordinate = (0,0),resize_fg= None) :
    if type(bg) is str :
        bg= Image.open(bg)
    if type(fg) is str:
        fg= Image.open(fg)
        
    if resize_fg != None :
        fg = ImageOps.contain (fg, resize_fg)

    # grab the size of both image
    w_bg, h_bg = bg.size
    w_fg, h_fg = fg.size

    #calculate center position
    center_w = int(w_bg/2) - int(w_fg/2)
    center_h =int(h_bg/2) - int (h_fg/2)

    coordinate = (center_w + coordinate[0], center_h + coordinate[1] )
    bg.paste (fg, 
                  box=coordinate,
                   mask = fg)
    return bg