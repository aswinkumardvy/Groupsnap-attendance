import face_recognition
import os
import cv2
import numpy as np
def face_encoding(image):
    img=cv2.imread(image)
    encode=face_recognition.face_encodings(img)[0]
    return encode
def encode_list(path):
    en_list=[]
    f=[]
    files=os.listdir(path)
    for file in files:
        en=face_encoding(path+'/'+file)
        f.append(file.split('.')[0])
        # f.append(file)
        en_list.append(en)
        np.save("final_encoded_list",en_list)
        np.save("final_encoded_list_of_name",f)
    return en_list,f
def face_compare(en_list,test_image):
    matches=face_recognition.compare_faces(en_list,test_image)
    face_dist=face_recognition.face_distance(en_list,test_image)
    match_index=np.argmin(face_dist)
    if matches[match_index]:
        return match_index
# a='/home/santhosh/vs_code/dataset3'
# c='/home/santhosh/vs_code/dataset3/2036010103.jpeg'
# b=face_encoding(c)
# en,c=encode_list(a)
# # matches=face_recognition.compare_faces(en,b)
# # face_dist=face_recognition.face_distance([en],b)
# # print(face_dist)
# # print(matches)
# # print(len(en))
# # print(face_compare(en,b))
# # print(c[face_compare(en,b)])
# print(b)
# # print(en)

