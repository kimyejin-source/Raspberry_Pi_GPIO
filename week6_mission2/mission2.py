from gpiozero import LED, Button
from signal import pause
from time import sleep

led = LED(8)
button = Button(25, pull_up=True)

def toggle_led():
    led.toggle()  # 현재 상태에서 반대 상태로 바꿈 (켜져 있으면 끄고, 꺼져 있으면 켬)
    sleep(0.5)    # 중복 입력 방지 (디바운싱 효과)

button.when_pressed = toggle_led

try:
    pause()
except KeyboardInterrupt:
    print("\n프로그램을 종료합니다 :)")