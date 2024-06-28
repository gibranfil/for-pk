from src.process.folder_helper import glob_data, create_directories
from src.process.processs_image import remove_bg, crop_image
import glob
import os


input_dir = '/home/gibran/project/image-script/Foto_Nametag'
output_dir = '/home/gibran/project/image-script/result/crop'
removebg_dir = '/home/gibran/project/image-script/result/bg_removed'
enhance_dir = '/home/gibran/project/image-script/result/image_enchance'

def main () :

    list_data, directory_list = glob_data (input_dir)
    crops (input_dir, output_dir, directory_list)
    remove (directory_list,output_dir)
    image_enhance (directory_list, input_place=removebg_dir)
   


def image_enhance (directory_list, input_place) :
    create_directories (directory_list, enhance_dir)
    print (directory_list)
    for folder in (directory_list) :
        print (folder)
        paths = os.path.join (input_place, folder)
        print (paths)
        saved = os.path.join (enhance_dir, folder)
        os.system (f'python /home/gibran/project/Real-ESRGAN/inference_realesrgan.py -n RealESRGAN_x4plus -i {paths} -o {saved} --face_enhance --ext png' )
    



def remove (directory_list, input_place) :
    create_directories (directory_list, removebg_dir)
    for folder in directory_list :
        print (folder)
        data_grab = glob.glob (f'{os.path.join (input_place, folder)}/*')
        for image in data_grab :
            filename = os.path.basename (image)
            path=os.path.join (removebg_dir, folder, filename)
            remove_bg (image, path)


def crops (input_dir,output_dir, directory_list) :
    create_directories (directory_list, output_dir)
    for x in directory_list :
        crop_image (os.path.join (input_dir, x), os.path.join(output_dir, x))

    





if __name__ == "__main__" :
    main ()