# button=gp21
# led=gp20

# import lgpio
# 
# hled = lgpio.gpiochip_open(0) #the hardware
# lgpio.gpio_claim_output( hled, 20, 1) #set pin 20 to output
# 
# def led( state=0):
#     lgpio.gpio_write( hled, 20, state)
    
from time import sleep
import gpiozero
from signal import pause


led = gpiozero.LED(20)

for _ in range(5):
    led.on()
    sleep(1)
    led.off()
    sleep(1)
    
led.off()

button = gpiozero.Button(21)

button.when_pressed = led.on
button.when_released = led.off

pause()

