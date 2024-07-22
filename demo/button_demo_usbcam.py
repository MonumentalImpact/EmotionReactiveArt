import numpy as np
import cv2
from deepface import DeepFace
import os

# button=gp21
# led=gp20

from time import sleep
import gpiozero
from signal import pause


led = gpiozero.LED(20)
led.off()

button = gpiozero.Button(21)

button.when_pressed = led.on
button.when_released = led.off

"""
emotions:
angry, disgust, fear, happy, sad, surprise, neutral

put folders containing the images to be show in the 'pics' folder
each folder under 'pics' should have 7 images, one for each emotion named as
    <emotion>.jpg
"""
pics =  'pics'
dirs = os.listdir(pics)
print(f"rotating through the follow folders : {dirs}")
cur_dir = dirs[0]
num_dirs = len(dirs)

testpic = 'testusbimage.jpg'

cam = cv2.VideoCapture(0)

emotion = 'happy'
emo_count = 7 #change cur_dir after emo_count changes in emotion

print("starting main loop")
q=ord('q') #key to quit
while True:
    while True:
        ret, cam_image = cam.read()
        emo_image = cv2.imread('pics/' + cur_dir + '/' + emotion+'.jpg')
        image = np.concatenate((cam_image,emo_image), axis=1)    
        cv2.imshow('Imagetest - press big red button to read emotion',image)
#         cv2.imshow('Imagetest - press big red button to read emotion',cam_image)
        if button.is_pressed:
            break
        k = cv2.waitKey(1)
        if k != -1:
            break
    if k == q:
        break
    
    cv2.imwrite(testpic, cam_image)
    try:
        print('processing images....')
        objs = DeepFace.analyze(img_path = testpic, 
            actions = ['emotion']
        )
        print(f"analyze {testpic}:\n",objs)
        emotion = objs[0]['dominant_emotion']
        print("dominant emotion is ", emotion)
        emo_file = 'pics/' + cur_dir + '/' + emotion + '.jpg'
        cv2.imwrite( emo_file, cam_image)

    except:
        print('analysis failed')
        pass

cam.release()
cv2.destroyAllWindows()

print('program ended')


 

