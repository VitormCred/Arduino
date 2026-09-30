import serial # Serve para acessar Arduino.
import time

# Inicia a conexão, trocar 'COM' pelo port correto.
arduino = serial.Serial('COM5', 9600, timeout=2)

# Deixa o Arduino resetar após enviar o código.
time.sleep(5)

def enviar_comando(cmd):
    # Converte String em Bytes
    arduino.write((cmd + '\n').encode())
    # Recebe resposta do Arduino
    return arduino.readline().decode('utf-8', errors='ignore').strip()

# Teste 
print("Iniciando teste")
time.sleep(1)
print(enviar_comando("LED_ON")) # Resposta Esperada: "LED ON"
time.sleep(5)
print(enviar_comando("LED_OFF")) # Resposta Esperada: "LED OFF"
time.sleep(5)
print(enviar_comando("LED_ON")) # Resposta Esperada: "LED ON"   
time.sleep(5)
print(enviar_comando("LED_OFF")) # Resposta Esperada: "LED OFF"
time.sleep(5)
while True:
    texto = input("Favor inserir B para buzzer ou N para não buzzer & S para sair: ")
    while texto == "b" or texto == "B": # Resposta Esperada: "BUZZER ON"
        print(enviar_comando("BUZZER_ON"))
        texto = input("Favor inserir B para buzzer: ")

# Close port
arduino.close()