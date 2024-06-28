
from face_crop_plus import Cropper
from backgroundremover.bg import remove


def crop_image (input_dir, output_dir) :
    cropper = Cropper(face_factor=0.55, strategy="largest", 
                  padding = 'constant', output_size=(600,700))
    cropper.process_dir (input_dir=input_dir, output_dir=output_dir)

def remove_bg(src_img_path, out_img_path):
    f = open(src_img_path, "rb")
    model_choices = ["u2net", "u2net_human_seg", "u2netp"]
    data = f.read()
    img = remove(data, model_name=model_choices[1],
                 alpha_matting=True,
                 alpha_matting_foreground_threshold=200,
                 alpha_matting_background_threshold=10,
                 alpha_matting_erode_structure_size=10,
                 alpha_matting_base_size=1000)
    f.close()
    f = open(out_img_path, "wb")
    f.write(img)
    f.close()


