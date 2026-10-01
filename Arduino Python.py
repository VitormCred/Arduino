import serial 
# Serve para acessar Arduino.
import time

# Inicia a conexão, trocar 'COM' pelo port correto.
arduino = serial.Serial('COM4', 9600, timeout=2)
texto = ""
# Deixa o Arduino resetar após enviar o código.
time.sleep(5)

def enviar_comando(cmd):
    # Converte String em Bytes
    arduino.write((cmd + '\n').encode())
    # Recebe resposta do Arduino
    return arduino.readline().decode('utf-8', errors='ignore').strip()

# Teste 
print("Iniciando teste")
#time.sleep(1)
#print(enviar_comando("LED_ON")) # Resposta Esperada: "LED ON"
#time.sleep(1)
#print(enviar_comando("LED_OFF")) # Resposta Esperada: "LED OFF"
#time.sleep(1)
#print(enviar_comando("LED_ON")) # Resposta Esperada: "LED ON"   
#time.sleep(1)
#print(enviar_comando("LED_OFF")) # Resposta Esperada: "LED OFF"
#time.sleep(1)
while texto != "Sair":
    texto = input("Favor inserir comando: ")
    if texto == "b" or texto == "B": # Resposta Esperada: "BUZZER ON"
        print(enviar_comando("BUZZER_ON"))
        pass
    elif texto == "t" or texto == "T": # Resposta Esperada: "Temperatura: X & Humidde do Ar: Y"
        print(enviar_comando("READ_TEMP")) 
    elif texto == "L" or texto == "l": # Resposta Eperad: "LED ON" & "LED OFF"
        print(enviar_comando("LED_ON")) 
        time.sleep(3)
        print(enviar_comando("LED_OFF")) 
        pass
    elif texto == "Sair":
        print("Obrigado por utilizar!")
        break
    else:
        pass

# Close port    
arduino.close()
