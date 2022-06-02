
# importamos librerias
import paho.mqtt.client as mqttClient
import time

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

def on_message(client, userdata, message):
    """ Función que recibe el mensaje desde el brocker
    
    """
    print("Mensaje: {}:{}:{}".format(message.client_id, message.topic,message.payload))
    archivo.write(str(message.topic) + " " + str(message.payload) + "\n")
    return

Connected = False
broker = '10.48.93.138'
port = 1883 # Puerto por defecto
tag = "/Whats/Up/Doc"

param = [i for i in tag.split("/")]
archivo = open("{}_{}.txt".format(param[1],param[-1]),'a')

client1 = mqttClient.Client("Cliente")
client1.on_connect = on_connect
client1.on_message = on_message
client1.connect(broker,port)
client1.loop_start()

while Connected != True:
    time.sleep(1)
    client1.suscribe(tag)

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Recepción de mensajes detenida por el usuario")
        client1.disconnect()
        client1.loop_stop()
        archivo.close()
