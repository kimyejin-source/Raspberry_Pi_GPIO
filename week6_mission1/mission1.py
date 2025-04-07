from gpiozero import LED, Button
from signal import pause

led = LED(8)
button = Button(25, pull_up=True)

def led_on():
    led.on()

def led_off():
    led.off()

button.when_pressed = led_on
button.when_released = led_off

try:
    pause()
except KeyboardInterrupt:
    print("\n프로그램을 종료합니다 :)")