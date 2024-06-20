from umqtt.simple import MQTTClient
from time import sleep

# Publish test messages e.g. with:
# mosquitto_pub -t foo_topic -m hello
# or see esp32 example at
# https://github.com/MonumentalImpact/IOT_workshop/blob/main/mqtt/test_mp_pub.py


CLIENT_NAME = 'mp1' #must be set to the name of the esp32 being used
BROKER_ADDR = 'pi5ub.local'

# Received messages from subscriptions will be delivered to this callback
def sub_cb(topic, msg):
    print((topic, msg))

def main(server="localhost"):
    c = MQTTClient(CLIENT_NAME, BROKER_ADDR)
    c.set_callback(sub_cb)
    c.connect()
    c.subscribe(b'art/emotion')
    i = 0
    while True:
        # Non-blocking wait for message
        c.check_msg()
        # Then need to sleep to avoid 100% CPU usage (in a real
        # app other useful actions would be performed instead)
        sleep(1)
        i+=1
        if i > 30:
            break

    c.disconnect()


if __name__ == "__main__":
    main()