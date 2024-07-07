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
from datetime import datetime
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import  storage
# cred = credentials.Certificate("/home/santhosh/vs_code/serviceAccountKey.json")
# firebase_admin.initialize_app(cred, {
# 'databaseURL': "https://attendance-3d35a-default-rtdb.firebaseio.com/",
# 'storageBucket': "attendance-3d35a.appspot.com"
# })
def database_main():
        cred = credentials.Certificate("/home/santhosh/vs_code/serviceAccountKey.json")
        firebase_admin.initialize_app(cred, {
        'databaseURL': "https://attendance-3d35a-default-rtdb.firebaseio.com/",
        'storageBucket': "attendance-3d35a.appspot.com"
        })
detail={0:'2036010073',1:'2036010086',2:'2036010085',3:'2036010103',4:'2036010101',5:'2036010093',6:'2136090003'}
l=['2036010073','2036010086','2036010085','2036010103','2036010101','2036010093','2136090003']
def prediction_comp(k,c):
        if(k==c):
                database_changer(k)
def database_changer(k):
        database_main()
        current_date_time = datetime.now()
        ref=db.reference('/Students')
        sp_ref=ref.child(detail[k])
        sp_ref.update({'total_attendance':sp_ref.child('total_attendance').get()+1})
        sp_ref.update({'last_attendance_time':f'{current_date_time}'})
