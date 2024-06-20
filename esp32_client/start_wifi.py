# wlan = network.WLAN(network.STA_IF) # create station interface
# wlan.active(True)       # activate the interface
# wlan.scan()             # scan for access points
# wlan.isconnected()      # check if the station is connected to an AP
# wlan.connect('ssid', 'key') # connect to an AP
# wlan.config('mac')      # get the interface's MAC address
# wlan.ifconfig()         # get the interface's IP/netmask/gw/DNS addresses
# 
# ap = network.WLAN(network.AP_IF) # create access-point interface
# ap.config(ssid='ESP-AP') # set the SSID of the access point
# ap.config(max_clients=10) # set how many clients can connect to the network
# ap.active(True)         # activate the interface
# wlan.config(reconnects=n)

from time import sleep


def wifi_connect(hostname=None, ssid='art-iot', key='artisfun'):
    import network
    if hostname is not None:
        network.hostname(hostname)
    wlan = network.WLAN(network.STA_IF)
#     wlan.config(reconnects=5)
    wlan.active(True)
    print('connecting to network...')
    tries = 0
    while True:
        wlan.connect(ssid, key)
        if wlan.isconnected():
            break
        sleep(15)
        tries += 1
        if tries > 8 :
            print('failed to connect to network')
            break
            
    print('network config:', wlan.ifconfig())

wifi_connect()
