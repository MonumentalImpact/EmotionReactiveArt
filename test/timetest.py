import os
from deepface import DeepFace
import timeit

pic1 = "pics/happy1.jpeg"

def get_emotion(pic=pic1):
    objs = DeepFace.analyze(img_path = pic, 
        actions = ['emotion']
    )
    return objs

for n in [1, 10, 100, 1000]:
    print(f"{n} runs: ",
          timeit.timeit(stmt=get_emotion,number=n))