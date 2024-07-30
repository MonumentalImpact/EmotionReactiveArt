from umqtt.simple import MQTTClient
import time
import json

CLIENT_NAME = 'mp1'
BROKER_ADDR = 'pi5ub.local'
c = MQTTClient(CLIENT_NAME, BROKER_ADDR) #, keepalive=60
c.connect()
c.publish(b'art/emotion', b'happy')
t = list(time.localtime())
c.publish(b'art/updated', json.dumps(t).encode('utf-8') )

# c.disconnect()