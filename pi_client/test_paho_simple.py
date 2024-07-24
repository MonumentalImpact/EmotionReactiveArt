from paho.mqtt.client import Client 
client =Client()

if client.connect("pi5ub.local", 1883, 60) != 0:
    print("could not connect")

client.publish("art/emotion", "neutral")

client.disconnect()
