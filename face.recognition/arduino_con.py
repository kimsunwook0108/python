import serial
import tkinter as tk

# 시리얼 포트 설정 (COM 포트를 확인한 후 수정)
try:
    arduino = serial.Serial('COM7', 9600)  # COM3 대신 확인한 포트 번호로 수정
except serial.SerialException:
    print("Could not open COM4. Please check the port and try again.")
    exit()

# LED 상태 변수
red_led_state = False
blue_led_state = False

# LED 제어 함수
def toggle_red_led():
    global red_led_state
    red_led_state = not red_led_state
    command = b'R1' if red_led_state else b'R0'
    print(f"Sending command: {command}")
    arduino.write(command)

def toggle_blue_led():
    global blue_led_state
    blue_led_state = not blue_led_state
    command = b'B1' if blue_led_state else b'B0'
    print(f"Sending command: {command}")
    arduino.write(command)

def turn_off_all_leds():
    global red_led_state, blue_led_state
    red_led_state = False
    blue_led_state = False
    print("Sending command: A0")
    arduino.write(b'A0')

# GUI 설정
root = tk.Tk()
root.title("LED Control")

red_button = tk.Button(root, text="Red LED", command=toggle_red_led)
red_button.pack(pady=10)

blue_button = tk.Button(root, text="Blue LED", command=toggle_blue_led)
blue_button.pack(pady=10)

all_button = tk.Button(root, text="All LEDs Off", command=turn_off_all_leds)
all_button.pack(pady=10)

root.mainloop()

# 프로그램 종료 시 시리얼 포트 닫기
arduino.close()