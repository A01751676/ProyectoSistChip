# Ana Patricia Islas Mainou     A01751676
# Alex Federico Núñez Escobar   A01751559
# Proyecto Arduino

import serial,time          # Libreria para comunicar con ARDUINO
from pygame import *        # Libreria para reproducir música
from gtts import *          # Libreria para convertir texto a audio
import os                   # Libreria para comunicarse con terminal
import pywhatkit as mss     # Libreria para whatsapp
from datetime import *      # Libreria para obtener la hora

def Arduino():
    arduino = serial.Serial("COM4",9600)
    
    datos = arduino.readline()
    
    while 1:  # Bucle infinito
        print(datos)
        time.sleep(3) # delay de 3 segundos

def Musica():
    mixer.init()

    #Load audio fiel
    os.system('cd D:\descargas\Trabajos_phyton')
    print(os.system('dir'))
    print("Select a song...")
    cancion = str(input()+'.mp3')
    mixer.music.load(cancion)

    #Set preferred volume
    mixer.music.set_volume(0.2)

    #Play the music
    mixer.music.play()

    #Infinite loop
    while True:
        print("------------------------------------------------------------------------------------")
        print("Press 'p' to pause the music")
        print("Press 'r' to resume the music")
        print("Press 'c' to change song")
        print("Press 'e' to exit the program")
        #take user input
        userInput = input(" ")
        
        if userInput == 'p':
            # Pause the music
            mixer.music.pause()	
            print("music is paused....")
        elif userInput == 'r':
            # Resume the music
            mixer.music.unpause()
            print("music is resumed....")
        elif userInput == 'c':
            # Return to Music()
            print("changing song....")
            Musica()
        elif userInput == 'e':
            # Stop the music playback
            mixer.music.stop()
            print("music is stopped....")
            Inicio()

def Text_Audio():

    text = str(input())
    language = 'es-us'

    speech = gTTS(text = text, lang = language, slow = False)

    speech.save('texto.mp3')

    os.system("start texto.mp3")

    Inicio()

def Txt_Audio():

    file = open("Carta.txt", "r").read().replace("\n", " ")
    language = 'es-us'

    speech = gTTS(text = str(file), lang = language, slow = False)

    speech.save("texto1.mp3")

    os.system("start texto1.mp3")

    Inicio()


def Mensaje_Wa():
    mss.start_server()
    print("Do you want to send a message to a person or a group?")
    print("1 to send a message to a person")
    print("2 to send a message to a group")
    print("3 to not send messages")
    usinput = input("")

    time = datetime.now()
    hour = time.hour
    minute = time.minute

    if (usinput == '1'):
        # syntax: phone number with country code, message, hour and minutes
        print("Who do you want to send a message to?")
        contacto = str('+52' + input())
        print("What do you want to send him as a message?")
        mensaje = str(input())
        mss.sendwhatmsg(contacto, mensaje, hour, minute)
        print("Sending message...")
    elif (usinput == '2'):
        print("Insert the group ID")
        group_id = str(input())
        print("Insert the message: ")
        message = str(input())
        # syntax: group id, message, hour and minutes
        mss.sendwhatmsg_to_group(group_id, message, hour, minute)    
    else:
        Inicio()


def Inicio():
    print("------------------------------------------------------------------------------------")
    print("1 to enter arduino")
    print("2 to enter music")
    print("3 to enter Text to Audio")
    print("4 to enter Txt to Audio")
    print("5 to enter Message from wattsapo")
    print("6 to exit program")

    UsInput = input(" ")
    if (UsInput == '1'):
        Arduino()
    elif (UsInput == '2'):
        Musica()
    elif (UsInput == '3'):
        Text_Audio()
    elif (UsInput == '4'):
        Txt_Audio()
    elif (UsInput == '5'):
        Mensaje_Wa()
    elif (UsInput == '6'):
        Salir()
    else:
        Inicio()

def Salir():
    print("Adios Usuario")
    return 0
    

Inicio()