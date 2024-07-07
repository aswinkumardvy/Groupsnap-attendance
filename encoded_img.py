import os
import cv2
import numpy as np
# dir='/home/santhosh/vs_code/dataset2/'
def img_encoder(dir):
    files=os.listdir(dir)
    img_array=[]
    for file in files:
        img=cv2.imread(dir+file)
        img_array.append(img)
    a=np.asarray(img_array)/255.
    b=np.asarray(img_array)
    np.save('img_array_1_0',b)
    # x=np.load('imd_array')
    # print(x)