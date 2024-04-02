import cv2
from deepface import DeepFace

testpic = 'pics/testusbimage.jpg'

cam = cv2.VideoCapture(0)

while True:
	ret, image = cam.read()
	cv2.imshow('Imagetest - press any key to save',image)
	k = cv2.waitKey(1)
	if k != -1:
		break
cv2.imwrite(testpic, image)
cam.release()
cv2.destroyAllWindows()

objs = DeepFace.analyze(img_path = testpic, 
    actions = ['age', 'gender', 'race', 'emotion']
)
print(f"analyze {testpic}:\n",objs)
