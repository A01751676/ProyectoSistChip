# pip install paho-mqtt

# importacion de librerias
import time # Para controlr tiempos de inactividad
import random
from cv2 import connectedComponents # Para generar un conjunto de datos a enviar
import paho.mqtt.client as mqttClient # libreria de MQTT

# Generar datos
n = 10000
aleatorio = [random.randint(0,2) for i in range (n)]
d = {0 : 'R', 1 : 'G'}
ValRGB = [d.get(x,'B') for x in aleatorio]
print (ValRGB)


def on_connect(client, userdata, flags, rc):
    """ Esta función valida la conexión al servidor
    
    """
    if rc == 0: # Conexion exitosa
        print("Conectado al Brocker")
        global Connected
        Connected = True
    else:
        print("Fallo en la conexión")
    
    return

Connected = False
broker = '10.197.1.103'
port = 1883 # Puerto por defecto
tag = "/Whats/Up/Doc"
#user = 
#passsword =

client = mqttClient.Client() 
client.on_connect=on_connect
client.connect(broker,port)
client.loop_start()

while Connected != True:
    time.sleep(0.1) # Se duerme 1 milsegundo
    try:
        for i in ValRGB:
            value = '{"Valor":"'+ "#" + str(i) +'"}'
            print(tag,value)
            client.publish(tag,value,qos=2)
            time.sleep(1)
    except KeyboardInterrupt: #Cuando presionas Ctrl + C
        print("Envio de datos detenido por el usuario")
        client.disconnect()
        client.loop_stop()