# button=gp21
# led=gp20


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

