from src.combiner.combiner import combine_image
from src.combiner.generate_text import  generate_text, generate_text2
from src.process.folder_helper import glob_data, read_string, create_directories

import os
import glob

input_dir = '/home/gibran/project/image-script/result/image_enchance'
final_path = '/home/gibran/project/image-script/final'

def main () :
    list_data, directory_list = glob_data (input_dir)
    image (input_dir, directory_list)


def image (input_place, directory_list) :
    create_directories (directory_list, final_path)
    font = "/home/gibran/project/image-script/asset/Berkshire_Swash/BerkshireSwash-Regular.ttf"
    color = (0,0,0)

    text_bg = '/home/gibran/project/image-script/asset/namesort.png'
    image_bg = "/home/gibran/project/image-script/asset/nametag2.png"
    box_text_full = "/home/gibran/project/image-script/asset/sizename.png"

    for folder in (directory_list) :
        paths = os.path.join (input_place, folder)
        data_grab = glob.glob (f'{os.path.join (input_place, folder)}/*')
        for image in data_grab :
            filename = os.path.basename (image)
            text = read_string (image)

            ##generate text twibbon
            print (text)
            text_twibon = generate_text (text_bg, text[0],font,color, font_size=55)
            #generate image photo to nameplate
            name_tag = combine_image (image_bg, image, resize_fg=(400,450),coordinate=(0,-300))
            #put text to nameplate
            name_tag = combine_image (name_tag, text_twibon,coordinate=(0,-50))
            #put text to nameplate full
            full = generate_text2 (box_text_full, text[1],font,color, font_size=75)
            name_tag = combine_image (name_tag, full,coordinate=(0,+110))
            path_output = os.path.join (final_path, folder, filename)
            name_tag = name_tag.save (path_output)









if __name__ == "__main__" :
    main ()