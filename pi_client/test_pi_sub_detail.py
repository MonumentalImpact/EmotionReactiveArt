from paho.mqtt.client import Client 
#from time import sleep
from sys import exit
import json


# Publish test messages e.g. with:
# mosquitto_pub -t foo_topic -m hello
# or see esp32 example at
# https://github.com/MonumentalImpact/IOT_workshop/blob/main/mqtt/test_mp_pub.py




CLIENT_NAME = 'artpi1' #must be set to the name of the local device
MQTT_SERVER = 'pi5ub.local'# the mqtt server

# Received messages from subscriptions will be delivered to this callback
def on_message(client, userdata, msg):
    print(f"client: {client}")
    print(msg.topic + " : " + str(msg.payload))
    if msg.topic == "art/emotion":
        print("doing something based on a single emotion")
        return
    if msg.topic == "art/emotiondetail":
        payload = msg.payload.decode("utf-8")
        emos = json.loads(payload)
        emofile = emos[0][0].capitalize() + "-" + emos[1][0].capitalize() + ".png"
        print(f"emofile = {emofile}")
        #this is where we call update_image(emofile)
        return

def main(server="localhost"):
    c = Client()
    if c.connect(server, 1883, 60) != 0:
        print("could not connect")
        exit()
    c.subscribe('art/emotion')
    c.subscribe('art/emotiondetail')
    c.subscribe('art/lastupdate')
    c.on_message = on_message
    c.loop_forever()


if __name__ == "__main__":
    main(MQTT_SERVER)