# 🎯 버튼 스위치 활용하기

Raspberry Pi와 Python(`gpiozero` 라이브러리)를 활용하여 버튼 스위치 입력에 따라 다양한 LED 동작을 제어하는 실습입니다.

![alt text](<스크린샷 2025-04-16 122724.png>)
---

## ✅ 회로 구성
![alt text](image.png)
- 버튼: GPIO 25번 핀에 연결 (풀업 설정)
- LED: GPIO 8, 7, 16, 20번에 연결
- 저항(R)을 이용한 풀업 회로 구성

---


## 미션 3 - 버튼을 누르면 domino4 1회 실행하기
```python
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
```


## 📝 개발 환경
Raspberry Pi 5

Python

gpiozero 라이브러리

라즈베리파이 GPIO 핀 연결



## 🔧 참고사항
각 미션마다 pull_up=True 설정을 통해 풀업 저항 회로를 구현했습니다.

버튼 중복 입력 방지를 위해 sleep()을 이용한 디바운싱 처리 포함.


## 시연 영상
https://youtube.com/shorts/UBqtm8QOkB0?si=jxBO2xcju3pB4m6H