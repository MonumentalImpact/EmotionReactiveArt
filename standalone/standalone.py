import numpy as np
import cv2 as cv
from deepface import DeepFace
import platform, shutil

window_mode = 'fullscreen' # or 'debug'
#window_mode = 'debug'

has_button = 'Arm' in platform.uname().machine or 'raspi' in platform.uname().release

# from time import sleep
# from signal import pause
#from sys import exit

if has_button:
    #gpio pins 20 and 21 used for LED and button
    import gpiozero
    led = gpiozero.LED(20)
    led.off()
    button = gpiozero.Button(21)
    button.when_pressed = led.on
    button.when_released = led.off


emotions = ["angry", "happy", "sad", "fear","neutral","disgust", "surprise"]
#angry, disgust, fear, happy, sad, surprise, neutral

refresh_delay = 30 #milliseconds between video refresh

initial_lastpic_file = '../images/start_emo_image.png'
lastpic_file = 'lastpic.png'
shutil.copyfile( initial_lastpic_file, lastpic_file)

testpic_file = 'testusbimage.jpg' #this is updated from the camera

logo_file = '../images/MITEE_LogoName_640x480_DARKMODE.png' #displayed in top right
logo_image = cv.imread(logo_file)

cam = cv.VideoCapture(0)

emotion = 'neutral'
emotiondetail = ''
last_emotion = emotion
status_msg = emotion

q=ord('q') #key to quit
win_title = 'Emotion Reactive Art - press the big red button to read emotion'
# if window_mode == 'fullscreen':
#     cv.namedWindow(win_title,cv.WND_PROP_FULLSCREEN)
#     cv.setWindowProperty(win_title,cv.WND_PROP_FULLSCREEN,cv.WINDOW_FULLSCREEN)
# else:
#     cv.namedWindow(win_title) #,cv.WND_PROP_FULLSCREEN)
#     cv.setWindowProperty(win_title,cv.WND_PROP_AUTOSIZE,cv.WINDOW_AUTOSIZE)

#run deepface on  last image to initialize model
print("initializing....")
objs = DeepFace.analyze(img_path = lastpic_file, actions = ['emotion'])

#set up art images
# global folderPath 
folderPath = "/home/kent/dev/EmotionReactiveArtImages/AI Art Library/"

# if window_mode == 'debug':
#     #make sure all the files are there
#     for i in emotions:
#         for x in emotions:
#             artfile = x.capitalize() + "-" + i.capitalize() + ".png"
#             print(f"artfile = {artfile}")
#             art_image = cv.imread(folderPath + artfile)
            
art_image = cv.imread(folderPath + "Neutral-Neutral.png")

print("starting main loop")
while True:
    while True:
        ret, cam_image = cam.read()
        emo_image = cv.imread(lastpic_file)
        #image = np.concatenate((cam_image,emo_image), axis=1)
        #print(f"cam {cam_image.shape}, emo {emo_image.shape}, art {art_image.shape}")
        image = np.vstack((np.hstack((cam_image,emo_image,logo_image)),art_image))
        
        #cv.namedWindow(win_title) #,cv.WND_PROP_FULLSCREEN)
        if window_mode == 'fullscreen':
            cv.namedWindow(win_title,cv.WND_PROP_FULLSCREEN)
            cv.setWindowProperty(win_title,cv.WND_PROP_FULLSCREEN,cv.WINDOW_FULLSCREEN)
        else:
            cv.namedWindow(win_title) #,cv.WND_PROP_FULLSCREEN)
            cv.setWindowProperty(win_title,cv.WND_PROP_AUTOSIZE,cv.WINDOW_AUTOSIZE)
        cv.imshow(win_title,image)
        cv.displayOverlay(win_title, status_msg)

        if has_button and button.is_pressed:
            break
        k = cv.waitKey(refresh_delay)
        if k != -1:
            break
        
    if k == q:
        break
    
    cv.imwrite(testpic_file, cam_image)
    try:
        print('processing images....')
        cv.displayOverlay(win_title, 'processing images....')
        objs = DeepFace.analyze(img_path = testpic_file, 
            actions = ['emotion']
        )
        print(f"analyze {testpic_file}:\n",objs)
        emotion = objs[0]['dominant_emotion']
        emotiondetail = sorted(objs[0]['emotion'].items(),key=lambda k: (k[1],k[0]), reverse=True)
        print("current dominant emotion is ", emotion)
        print(f"emotion details: {emotiondetail}")
        cv.imwrite( lastpic_file, cam_image)
        analyzed = True
        status_msg = emotion + " : " + str(emotiondetail)


    except:
        print('analysis failed')
        analyzed = False
        status_msg = f"Analysis failed last time.  Current emotion is {emotion}. Possible emotions are {' '.join(emotions)}."
        pass
    
#     if analyzed and emotion != last_emotion:
    if analyzed :
        print(f"dominant emotion: {emotion}")
        print(f"emotiondetail: {emotiondetail}")
        last_emotion = emotion
        artfile = emotiondetail[0][0].capitalize() + "-" + emotiondetail[1][0].capitalize() + ".png"
        print(f"artfile = {artfile}")
        art_image = cv.imread(folderPath + artfile)



cam.release()
cv.destroyAllWindows()

print('program ended')


 

