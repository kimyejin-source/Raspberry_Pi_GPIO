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


## 4️⃣ 미션 4 - 버튼을 누를 때마다 4-bit 카운터 값 증가시키기

```python
from gpiozero import LED, Button
from time import sleep

# 4개의 LED 핀 (MSB -> LSB 순서)
led_pins = [8, 7, 16, 20]
leds = [LED(pin) for pin in led_pins]

# 버튼 핀 (풀업 활성화)
button = Button(25, pull_up=True)

# 4-bit 카운터 (0~15)
counter = 0

print("버튼을 누를 때마다 4비트 카운터 증가!")

while True:
    # 버튼이 눌렸을 때만 처리
    if button.is_pressed:
        counter = (counter + 1) % 16

        # 카운트 값을 4개의 LED로 표시
        for i in range(4):
            bit = (counter >> (3 - i)) & 1
            if bit:
                leds[i].on()
            else:
                leds[i].off()

        # 디바운스 및 중복 방지
        while button.is_pressed:
            sleep(0.05)  # 버튼을 떼기 전까지 대기

        sleep(0.2)  # 다음 입력까지 약간 대기
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
https://youtube.com/shorts/AktmIixvCec?si=F7oD8LcqokP5tDd9