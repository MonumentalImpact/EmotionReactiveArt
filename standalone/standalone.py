import numpy as np
import cv2
from deepface import DeepFace
# import os
import json

import platform
has_button = 'Arm' in platform.uname().machine

# button=gp21
# led=gp20

# from time import sleep
# from signal import pause
from sys import exit

if has_button:
    import gpiozero
    led = gpiozero.LED(20)
    led.off()
    button = gpiozero.Button(21)
    button.when_pressed = led.on
    button.when_released = led.off


emotions = ["angry", "happy", "sad", "fear","neutral","disgust", "surprise"]
#angry, disgust, fear, happy, sad, surprise, neutral


lastpic_file = 'lastpic.jpg'
testpic = 'testusbimage.jpg'

cam = cv2.VideoCapture(0)

emotion = 'neutral'
emotiondetail = ''
last_emotion = emotion
status_msg = emotion
emo_count = 7 #change cur_dir after emo_count changes in emotion

print("starting main loop")
q=ord('q') #key to quit
win_title = 'Emotion Reactive Art - press big red button to read emotion'
cv2.namedWindow(win_title,cv2.WND_PROP_FULLSCREEN)
cv2.setWindowProperty(win_title,cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)

while True:
    while True:
        ret, cam_image = cam.read()
        emo_image = cv2.imread(lastpic_file)
        image = np.concatenate((cam_image,emo_image), axis=1)    

        cv2.namedWindow(win_title) #,cv2.WND_PROP_FULLSCREEN)
        #cv2.setWindowProperty(win_title) #,cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
        cv2.imshow(win_title,image)
        cv2.displayOverlay(win_title, status_msg)

        if has_button and button.is_pressed:
            break
        k = cv2.waitKey(1)
        if k != -1:
            break
        
    if k == q:
        break
    
    cv2.imwrite(testpic, cam_image)
    try:
        print('processing images....')
        cv2.displayOverlay(win_title, 'processing images....')
        objs = DeepFace.analyze(img_path = testpic, 
            actions = ['emotion']
        )
#         print(f"analyze {testpic}:\n",objs)
        emotion = objs[0]['dominant_emotion']
        emotiondetail = json.dumps(sorted(objs[0]['emotion'].items(),key=lambda k: (k[1],k[0]), reverse=True))
        print("current dominant emotion is ", emotion)
        print(f"emotion details: {emotiondetail}")
        cv2.imwrite( lastpic_file, cam_image)
        analyzed = True
        status_msg = emotion + " : " + emotiondetail


    except:
        print('analysis failed')
        analyzed = False
        status_msg = f"Analysis failed last time.  Current emotion is {emotion}. Possible emotions are {' '.join(emotions)}."
        pass
    
#     if analyzed and emotion != last_emotion:
    if analyzed :
        print(f"posting dominant emotion: {emotion}")
        client.publish("art/emotion", emotion.encode('utf-8'))
        print(f"posting emotiondetail: {emotiondetail}")
        client.publish("art/emotiondetail", emotiondetail.encode('utf-8'))
        last_emotion = emotion


cam.release()
cv2.destroyAllWindows()

print('program ended')


 

