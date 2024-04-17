import cv2
from deepface import DeepFace

testpic = 'pics/testusbimage.jpg'

cam = cv2.VideoCapture(0)

while True:
    ret, image = cam.read()
    cv2.imshow('Imagetest - press any key to save',image)
    k = cv2.waitKey(1)
    if k == 'q':
        break

    cv2.imwrite(testpic, image)
    try:
        objs = DeepFace.analyze(img_path = testpic, 
            actions = ['emotion']
        )
#         print(f"analyze {testpic}:\n",objs)
        print("dominant emotion is ", objs[0]['dominant_emotion'])

    except:
#         print('.')
        pass

cam.release()
cv2.destroyAllWindows()



 
