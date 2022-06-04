# Ana Patricia Islas Mainou     A01751676
# Alex Federico Núñez Escobar   A01751559
# Interfaz Gráfica proyecto DISEÑO DE CHIPS

# Using tkinter, firstafull you need to create things and then you show that things

from cgitb import text
from multiprocessing.spawn import import_main_path
from tkinter import *          # importamos toda la libreria de 'tkinter' 
from tkinter import Button, Label,Tk,filedialog, ttk, Frame, PhotoImage
from turtle import bgcolor
from click import open_file
from gtts import *             # Libreria para convertir texto a audio
import random
from matplotlib import artist
import mutagen
# Librerias para mapa -----------------------------
import tkintermapview
import geocoder
# Libreria para musica
import pygame
from pygame import *
from SongRI import *
#from LightsMotors2 import *
# Libreria para mostrar la fecha
import datetime as dt
import time
# Libreria para quitar fondo 
from PIL import Image, ImageTk
#from win32api import GetSystemMetrics
# Librerias para reversa
import cv2
import numpy as np
#import RPi.GPIO as GPIO
# ibrerias para el telefono y mensajes
from twilio.rest import Client


# Start Tkinter fro the interface
root = Tk()

img_dir = 'Imagenes'

#os.chdir('FB_integration')
# Principal window
root.title('Carrito')     # Define title
root.geometry('800x440')  # configure sice of screen
root.config(bg = 'black')
root.resizable(0,0)  
#root.wm_attributes('-transparentcolor','black')

# We include tab panel
nb = ttk.Notebook(root)
nb.pack(pady = 0)

color_tab1 = '#CDCDCD' # Menu
color_tab2 = '#00858A' # Música
color_tab3 = '#C539FD' # GPS
color_tab4 = '#008F39' # Motores
color_tab5 = '#FF9900' # Mensajes
color_tab6 = '#4169E1' # Llamadas
color_tab7 = '#FFCD48' # Reversa
text_color = '#FFFFFF' # Color del texto

os.chdir(img_dir)

# Creating tabs
tab1 = Frame(nb, width = 500, height = 500, background = color_tab1)
tab2 = Frame(nb, width = 500, height = 500, background = color_tab2)
tab3 = Frame(nb, width = 500, height = 500, background = color_tab3)
tab4 = Frame(nb, width = 500, height = 500, background = color_tab4)
tab5 = Frame(nb, width = 500, height = 500, background = color_tab5)
tab6 = Frame(nb, width = 500, height = 500, background = color_tab6)
tab7 = Frame(nb, width = 500, height = 500, background = color_tab7)

# pack Tabs
tab1.place(x = 0, y = 0) 
tab2.place(x = 0, y = 0) 
tab3.place(x = 0, y = 0) 
tab4.place(x = 0, y = 0) 
tab5.place(x = 0, y = 0)
tab6.place(x = 0, y = 0) 
tab7.place(x = 0, y = 0) 

# Menú
menu_con_fondo = PhotoImage(file = 'menu_con_fondo.png')
menu_sin_fondo = PhotoImage(file = 'menu_sin_fondo.png')

# Música
musica_con_fondo = PhotoImage(file = 'musica_con_fondo.png')
musica_sin_fondo = PhotoImage(file = 'musica_sin_fondo.png')

# Mapa
mapa_con_fondo = PhotoImage(file = 'mapa_con_fondo.png')
mapa_sin_fondo = PhotoImage(file = 'mapa_sin_fondo.png')

# Motores
motores_con_fondo = PhotoImage(file = 'motores_con_fondo.png')
motores_sin_fondo = PhotoImage(file = 'motores_sin_fondo.png')

# Mensajes
mensajes_con_fondo = PhotoImage(file = 'mensajes_con_fondo.png')
mensajes_sin_fondo = PhotoImage(file = 'mensajes_sin_fondo.png')

# Teléfono
telefono_con_fondo = PhotoImage(file = 'telefono_con_fondo.png')
telefono_sin_fondo = PhotoImage(file = 'telefono_sin_fondo.png')

# Camara
camara_con_fondo = PhotoImage(file = 'reversa_con_fondo.png')
camara_sin_fondo = PhotoImage(file = 'reversa_sin_fondo.png')

os.chdir('..')
#Reduce las dimensiones de la imagen en un (ancho_imagen / 2)

# Menu
menu_con_fondo_sub = menu_con_fondo.subsample(32)
menu_sin_fondo_sub = menu_sin_fondo.subsample(32)

# Música
musica_con_fondo_sub = musica_con_fondo.subsample(7)
musica_sin_fondo_sub = musica_sin_fondo.subsample(32)

# Mapa
mapa_con_fondo_sub = mapa_con_fondo.subsample(7)
mapa_sin_fondo_sub = mapa_sin_fondo.subsample(32)

# Motores
motores_con_fondo_sub = motores_con_fondo.subsample(7)
motores_sin_fondo_sub = motores_sin_fondo.subsample(32)

# Mensajes
mensajes_con_fondo_sub = mensajes_con_fondo.subsample(7)
mensajes_sin_fondo_sub = mensajes_sin_fondo.subsample(32)

# Telefono
telefono_con_fondo_sub = telefono_con_fondo.subsample(7)
telefono_sin_fondo_sub = telefono_sin_fondo.subsample(32)

# Camara
camara_con_fondo_sub = camara_con_fondo.subsample(7)
camara_sin_fondo_sub = camara_sin_fondo.subsample(32)

# Adding tabs to screen 
nb.add(tab1, image = menu_sin_fondo_sub)
nb.add(tab2, image = musica_sin_fondo_sub)
nb.add(tab3, image = mapa_sin_fondo_sub)
nb.add(tab4, image = motores_sin_fondo_sub)
nb.add(tab5, image = mensajes_sin_fondo_sub)
nb.add(tab6, image = telefono_sin_fondo_sub)
nb.add(tab7, image = camara_sin_fondo_sub)

# Sabemos la fecha y hora
date = dt.datetime.now()
tiemp = time.strftime("%I:%M:%S %p")


# Labels para texto ----------------------------

titulo_musica = Label(tab2, text = "REPRODUCTOR DE MÚSICA", font = ('Calibri',30), background = color_tab2, fg = text_color).place(x = 160,y = 5)
fecha_musica = Label(tab2, text = f"{date:%A, %B %d}", font = ('Calibri',10), background = color_tab2, fg = text_color).place(x = 690,y = 5)
hora_musica = Label(tab2, text = tiemp, font = ('Calibri',10), background = color_tab2, fg = text_color).place(x = 710,y = 20)

titulo_menu = Label(tab3, text = "MAPA Y POSICIÓN GEOGRÁFICA", font = ('Calibri',30), background = color_tab3, fg = text_color).place(x = 160,y = 5)
fecha_menu = Label(tab3, text = f"{date:%A, %B %d}", font = ('Calibri',10), background = color_tab3, fg = text_color).place(x = 690,y = 5)
hora_menu = Label(tab3, text = tiemp, font = ('Calibri',10), background = color_tab3, fg = text_color).place(x = 710,y = 20)

titulo_menu = Label(tab3, text = "MAPA Y POSICIÓN GEOGRÁFICA", font = ('Calibri',30), background = color_tab3).place(x = 160,y = 5)
fecha_menu = Label(tab3, text = f"{date:%A, %B %d}", font = ('Calibri',10), background = color_tab3).place(x = 690,y = 5)
hora_menu = Label(tab3, text = tiemp, font = ('Calibri',10), background = color_tab3).place(x = 710,y = 20)

titulo_motores = Label(tab4, text = "MOVER MOTORES DEL COCHE", font = ('Calibri',30), background = color_tab4, fg = text_color).place(x = 160,y = 5)
fecha_motores = Label(tab4, text = f"{date:%A, %B %d}", font = ('Calibri',10), background = color_tab4, fg = text_color).place(x = 690,y = 5)
hora_motores = Label(tab4, text = tiemp, font = ('Calibri',10), background = color_tab4, fg = text_color).place(x = 710,y = 20)

titulo_mensajes = Label(tab5, text = "LEER MENSAJES NO LEIDOS", font = ('Calibri',30), background = color_tab5, fg = text_color).place(x = 160,y = 5)
fecha_mensajes = Label(tab5, text = f"{date:%A, %B %d}", font = ('Calibri',10), background = color_tab5, fg = text_color).place(x = 690,y = 5)
hora_mensajes = Label(tab5, text = tiemp, font = ('Calibri',10), background = color_tab5, fg = text_color).place(x = 710,y = 20)

titulo_telefono = Label(tab6, text = "LLAMAR A FAVORITOS", font = ('Calibri',30), background = color_tab6, fg = text_color).place(x = 160,y = 5)
fecha_telefono = Label(tab6, text = f"{date:%A, %B %d}", font = ('Calibri',10), background = color_tab6, fg = text_color).place(x = 690,y = 5)
hora_telefono = Label(tab6, text = tiemp, font = ('Calibri',10), background = color_tab6, fg = text_color).place(x = 710,y = 20)

nb.pack(expand = 1, fill ="both")

# Global Variables and functions -------------------------------------------------------------------------------
status_musica = False # status 0 => hide, 1 => show
status_mapa = False # status 0 => hide, 1 => show
status_motor = False # status 0 => hide, 1 => show
status_luces = False # status 0 => hide, 1 => show
status_telefono = False # status 0 => hide, 1 => show
status_camara = False # status 0 => hide, 1 => show
status_global = False # status 0 => hide, 1 => show
contador = 1

if contador == 1:
    nb.hide(1)
    nb.hide(2)
    nb.hide(3)
    nb.hide(4)
    nb.hide(5)
    nb.hide(6)
    contador = contador + 1

def travel_global():
    global status_global      
    if (status_global):
        status_global = False
    else:
        nb.hide(1)
        nb.hide(2)
        nb.hide(3)
        nb.hide(4)
        nb.hide(5)
        nb.hide(6)
        nb.select(0)
        status_global = False

# Components of TAB1 = GLOBAL -------------------------------------------------------------------------------------
# Global ----------------------------------------------------------------------------------------------------------

def travel_musica():
    global status_musica    
    if (status_musica == False):
        nb.add(tab2, image = musica_sin_fondo_sub)
        nb.select(1)

def travel_mapa():
    global status_mapa    
    if (status_mapa == False):
        nb.add(tab3, image = mapa_sin_fondo_sub)
        nb.select(2)

def travel_motor():
    global status_motor    
    if (status_motor == False):
        nb.add(tab4, image = motores_sin_fondo_sub)
        nb.select(3)

def travel_luces():
    global status_luces    
    if (status_luces == False):
        nb.add(tab5, image = mensajes_sin_fondo_sub)
        nb.select(4)

def travel_telefono():
    global status_telefono    
    if (status_telefono == False):
        nb.add(tab6, image = telefono_sin_fondo_sub)
        nb.select(5)

def travel_camara():
    global status_camara    
    if (status_camara == False):
        nb.add(tab7, image = camara_sin_fondo_sub)
        nb.select(6)

boton_mus = Button(tab1, image = musica_con_fondo_sub, borderwidth = 0 , cursor='hand2', command = travel_musica, background = color_tab1).place(x=70, y=20)
boton_mapa = Button(tab1, image = mapa_con_fondo_sub, borderwidth = 0 , cursor='hand2', command = travel_mapa, background = color_tab1).place(x=320, y=20)
boton_motor = Button(tab1, image = motores_con_fondo_sub, borderwidth = 0 , cursor='hand2', command = travel_motor, background = color_tab1).place(x=570, y=20) 
boton_luces = Button(tab1, image = mensajes_con_fondo_sub, borderwidth = 0 , cursor='hand2', command = travel_luces, background = color_tab1).place(x=70, y=200)
boton_telefono = Button(tab1, image = telefono_con_fondo_sub, borderwidth = 0 , cursor='hand2', command = travel_telefono, background = color_tab1).place(x=320, y=200)
boton_camara = Button(tab1, image = camara_con_fondo_sub, borderwidth = 0 , cursor='hand2', command = travel_camara, background = color_tab1).place(x=570, y=200)


# Components of TAB2 -------------------------------------------------------------------------------------
# Música -------------------------------------------------------------------------------------------------

pygame.mixer.init()
pygame.mixer.init(frequency = 44100)
actual_song = ''
direction = ''

## --------------------------------------
## GLOBAL VARIABLES FOR MP3 PLAYER
first = True
songList = getSongList()
songIndex = 0
status = False # status 0 => pause, 1 => play
imagen = False

# INITIATE MP3 OBJETCT WITH FIRST SONG
initMP3Player()
data = loadSong(songList [songIndex])
actual_song = songList [songIndex]
song_name = data["title"]

## MP3 PLAYER COMMANDS TO BUTTONS --------------------------------------------
lista = []
for i in range (50,300,10):
    lista.append(i)

def evalFinal():
    if (knowSongEnd()):
        next()

# PLAY PREVIOUS SONG
def previous():
    global data
    global songIndex
    songIndex, data = playPrevious(songList, songIndex)
    updateLabels()

# PLAY AND PAUSE SONG
def play_pause():
    global first
    global status 
    global actualizar   

    if (status):
        pauseSong()
        status = False
    else:
        first = playSong(first)
        status = True

# PLAY NEXT SONG
def next():
    global data
    global songIndex
    songIndex, data = playNext(songList, songIndex)
    tab2.delete('all')
    updateLabels()

def rewind():
    pygame.mixer.music.rewind()

def randomorder():
    global first, songList, randomsongList, songIndex,  data
    mixer.music.stop()
    songList = getSongList()
    randomsongList= randomSongOrder(songList)
    loadSong(randomsongList [songIndex])
    songIndex, data = playNext(randomsongList, songIndex)
    tab2.delete('all')
    updateLabels()
    

def stop():
    global actualizar
    pygame.mixer.music.stop()
    travel_global()


def updateLabels():
    global titulo_cancion,artista_cancion,album_cancion,ano_cancion,rate_cancion,stereo_cancion
    try:
        titulo_cancion = Label(tab2, text = data["title"], font = ('Calibri',10), background = color_tab2, fg = text_color).place(x = 600,y = 70)
        artista_cancion = Label(tab2, text = data["artist"], font = ('Calibri',10), background = color_tab2, fg = text_color).place(x = 600,y = 90)
        album_cancion = Label(tab2, text = data["album"], font = ('Calibri',10), background = color_tab2, fg = text_color).place(x = 600,y = 110)
        ano_cancion = Label(tab2, text = data["year"], font = ('Calibri',10), background = color_tab2, fg = text_color).place(x = 600,y = 130)
        rate_cancion = Label(tab2, text = data["sampleRate"], font = ('Calibri',10), background = color_tab2, fg = text_color).place(x = 600,y = 150)
        stereo_cancion = Label(tab2, text = "Stereo", font = ('Calibri',10), background = color_tab2, fg = text_color).place(x = 600,y = 170)
    except: 
        pass

# Labels de cancion
titulo_cancion = Label(tab2, text = data["title"], font = ('Calibri',10), background = color_tab2, fg = text_color).place(x = 600,y = 70)
artista_cancion = Label(tab2, text = data["artist"], font = ('Calibri',10), background = color_tab2, fg = text_color).place(x = 600,y = 90)
album_cancion = Label(tab2, text = data["album"], font = ('Calibri',10), background = color_tab2, fg = text_color).place(x = 600,y = 110)
ano_cancion = Label(tab2, text = data["year"], font = ('Calibri',10), background = color_tab2, fg = text_color).place(x = 600,y = 130)
rate_cancion = Label(tab2, text = data["sampleRate"], font = ('Calibri',10), background = color_tab2, fg = text_color).place(x = 600,y = 150)
stereo_cancion = Label(tab2, text = "Stereo", font = ('Calibri',10), background = color_tab2, fg = text_color).place(x = 600,y = 170)

# Bars 
bar1 = ttk.Progressbar(tab2, orient = 'vertical', length = 170, maximum = 300, style = 'Vertical.TProgressbar')
bar1.place(x=50, y=60)
bar2 = ttk.Progressbar(tab2, orient = 'vertical', length = 170, maximum = 300, style = 'Vertical.TProgressbar')
bar2.place(x=70, y=60)
bar3 = ttk.Progressbar(tab2, orient = 'vertical', length = 170, maximum = 300, style = 'Vertical.TProgressbar')
bar3.place(x=90, y=60)
bar4 = ttk.Progressbar(tab2, orient = 'vertical', length = 170, maximum = 300, style = 'Vertical.TProgressbar')
bar4.place(x=110, y=60)
bar5 = ttk.Progressbar(tab2, orient = 'vertical', length = 170, maximum = 300, style = 'Vertical.TProgressbar')
bar5.place(x=130, y=60)
bar6 = ttk.Progressbar(tab2, orient = 'vertical', length = 170, maximum = 300, style = 'Vertical.TProgressbar')
bar6.place(x=150, y=60)
bar7 = ttk.Progressbar(tab2, orient = 'vertical', length = 170, maximum = 300, style = 'Vertical.TProgressbar')
bar7.place(x=170, y=60)
bar8 = ttk.Progressbar(tab2, orient = 'vertical', length = 170, maximum = 300, style = 'Vertical.TProgressbar')
bar8.place(x=190, y=60)
bar9 = ttk.Progressbar(tab2, orient = 'vertical', length = 170, maximum = 300, style = 'Vertical.TProgressbar')
bar9.place(x=210, y=60)
bar10 = ttk.Progressbar(tab2, orient = 'vertical', length = 170, maximum = 300, style = 'Vertical.TProgressbar')
bar10.place(x=230, y=60)
bar11 = ttk.Progressbar(tab2, orient = 'vertical', length = 170, maximum = 300, style = 'Vertical.TProgressbar')
bar11.place(x=250, y=60)
bar12 = ttk.Progressbar(tab2, orient = 'vertical', length = 170, maximum = 300, style = 'Vertical.TProgressbar')
bar12.place(x=270, y=60)
bar13 = ttk.Progressbar(tab2, orient = 'vertical', length = 170, maximum = 300, style = 'Vertical.TProgressbar')
bar13.place(x=290, y=60)
bar14 = ttk.Progressbar(tab2, orient = 'vertical', length = 170, maximum = 300, style = 'Vertical.TProgressbar')
bar14.place(x=310, y=60)
bar15 = ttk.Progressbar(tab2, orient = 'vertical', length = 170, maximum = 300, style = 'Vertical.TProgressbar')
bar15.place(x=330, y=60)
bar16 = ttk.Progressbar(tab2, orient = 'vertical', length = 170, maximum = 300, style = 'Vertical.TProgressbar')
bar16.place(x=350, y=60)
bar17 = ttk.Progressbar(tab2, orient = 'vertical', length = 170, maximum = 300, style = 'Vertical.TProgressbar')
bar17.place(x=370, y = 60)
bar18 = ttk.Progressbar(tab2, orient = 'vertical', length = 170, maximum = 300, style = 'Vertical.TProgressbar')
bar18.place(x=390, y=60)
bar19 = ttk.Progressbar(tab2, orient = 'vertical', length = 170, maximum = 300, style = 'Vertical.TProgressbar')
bar19.place(x=410, y=60)
bar20 = ttk.Progressbar(tab2, orient = 'vertical', length = 170, maximum = 300, style = 'Vertical.TProgressbar')
bar20.place(x=430, y=60)

# Imágenes para el reproductor de música
os.chdir(img_dir)
icono_rewind = PhotoImage(file = 'icono_rewind.png')       # rewind
icono_repeat = PhotoImage(file = 'icono_repetir.png')      # repeat
icono_previous = PhotoImage(file = 'icono_previous.png')   # previous
icono_play = PhotoImage(file = 'icono_play.png')           # play
icono_pause = PhotoImage(file = 'icono_pausa.png')         # pause
icono_next = PhotoImage(file = 'icono_next.png')           # next
icono_random = PhotoImage(file = 'icono_random.png')       # random
os.chdir('..')

#Reduce las dimensiones de la imagen en un (ancho_imagen / 2)
icono_rewind_sub = icono_rewind.subsample(7)
icono_repeat_sub = icono_repeat.subsample(15)
icono_previous_sub = icono_previous.subsample(10)
icono_play_sub = icono_play.subsample(7)
icono_pause_sub = icono_pause.subsample(7)
icono_next_sub = icono_next.subsample(10)
icono_random_sub = icono_random.subsample(15)

def change_img():
    global imagen

    if (imagen):
        play_pause_img = icono_play_sub
        Button_play_pause = Button(tab2, image = play_pause_img, borderwidth = 0, cursor='hand2', command = change_img, background = color_tab2, fg = text_color)
        Button_play_pause.place(x = 405, y = 245)
        imagen = False
        play_pause()
    else:
        play_pause_img = icono_pause_sub
        Button_play_pause = Button(tab2, image = play_pause_img, borderwidth = 0, cursor='hand2', command = change_img, background = color_tab2, fg = text_color)
        Button_play_pause.place(x = 405, y = 245)
        imagen = True
        play_pause()

# Botones para el reproductor de música
Button_repeat = Button(tab2, image = icono_repeat_sub, borderwidth = 0, cursor='hand2', command = rewind, background = color_tab2, fg = text_color)
Button_repeat.place(x = 110, y = 290)
Button_previous = Button(tab2, image = icono_previous_sub, borderwidth = 0, cursor='hand2', command = previous, background = color_tab2, fg = text_color)
Button_previous.place(x = 170, y = 270)
Button_rewind = Button(tab2, image = icono_rewind_sub, borderwidth = 0, cursor='hand2', command = rewind, background = color_tab2, fg = text_color)
Button_rewind.place(x = 270, y = 245)
Button_play_pause = Button(tab2, image = icono_play_sub, borderwidth = 0, cursor='hand2', command = change_img, background = color_tab2, fg = text_color)
Button_play_pause.place(x = 405, y = 245)
Button_next = Button(tab2, image = icono_next_sub, borderwidth = 0, cursor='hand2', command = next, background = color_tab2, fg = text_color)
Button_next.place(x = 540, y = 270)
Button_random = Button(tab2, image = icono_random_sub, borderwidth = 0, cursor='hand2', command = randomorder, background = color_tab2, fg = text_color)
Button_random.place(x = 640, y = 290)


boton_global1 = Button(tab2, image = menu_con_fondo_sub, borderwidth = 0, cursor='hand2', command = stop, background = color_tab2, fg = text_color).place(x=10, y=10)

# Components of TAB3 -------------------------------------------------------------------------------------
# Mapa ---------------------------------------------------------------------------------------------------

frame_map = LabelFrame(tab3)
#frame_map.pack(padx = 20, pady = 20)
frame_map.place(x = 60, y = 60)

#latitud = 19.597111
#longitud = -99.227274

g = geocoder.ip('me')

latitud = g.latlng[0]
longitud = g.latlng[1]


map_widget = tkintermapview.TkinterMapView(frame_map, width = 700, height = 300, corner_radius = 0)
map_widget.set_position(latitud,longitud)
map_widget.set_zoom(16)

# Marker
marker_1 = map_widget.set_marker(latitud,longitud, text="Carrito")

map_widget.pack()


boton_global2 = Button(tab3, image = menu_con_fondo_sub, borderwidth = 0, cursor='hand2', command = travel_global, background = color_tab3, fg = text_color).place(x=10, y=10)
# Components of TAB4 -------------------------------------------------------------------------------------
# MOTOR --------------------------------------------------------------------------------------------------

# Imágenes para el motor
os.chdir(img_dir)
adelante_con_fondo = PhotoImage(file = 'flecha_up.png')        # adelante
reversa_con_fondo = PhotoImage(file = 'flecha_down.png')       # reversa
derecha_con_fondo = PhotoImage(file = 'flecha_right.png')      # derecha
izquierda_con_fondo = PhotoImage(file = 'flecha_left.png')     # izquierda
front_con_fondo = PhotoImage(file = 'musica_con_fondo.png')    # Delante
back_con_fondo = PhotoImage(file = 'musica_con_fondo.png')     # Reversa
stopp_con_fondo = PhotoImage(file = 'musica_con_fondo.png')    # Parking
right_con_fondo = PhotoImage(file = 'musica_con_fondo.png')    # Derecha
left_con_fondo = PhotoImage(file = 'musica_con_fondo.png')     # Izquierda
icono_intermitentes = PhotoImage(file = 'icono_intermitentes.png') # intermitentes
icono_fog = PhotoImage(file = 'icono_fog.png')                     # Fog
os.chdir('..')

#Reduce las dimensiones de la imagen en un (ancho_imagen / 2)
adelante_con_fondo_sub = adelante_con_fondo.subsample(10)
reversa_con_fondo_sub = reversa_con_fondo.subsample(10)
derecha_con_fondo_sub = derecha_con_fondo.subsample(10)
izquierda_con_fondo_sub = izquierda_con_fondo.subsample(10)
front_con_fondo_sub = front_con_fondo.subsample(20)
back_con_fondo_sub = back_con_fondo.subsample(20)
stopp_con_fondo_sub = stopp_con_fondo.subsample(20)
right_con_fondo_sub = right_con_fondo.subsample(20)
left_con_fondo_sub = left_con_fondo.subsample(20)
icono_intermitentes_sub = icono_intermitentes.subsample(20);
icono_fog_sub = icono_fog.subsample(20);

# Variable global
global velocidad
velocidad = 0

def frontt():
    global velocidad
    velocidad = 1

    img_adelante = Label(tab4, image = front_con_fondo_sub)
    img_adelante.place(x=500, y=100)

def right():
    global velocidad
    velocidad = 2

    img_derecha = Label(tab4, image = right_con_fondo_sub)
    img_derecha.place(x=500, y=100)

def left():
    global velocidad
    velocidad = 3

    img_izquierda = Label(tab4, image = left_con_fondo_sub)
    img_izquierda.place(x=500, y=100)

def backward():
    global velocidad
    velocidad = 4
    
    img_reversa = Label(tab4, image = back_con_fondo_sub)
    img_reversa.place(x=500, y=100)

def intermitentes_ligths():
    print('Hola');

def fog_ligths():
    print('Hola');


adelante = Button(tab4, image = adelante_con_fondo_sub, borderwidth = 0, cursor='hand2', command = frontt, background = color_tab4, fg = text_color).place(x=225, y=55)
derecha = Button(tab4, image = derecha_con_fondo_sub, borderwidth = 0, cursor='hand2', command = right, background = color_tab4, fg = text_color).place(x=395, y=135)
izquierda = Button(tab4, image = izquierda_con_fondo_sub, borderwidth = 0, cursor='hand2', command = left, background = color_tab4, fg = text_color).place(x=75, y=135)
reversa = Button(tab4, image = reversa_con_fondo_sub, borderwidth = 0, cursor='hand2', command = backward, background = color_tab4, fg = text_color).place(x=225, y=215)

intermitente = Button(tab4, image = icono_intermitentes_sub, borderwidth = 0, cursor='hand2', command = intermitentes_ligths, background = color_tab4, fg = text_color).place(x=600, y=55)
faros = Button(tab4, image = icono_fog_sub, borderwidth = 0, cursor='hand2', command = fog_ligths, background = color_tab4, fg = text_color).place(x=600, y=200)

boton_global3 = Button(tab4, image = menu_con_fondo_sub, borderwidth = 0, cursor='hand2', command = travel_global, background = color_tab4, fg = text_color).place(x=10, y=10)

# Components of TAB5 -------------------------------------------------------------------------------------
# MENSAJES --------------------------------------------------------------------------------------------------

def mensaje1():
    # Your Account SID from twilio.com/console
    account_sid = "AC1e6d6b8325da4b4406edcf8cbd914d58"
    # Your Auth Token from twilio.com/console
    auth_token  = "dd532883b0cfa24ea4591cf66da612f6"
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        to="+525618675785", 
        from_="+12074924829",
        body="Logre mandar mensajes mss")
    print(message.sid)

def mensaje2():
    # Your Account SID from twilio.com/console
    account_sid = "AC1e6d6b8325da4b4406edcf8cbd914d58"
    # Your Auth Token from twilio.com/console
    auth_token  = "dd532883b0cfa24ea4591cf66da612f6"
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        to="+525618675785", 
        from_="+12074924829",
        body="Logre mandar mensajes mss")
    print(message.sid)

def mensaje3():
    # Your Account SID from twilio.com/console
    account_sid = "AC1e6d6b8325da4b4406edcf8cbd914d58"
    # Your Auth Token from twilio.com/console
    auth_token  = "dd532883b0cfa24ea4591cf66da612f6"
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        to="+525618675785", 
        from_="+12074924829",
        body="Logre mandar mensajes mss")
    print(message.sid)

def mensaje4():
    # Your Account SID from twilio.com/console
    account_sid = "AC1e6d6b8325da4b4406edcf8cbd914d58"
    # Your Auth Token from twilio.com/console
    auth_token  = "dd532883b0cfa24ea4591cf66da612f6"
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        to="+525618675785", 
        from_="+12074924829",
        body="Logre mandar mensajes mss")
    print(message.sid)


mensaje_1 = Button(tab5, text= " Mensaje 1 ", borderwidth = 0, cursor='hand2', height="3", width="80",font=('Calibri',10),command = mensaje1, background = color_tab5, fg = text_color).place(x=120, y=80)
mensaje_2 = Button(tab5, text= " Mensaje 2 ", borderwidth = 0, cursor='hand2', height="3", width="80",font=('Calibri',10),command = mensaje2, background = color_tab5, fg = text_color).place(x=120, y=150)
mensaje_3 = Button(tab5, text= " Mensaje 3 ", borderwidth = 0, cursor='hand2', height="3", width="80",font=('Calibri',10),command = mensaje3, background = color_tab5, fg = text_color).place(x=120, y=220)
mensaje_4 = Button(tab5, text= " Mensaje 4 ", borderwidth = 0, cursor='hand2', height="3", width="80",font=('Calibri',10),command = mensaje4, background = color_tab5, fg = text_color).place(x=120, y=290)


boton_global4 = Button(tab5, image = menu_con_fondo_sub, borderwidth = 0, cursor='hand2', command = travel_global, background = color_tab5, fg = text_color).place(x=10, y=10)
# Components of TAB6 -------------------------------------------------------------------------------------
# TELEFONO -----------------------------------------------------------------------------------------------

def llamada_AlexN():
    # Your Account SID from twilio.com/console
    account_sid = "AC1e6d6b8325da4b4406edcf8cbd914d58"
    # Your Auth Token from twilio.com/console
    auth_token  = "dd532883b0cfa24ea4591cf66da612f6"
    client = Client(account_sid, auth_token)
    call = client.calls.create(
        to="+525618675785", 
        from_="+12074924829",
        url = "http://demo.twilio.com/docs/voice.xml"
    )
    print(call.sid)

def llamada_AnaP():
    # Your Account SID from twilio.com/console
    account_sid = "AC10e4010f3e3006844e9d8aef19130a37"
    # Your Auth Token from twilio.com/console
    auth_token  = "9be6a29df31a87edbfb396e7f9877b0c"
    client = Client(account_sid, auth_token)
    call = client.calls.create(
        to="+525510041137", 
        from_="+18127220493",
        url = "http://demo.twilio.com/docs/voice.xml"
    )
    print(call.sid)


AlexNu = Button(tab6, text= " Alex N ", borderwidth = 0, cursor='hand2', height="3", width="80",font=('Calibri',10), command = llamada_AlexN, background = color_tab6, fg = text_color).place(x=120, y=80)
AnaP = Button(tab6, text= " Ana P ", borderwidth = 0, cursor='hand2', height="3", width="80",font=('Calibri',10), command = llamada_AnaP, background = color_tab6, fg = text_color).place(x=120, y=150)
Contacto3 = Button(tab6, text= " Contacto 3 ", borderwidth = 0, cursor='hand2', height="3", width="80",font=('Calibri',10), background = color_tab6, fg = text_color).place(x=120, y=220)
Contacto4 = Button(tab6, text= " Contacto 4 ", borderwidth = 0, cursor='hand2', height="3", width="80",font=('Calibri',10), background = color_tab6, fg = text_color).place(x=120, y=290)

boton_global5 = Button(tab6, image = menu_con_fondo_sub, borderwidth = 0, cursor='hand2', command = travel_global, background = color_tab6, fg = text_color).place(x=10, y=10)


# Components of TAB7 -------------------------------------------------------------------------------------
# CAMARA -------------------------------------------------------------------------------------------------


# Create a Label to capture the Video frames sized 800 x 420
label =Label(tab7)
label.place(x = 60, y = 10)
cap= cv2.VideoCapture(0)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 358)


reverseStatusPin = 32
#GPIO.setup(reverseStatusPin, GPIO.OUT)
# Define function to show frame
def show_frames():
   # Get the latest frame and convert into Image
   #GPIO.output(reverseStatusPin, GPIO.HIGH)
   cv2image= cv2.cvtColor(cap.read()[1],cv2.COLOR_BGR2RGB)
   
   linesPts = np.array([[0, 358], [75, 268], [565, 268], [640, 358]])
   linesPts = linesPts.reshape((-1, 1, 2))
   cv2image = cv2.polylines(cv2image, np.int32([linesPts]), True, (255, 0, 0), 2)
   
   linesPts = np.array([[75, 268], [150, 178], [490, 178], [565, 268]])
   linesPts = linesPts.reshape((-1, 1, 2))
   cv2image = cv2.polylines(cv2image, np.int32([linesPts]), True, (255, 255, 0), 2)
   
   linesPts = np.array([[150, 178], [225, 88], [415, 88], [490, 178]])
   linesPts = linesPts.reshape((-1, 1, 2))
   cv2image = cv2.polylines(cv2image, np.int32([linesPts]), True, (0, 255, 0), 2)
   
   
   img = Image.fromarray(cv2image)
   # Convert image to PhotoImage
   imgtk = ImageTk.PhotoImage(image = img)
   label.imgtk = imgtk
   label.configure(image=imgtk)
   # Repeat after an interval to capture continiously
   label.after(20, show_frames)

show_frames()

boton_global6 = Button(tab7, image = menu_con_fondo_sub, borderwidth = 0, cursor='hand2', command = travel_global, background = color_tab7, fg = text_color).place(x=10, y=10)
# Create an infinite loop
root.mainloop()