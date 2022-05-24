# Ana Patricia Islas Mainou     A01751676
# Alex Federico Núñez Escobar   A01751559
# Conexión con arduino

import serial,time

arduino = serial.Serial("COM4",9600)

datos = arduino.readline()

while 1:  # Bucle infinito
    print(datos)
    time.sleep(3) # delay de 3 segundos