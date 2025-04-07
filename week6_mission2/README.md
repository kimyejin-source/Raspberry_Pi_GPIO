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


## 2️⃣ 미션 2 - 버튼을 누를 때마다 LED 토글시키기
```python
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
https://youtube.com/shorts/oOkaHx89Cds?si=omgPOsBCAub0eBcR