from PIL import Image
from django.core.files import File
from io import BytesIO

def process_your_picture(user,local_pic,cloud_pic):
    if local_pic and cloud_pic:
        # -----------------Start your code here ----------------
        # Use PIL image object to access two pictures
        img_local = Image.open(local_pic.path)
        img_cloud = Image.open(cloud_pic.path)
        # implement your code here ------------>
        
        # output_img should be PIL image object
        # output_img_type should be suffix of your image
        # modify following two lines 
        output_img = img_cloud
        output_img_type = 'png'
        # ----------------End your code here --------------
        file_object = image_pil_to_django(output_img, output_img_type)
        user.localpics.imagedisplay.save('output.PNG',file_object)
        user.localpics.save()

def image_pil_to_django(img, img_format):
    img_format = img_format.upper()
    buffer = BytesIO()
    img.save(buffer, format=img_format)
    file_object = File(buffer)
    return file_object

