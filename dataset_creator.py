import numpy as np
import os
import cv2
from PIL import Image
import os
import numpy as np
import cv2
import face_recognition
import pickle
import firebase_admin
import json
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import  storage
import label_creator as lc

cred = credentials.Certificate("/home/santhosh/vs_code/serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://attendance-3d35a-default-rtdb.firebaseio.com/",
    'storageBucket': "attendance-3d35a.appspot.com"
})
# file_path="/home/santhosh/vs_code/dataset2"
def dataset_creator(file_path):
    data=[]
    name_list=[]
    labels=[]
    # initial(file_path)
    files=os.listdir(file_path)
    file_name='final_array_list_big.pkl'
    for images in files:
            image=cv2.imread(file_path+"/"+images)
            image2 = cv2.resize(image, (256, 256))
            array=image2/255
            data.append(array)
            name_list.append(images[:10])
            labels.append(lc.label(images[:10]))
    np.save("final_name_labels",name_list)
    np.save("final_labels",labels)
    with open(file_name, 'wb') as f:
        pickle.dump(data, f)
    return data

def cnn_image(file_path):
    image=cv2.imread(file_path)
    image2 = cv2.resize(image, (256, 256))
    array=image2/255
    return array
            
            
def initial(file_path):
    files=os.listdir(file_path)
    for images in files:
        fileName = f'{file_path}/{images}'
        bucket = storage.bucket()
        blob = bucket.blob(fileName)
        blob.upload_from_filename(fileName)

str=dataset_creator("/home/santhosh/vs_code/dataset/crop_img")

# with open(str, 'rb') as f:
#     my_list = pickle.load(f)
# print(my_list)

    

