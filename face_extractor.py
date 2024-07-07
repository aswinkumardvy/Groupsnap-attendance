import cv2
import os
import face_recognition
from PIL import Image 
def face_extractor(old_path,new_path):

    # old_path='/home/santhosh/vs_code/dataset/crop_img'
    #new_path='/home/santhosh/vs_code/dataset2/'
    if(os.listdir(new_path).count!=0):
        temp=os.listdir(new_path)
        for i in temp:
                os.remove(new_path+"/"+i)
    files=os.listdir(old_path)
    for i in files:
        # img=cv2.imread(dir+'/'+i)
        # img=cv2.resize(img,(256,256))

        image=face_ident(old_path+'/'+i)
        f=os.path.join(new_path+'/'+(i.split('.')[0])+'_cropped.jpg')
        
        # cv2.imwrite(f,img)
        image.save(f)
def face_ident(img_path):
    image = face_recognition.load_image_file(img_path)
    face_locations = face_recognition.face_locations(image)
    if(len(face_locations) >0):
        top, right, bottom, left = face_locations[0]
        face_image = image[top-400:bottom+256, left-256:right+256]
        pil_image = Image.fromarray(face_image)
        return pil_image
    else:
         return

old_path="/home/santhosh/vs_code/dataset/sample"
new_path="/home/santhosh/vs_code/own_dataset"
face_extractor(old_path,new_path)

# pil=face_ident("/home/santhosh/vs_code/dataset/IMG_4316.jpg")
# pil.show()