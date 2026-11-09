import serial
import time

arduino = serial.Serial('COM5', 9600, timeout=2)
time.sleep(5)
print("Pode escrever agora!")
while True:
    arduino.write((input() + '\n').encode())
    arduino.readline().decode('utf-8', errors='ignore').strip() 