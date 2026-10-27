import serial  # Serve para acessar Arduino.
import time

# Inicia a conexão, trocar 'COM' pelo port correto.
arduino = serial.Serial('COM5', 9600, timeout=2)
texto = ""
# Deixa o Arduino resetar após enviar o código.
time.sleep(5)

def enviar_comando(cmd):
    # Converte String em Bytes
    arduino.write((cmd + '\n').encode())
    # Recebe resposta do Arduino
    return arduino.readline().decode('utf-8', errors='ignore').strip()

def comando(cmd):
    # Decidide se o payload contem ou não subtexto
    if cmd == "DISPLAY_TEXT":
        texto = input("Favor inserir texto: ")
        payload = f"{cmd}:{texto}\n"
    else:
        payload = (cmd+'\n')
    # Envia o comando e subtexto (caso presente)
    arduino.write(payload.encode('utf-8'))
    # Recebe resposta do arduino (lê o serial)
    return arduino.readline().decode('utf-8', errors='ignore').strip()

# Teste 
print("Iniciando teste")
#time.sleep(1)
#print(enviar_comando("LED_ON")) # Resposta esperada: "LED ON"
#time.sleep(1)
#print(enviar_comando("LED_OFF")) # Resposta esperada: "LED OFF"
#time.sleep(1)
#print(enviar_comando("LED_ON")) # Resposta esperada: "LED ON"   
#time.sleep(1)
#print(enviar_comando("LED_OFF")) # Resposta esperada: "LED OFF"
#time.sleep(1)
while texto != "sair":
    texto = input("Favor inserir comando: ").lower()
    if texto == "b": # Resposta esperada: "BUZZER ON"
        print(comando("BUZZER_ON"))
        pass
    elif texto == "t": # Resposta esperada: "Temperatura: X & Humidde do Ar: Y"
        print(comando("READ_TEMP")) 
    elif texto == "l": # Resposta esperada: "LED ON" & "LED OFF"
        print(comando("LED_ON")) 
        time.sleep(2)
        print(comando("LED_OFF")) 
        pass
    elif texto == "d": # Resposta esperada: "Distância: X cm"
        print(comando("READ_DIST"))
        pass
    elif texto == "e":
            print(comando("DISPLAY_TEXT")) # Resposta esperada: Exibir o texto digitado no LCD"
    elif texto == "sair":
        print("Obrigado por utilizar!")
        break
    else:
        pass

# Close port    
arduino.close()
