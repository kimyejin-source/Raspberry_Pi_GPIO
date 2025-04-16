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
