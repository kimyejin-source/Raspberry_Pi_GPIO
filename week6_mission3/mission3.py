from gpiozero import LED, Button
from time import sleep
from signal import pause

# LED 핀 번호
led_pins = [8, 7, 16, 20]
leds = [LED(pin) for pin in led_pins]

# 버튼 설정 (풀업 포함)
button = Button(25, pull_up=True)

def on_button_pressed():
    for led in leds:
        led.on()
        sleep(1)
        led.off()

# 버튼이 눌렸을 때 domino4 실행행
button.when_pressed = on_button_pressed

try:
    pause()
except KeyboardInterrupt:
    print("\n프로그램을 종료합니다 :)")