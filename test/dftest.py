import os
from deepface import DeepFace

pic1 = "pics/happy1.jpeg"
pic2 = "pics/happy2.jpeg"
result = DeepFace.verify(img1_path = pic1, img2_path = pic2)
print("verify:\n",result)


for pic in [pic1, pic2]:
    objs = DeepFace.analyze(img_path = pic, 
        actions = ['age', 'gender', 'race', 'emotion']
    )
    print(f"analyze {pic}:\n",objs)
