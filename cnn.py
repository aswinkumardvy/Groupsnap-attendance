from keras.models import Sequential
from keras.layers import Conv2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense
import cv2
import numpy as np
from PIL import Image
import pickle
import dataset_creator as dc
def cnn(train_labels,train_images):
    classifier = Sequential()
    classifier.add(Conv2D(32, (3, 3), input_shape = (256, 256, 3), activation = 'relu'))
    classifier.add(MaxPooling2D(pool_size = (2, 2)))
    classifier.add(Conv2D(64, (3, 3), activation = 'relu'))
    classifier.add(MaxPooling2D(pool_size = (2, 2)))
    classifier.add(Flatten())
    classifier.add(Dense(units = 128, activation = 'relu'))
    classifier.add(Dense(units = 3, activation = 'sigmoid'))
    classifier.compile(optimizer = 'adam', loss = 'sparse_categorical_crossentropy', metrics = ['accuracy'])


    h=classifier.fit(train_images, train_labels, epochs=20)
    loss, accuracy = classifier.evaluate(train_images, train_labels)
    print(loss,accuracy)
    return classifier
def given_image(path):
    image=dc.cnn_image(path)
    return np.asarray(image)
