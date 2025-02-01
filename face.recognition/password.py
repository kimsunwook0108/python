import tkinter as tk
import serial

# Initialize serial communication with Arduino
arduino = serial.Serial('COM8', 9600)  # Adjust 'COM8' to your Arduino's port

# def send_signal(signal):
#     arduino.write(f'{signal}\n'.encode())

def move_to_180():
    arduino.write(b'1')

def move_to_0():
   arduino.write(b'0')

# Create the main window
root = tk.Tk()
root.title("Servo Motor Control")

# Create buttons
button_180 = tk.Button(root, text="180도", command=move_to_180)
button_0 = tk.Button(root, text="0도", command=move_to_0)

# Place buttons on the window
button_180.pack(pady=10)
button_0.pack(pady=10)

# Run the GUI loop
root.mainloop()