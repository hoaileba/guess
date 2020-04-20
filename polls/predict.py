import tensorflow as tf 
import numpy as np
import cv2 as cv
def ans(image_dir):
    model = tf.keras.models.load_model('static/models/model.h5')
    # model.compile(optimizer = 'adam', loss = 'categorical_crossentropy',metrics = ['accuracy'])
    img = cv.imread(image_dir)
    img_gray = np.array(cv.cvtColor(img,cv.COLOR_BGR2GRAY))
    # print(img)
    img_= cv.resize(img_gray,(32,32))
    img_ = np.array(img_).reshape(1,32,32,1)
    img_ = img_/255.0
    pred = model.predict(img_)
    pre = np.argmax(pred,axis = 1)
    x = pre[-1]
    # print(x)
    # print(pred[-1][x])
    # prercent = pred[x]
    # print(pre[-1],percent)
    return x, pred[-1][x]





