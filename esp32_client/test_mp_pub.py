from umqtt.simple import MQTTClient

CLIENT_NAME = 'mp1'
BROKER_ADDR = 'pi5ub.local'
c = MQTTClient(CLIENT_NAME, BROKER_ADDR) #, keepalive=60
c.connect()
c.publish(b'art/emotion', b'happy')

# c.disconnect()