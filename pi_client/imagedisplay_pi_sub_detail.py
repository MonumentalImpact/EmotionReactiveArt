from paho.mqtt.client import Client 
#from time import sleep
from sys import exit
import json
import cv2


# Publish test messages e.g. with:
# mosquitto_pub -t foo_topic -m hello
# or see esp32 example at
# https://github.com/MonumentalImpact/IOT_workshop/blob/main/mqtt/test_mp_pub.py




CLIENT_NAME = 'artpi1' #must be set to the name of the local device
MQTT_SERVER = 'pi5ub.local'# the mqtt server
global folderPath 
folderPath = "/home/kent/dev/MITEE/EmotionReactiveArtImages/AI Art Library/"
q=ord('q')

def setup():
    emotions = ["Angry","Disgust","Fear","Happy","Sad","Surprise","Neutral"]
    for i in range(0,7):
        for x in range(0,7):
            print(emotions[i]+ emotions[x])
            cv2.namedWindow("ART",cv2.WND_PROP_FULLSCREEN)
            cv2.setWindowProperty("ART",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
            image = cv2.imread(folderPath + emotions[i]+"-"+emotions[x]+".png")
            cv2.imshow("ART",image)
            k = cv2.waitKey(1)
            #cv2.destroyAllWindows()
# Received messages from subscriptions will be delivered to this callback
def on_message(client, userdata, msg):
    print(f"client: {client}")
    print(msg.topic + " : " + str(msg.payload))
    if msg.topic == "art/emotion":
#         print("doing something based on a single emotion")
        return
    if msg.topic == "art/emotiondetail":
        payload = msg.payload.decode("utf-8")
        emos = json.loads(payload)
        emofile = emos[0][0].capitalize() + "-" + emos[1][0].capitalize() + ".png"
        print(f"emofile = {emofile}")
        cv2.namedWindow("ART",cv2.WND_PROP_FULLSCREEN)
        cv2.setWindowProperty("ART",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)        
        image = cv2.imread(folderPath + emofile)
        cv2.imshow("ART",image) 
        k = cv2.waitKey(1)
        if k == q:
            exit(0)
        return

def main(server="localhost"):
    setup()
    c = Client()
    if c.connect(server, 1883, 25000) != 0:
        print("could not connect")
        exit()
    else:
        print(f"connected to {server}")
    c.subscribe('art/emotion')
    c.subscribe('art/emotiondetail')
    c.subscribe('art/lastupdate')
    c.on_message = on_message
    c.loop_forever()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main(MQTT_SERVER)