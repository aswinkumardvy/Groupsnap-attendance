import os
import numpy as np
def labels():
    
    dir='/home/santhosh/vs_code/dataset/crop_img/'
    files=os.listdir(dir)
    labels=[]
    name_label=[]
    # def name(x):
    #     t=x[:11]
    #     if(t[10:11]=='('):
    #         return t[:10]
    #     else:
    #         return t[:11]
    for i in files:
        x=i[:10]

        if x=='2036010073':
            labels.append(0)
            name_label.append('2036010073')
        elif x=='2036010086':
            labels.append(1)
            name_label.append('2036010086')           
        elif x=='2036010085':
            labels.append(2)
            name_label.append('2036010085')
        elif x=='2036010093':
            labels.append(3)
            name_label.append('2036010093')
        elif x=='2036010103':
            labels.append(4)
            name_label.append('2036010103')
        elif x=='2136090003':
            labels.append(5)
            name_label.append('2136090003')
    labels=np.asarray(labels)
    np.save('final_labels',labels)
    np.save('final_name_labels',name_label)
    print(len(labels))
    print(len(name_label))
labels=[]
name_label=[]
def label(x):
        if x=='2036010073':
            return 0
        elif x=='2036010086':
            return 1
        elif x=='2036010085':
            return 2
        elif x=='2036010093':
            return 3
        elif x=='2036010103':
            return 4
        elif x=='2136090003':
            return 5
            # name_label.append('2136090003')        
    