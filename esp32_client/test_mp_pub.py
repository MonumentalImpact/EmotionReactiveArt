from umqtt.simple import MQTTClient
import time

CLIENT_NAME = 'mp1'
BROKER_ADDR = 'pi5ub.local'
c = MQTTClient(CLIENT_NAME, BROKER_ADDR) #, keepalive=60
c.connect()
c.publish(b'art/emotion', b'happy')
c.publish(b'art/updated', str(list(time.localtime())).encode('utf-8') )

# c.disconnect()