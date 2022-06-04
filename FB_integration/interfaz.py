# Ana Patricia Islas Mainou     A01751676
# Alex Federico Núñez Escobar   A01751559
# Interfaz Gráfica proyecto DISEÑO DE CHIPS

# Using tkinter, firstafull you need to create things and then you show that things

from cgitb import text
from multiprocessing.spawn import import_main_path
from tkinter import *          # importamos toda la libreria de 'tkinter' 
from tkinter import Button, Label,Tk,filedialog, ttk, Frame, PhotoImage
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
from win32api import GetSystemMetrics
# Librerias para reversa
import cv2
import numpy as np
#import RPi.GPIO as GPIO
# ibrerias para el telefono y mensajes
from twilio.rest import Client


# Start Tkinter fro the interface
root = Tk()

img_dir = 'Imagenes'
os.chdir('FB_integration')
# Principal window
root.title('Carrito')     # Define title
root.geometry('800x440')  # configure sice of screen
root.config(bg = 'black')
root.resizable(0,0)  
#root.wm_attributes('-transparentcolor','black')

# We include tab panel
nb = ttk.Notebook(root)
nb.pack(pady = 0)


# Colores aleatorios
color1 = ["#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])]
color2 = ["#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])]
color3 = ["#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])]
color4 = ["#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])]

# Fondo Tab
os.chdir(img_dir)
fondo_menu = PhotoImage(file = 'fondo_menu.png')
fondo_musica = PhotoImage(file = 'fondo_musica.png')
fondo_mapa = PhotoImage(file = 'fondo_mapa.png')
fondo_motores = PhotoImage(file = 'fondo_motores.png')
fondo_mensajes = PhotoImage(file = 'fondo_mensajes.png')
fondo_telefono = PhotoImage(file = 'fondo_telefono.png')
fondo_camara = PhotoImage(file = 'fondo_reversa.png')


# Creating tabs
tab1 = Frame(nb, width = 500, height = 500)
tab2 = Frame(nb, width = 500, height = 500)
tab3 = Frame(nb, width = 500, height = 500)
tab4 = Frame(nb, width = 500, height = 500)
tab5 = Frame(nb, width = 500, height = 500)
tab6 = Frame(nb, width = 500, height = 500)
tab7 = Frame(nb, width = 500, height = 500)

# pack Tabs
tab1.place(x = 0, y = 0) 
tab2.place(x = 0, y = 0) 
tab3.place(x = 0, y = 0) 
tab4.place(x = 0, y = 0) 
tab5.place(x = 0, y = 0)
tab6.place(x = 0, y = 0) 
tab7.place(x = 0, y = 0) 

# Menú
fondo_menu = PhotoImage(file = 'fondo_menu.png')
menu_con_fondo = PhotoImage(file = 'menu_con_fondo.png')
menu_sin_fondo = PhotoImage(file = 'menu_sin_fondo.png')

# Música
fondo_musica = PhotoImage(file = 'fondo_musica.png')
musica_con_fondo = PhotoImage(file = 'musica_con_fondo.png')
musica_sin_fondo = PhotoImage(file = 'musica_sin_fondo.png')

# Mapa
fondo_mapa = PhotoImage(file = 'fondo_mapa.png')
mapa_con_fondo = PhotoImage(file = 'mapa_con_fondo.png')
mapa_sin_fondo = PhotoImage(file = 'mapa_sin_fondo.png')

# Motores
fondo_motores = PhotoImage(file = 'fondo_motores.png')
motores_con_fondo = PhotoImage(file = 'motores_con_fondo.png')
motores_sin_fondo = PhotoImage(file = 'motores_sin_fondo.png')

# Mensajes
fondo_mensajes = PhotoImage(file = 'fondo_mensajes.png')
mensajes_con_fondo = PhotoImage(file = 'mensajes_con_fondo.png')
mensajes_sin_fondo = PhotoImage(file = 'mensajes_sin_fondo.png')

# Teléfono
fondo_telefono = PhotoImage(file = 'fondo_telefono.png')
telefono_con_fondo = PhotoImage(file = 'telefono_con_fondo.png')
telefono_sin_fondo = PhotoImage(file = 'telefono_sin_fondo.png')

# Camara
fondo_camara = PhotoImage(file = 'fondo_reversa.png')
camara_con_fondo = PhotoImage(file = 'reversa_con_fondo.png')
camara_sin_fondo = PhotoImage(file = 'reversa_sin_fondo.png')

os.chdir('..')
#Reduce las dimensiones de la imagen en un (ancho_imagen / 2)

# Menu
fondo_menu_sub = fondo_menu.subsample(2)
menu_con_fondo_sub = menu_con_fondo.subsample(32)
menu_sin_fondo_sub = menu_sin_fondo.subsample(32)

# Música
fondo_musica_sub = fondo_musica.subsample(2)
musica_con_fondo_sub = musica_con_fondo.subsample(7)
musica_sin_fondo_sub = musica_sin_fondo.subsample(32)

# Mapa
fondo_mapa_sub = fondo_mapa.subsample(2)
mapa_con_fondo_sub = mapa_con_fondo.subsample(7)
mapa_sin_fondo_sub = mapa_sin_fondo.subsample(32)

# Motores
fondo_motores_sub = fondo_motores.subsample(2)
motores_con_fondo_sub = motores_con_fondo.subsample(7)
motores_sin_fondo_sub = motores_sin_fondo.subsample(32)

# Mensajes
fondo_mensajes_sub = fondo_mensajes.subsample(2)
mensajes_con_fondo_sub = mensajes_con_fondo.subsample(7)
mensajes_sin_fondo_sub = mensajes_sin_fondo.subsample(32)

# Telefono
fondo_telefono_sub = fondo_telefono.subsample(2)
telefono_con_fondo_sub = telefono_con_fondo.subsample(7)
telefono_sin_fondo_sub = telefono_sin_fondo.subsample(32)

# Camara
fondo_camara_sub = fondo_camara.subsample(2)
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


# Canvas para imagenes y labels sin fondo ----------------------------
canvas_menu = Canvas(tab1)
canvas_menu.create_image(0,0, image = fondo_menu_sub, anchor = 'nw')
canvas_menu.pack(fill = "both", expand = 1)

canvas_menu = Canvas(tab3)
canvas_menu.create_image(0,0, image = fondo_mapa_sub, anchor = 'nw')
canvas_menu.create_text(400,30, text = "MAPA Y POSICIÓN GEOGRÁFICA", font = ('Calibri',30))
canvas_menu.create_text(725,15, text = f"{date:%A, %B %d, %Y}", font = ('Calibri',10))
canvas_menu.create_text(750,30, text = tiemp, font = ('Calibri',10))
canvas_menu.pack(fill = "both", expand = 1)

canvas_motores = Canvas(tab4)
canvas_motores.create_image(0,0, image = fondo_motores_sub, anchor = 'nw')
canvas_motores.create_text(400,30, text = "MOVER MOTORES DEL COCHE", font = ('Calibri',30))
canvas_motores.create_text(725,15, text = f"{date:%A, %B %d, %Y}", font = ('Calibri',10))
canvas_motores.create_text(750,30, text = tiemp, font = ('Calibri',10))
canvas_motores.pack(fill = "both", expand = 1)

canvas_mensajes = Canvas(tab5)
canvas_mensajes.create_image(0,0, image = fondo_mensajes_sub, anchor = 'nw')
canvas_mensajes.create_text(400,30, text = "LEER MENSAJES NO LEIDOS", font = ('Calibri',30))
canvas_mensajes.create_text(725,15, text = f"{date:%A, %B %d, %Y}", font = ('Calibri',10))
canvas_mensajes.create_text(750,30, text = tiemp, font = ('Calibri',10))
canvas_mensajes.pack(fill = "both", expand = 1)

canvas_telefono = Canvas(tab6)
canvas_telefono.create_image(0,0, image = fondo_telefono_sub, anchor = 'nw')
canvas_telefono.create_text(400,30, text = "LLAMAR A FAVORITOS", font = ('Calibri',30))
canvas_telefono.create_text(725,15, text = f"{date:%A, %B %d, %Y}", font = ('Calibri',10))
canvas_telefono.create_text(750,30, text = tiemp, font = ('Calibri',10))
canvas_telefono.pack(fill = "both", expand = 1)

canvas_camara = Canvas(tab7)
canvas_camara.create_image(0,0, image = fondo_camara_sub, anchor = 'nw')
canvas_camara.pack(fill = "both", expand = 1)



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

boton_mus = Button(tab1, image = musica_con_fondo_sub, borderwidth = 0 , cursor='hand2', command = travel_musica).place(x=70, y=20)
boton_mapa = Button(tab1, image = mapa_con_fondo_sub, borderwidth = 0 , cursor='hand2', command = travel_mapa).place(x=320, y=20)
boton_motor = Button(tab1, image = motores_con_fondo_sub, borderwidth = 0 , cursor='hand2', command = travel_motor).place(x=570, y=20) 
boton_luces = Button(tab1, image = mensajes_con_fondo_sub, borderwidth = 0 , cursor='hand2', command = travel_luces).place(x=70, y=200)
boton_telefono = Button(tab1, image = telefono_con_fondo_sub, borderwidth = 0 , cursor='hand2', command = travel_telefono).place(x=320, y=200)
boton_camara = Button(tab1, image = camara_con_fondo_sub, borderwidth = 0 , cursor='hand2', command = travel_camara).place(x=570, y=200)


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

def start_playback():
    global actual_song, song_name, direction, actualizar 
    bar1['value'] = random.choice(lista)
    bar2['value'] = random.choice(lista)
    bar3['value'] = random.choice(lista)
    bar4['value'] = random.choice(lista)
    bar5['value'] = random.choice(lista)
    bar6['value'] = random.choice(lista)
    bar7['value'] = random.choice(lista)
    bar8['value'] = random.choice(lista)
    bar9['value'] = random.choice(lista)
    bar10['value'] = random.choice(lista)
    bar11['value'] = random.choice(lista)
    bar12['value'] = random.choice(lista)
    bar13['value'] = random.choice(lista)
    bar14['value'] = random.choice(lista)
    bar15['value'] = random.choice(lista)
    bar16['value'] = random.choice(lista)
    bar17['value'] = random.choice(lista)
    bar18['value'] = random.choice(lista)
    bar19['value'] = random.choice(lista)
    bar20['value'] = random.choice(lista)

    time = pygame.mixer.music.get_pos()
    x = int(int(time)*0.001)
    actual_song = songList [songIndex]

    audio = mutagen.File(actual_song)
    log = audio.info.length
    minutes, seconds = divmod(log, 60)

    minutes, seconds = int(minutes), int (seconds)
    tt = minutes * 60 + seconds
    actualizar = root.after(100, start_playback)
    #evalFinal()

    if (x == tt):
        root.after_cancel(actualizar)
        stop_effect()

    updateLabels()


def evalFinal():
    if (knowSongEnd()):
        next()
    else:
        start_playback()

# PLAY PREVIOUS SONG
def previous():
    global data
    global songIndex
    stop_effect()
    songIndex, data = playPrevious(songList, songIndex)
    updateLabels()
    start_playback()

# PLAY AND PAUSE SONG
def play_pause():
    global first
    global status 
    global actualizar   

    if (status):
        pauseSong()
        stop_effect()
        status = False
    else:
        first = playSong(first)
        status = True
        start_playback()

# PLAY NEXT SONG
def next():
    global data
    global songIndex
    stop_effect()
    songIndex, data = playNext(songList, songIndex)
    frame2.delete('all')
    updateLabels()
    start_playback()

def rewind():
    pygame.mixer.music.rewind()

def randomorder():
    global first, songList, randomsongList, songIndex,  data
    mixer.music.stop()
    songList = getSongList()
    randomsongList= randomSongOrder(songList)
    loadSong(randomsongList [songIndex])
    songIndex, data = playNext(randomsongList, songIndex)
    frame2.delete('all')
    updateLabels()
    start_playback()
    


def stop_effect():
    bar1['value'] = 60
    bar2['value'] = 70
    bar3['value'] = 80
    bar4['value'] = 90
    bar5['value'] = 100
    bar6['value'] = 90
    bar7['value'] = 80
    bar8['value'] = 70
    bar9['value'] = 60
    bar10['value'] = 70
    bar11['value'] = 80
    bar12['value'] = 90
    bar13['value'] = 100
    bar14['value'] = 90
    bar15['value'] = 70
    bar16['value'] = 60
    bar17['value'] = 70
    bar18['value'] = 80
    bar19['value'] = 90
    bar20['value'] = 100

def stop():
    global actualizar
    pygame.mixer.music.stop()
    stop_effect()
    travel_global()


def updateLabels():
    global title, artista,album, Year, SampleR
    try:
        frame2.create_image(0,0, image = fondo_musica_sub, anchor = 'nw')
        frame2.create_text(400,30, text = "REPRODUCTOR DE MÚSICA", font = ('Calibri',30))
        frame2.create_text(725,15, text = f"{date:%A, %B %d, %Y}", font = ('Calibri',10))
        frame2.create_text(750,30, text = tiemp, font = ('Calibri',10)) 
        frame2.create_text(625,90, text = data["title"], font = ('Calibri',15))
        frame2.create_text(625,105, text = data["artist"], font = ('Calibri',15))
        frame2.create_text(625,135, text = data["album"], font = ('Calibri',12))
        frame2.create_text(625,150, text = data["year"], font = ('Calibri',12))
        frame2.create_text(625,165, text = data["sampleRate"], font = ('Calibri',12))
        frame2.create_text(625,180, text = "Stereo", font = ('Calibri',12))
    except: 
        pass

# CANVAS audio 
frame2 = Canvas(tab2)
frame2.create_image(0,0, image = fondo_musica_sub, anchor = 'nw')
frame2.create_text(400,25, text = "REPRODUCTOR DE MÚSICA", font = ('Calibri',28))
frame2.create_text(725,15, text = f"{date:%A, %B %d, %Y}", font = ('Calibri',10))
frame2.create_text(750,30, text = tiemp, font = ('Calibri',10))
frame2.create_text(625,90, text = data["title"], font = ('Calibri',15))
frame2.create_text(625,105, text = data["artist"], font = ('Calibri',15))
frame2.create_text(625,135, text = data["album"], font = ('Calibri',12))
frame2.create_text(625,150, text = data["year"], font = ('Calibri',12))
frame2.create_text(625,165, text = data["sampleRate"], font = ('Calibri',12))
frame2.create_text(625,180, text = "Stereo", font = ('Calibri',12))
frame2.pack(fill = "both", expand = 1)


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

# Song information 
style1 = ttk.Style()
style1.theme_use('clam')
style1.configure("Horizontal.TProgressbar", foreground = 'red', troughcolor = 'DarkOrchid1', bordercolor = '#970BD9', lightcolor = '#970BD9', darkcolor = 'black')

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
        Button_play_pause = Button(frame2, image = play_pause_img, borderwidth = 0, cursor='hand2', command = change_img)
        Button_play_pause.place(x = 405, y = 245)
        imagen = False
        play_pause()
    else:
        play_pause_img = icono_pause_sub
        Button_play_pause = Button(frame2, image = play_pause_img, borderwidth = 0, cursor='hand2', command = change_img)
        Button_play_pause.place(x = 405, y = 245)
        imagen = True
        play_pause()

# Botones para el reproductor de música
Button_repeat = Button(frame2, image = icono_repeat_sub, borderwidth = 0, cursor='hand2', command = rewind)
Button_repeat.place(x = 110, y = 290)
Button_previous = Button(frame2, image = icono_previous_sub, borderwidth = 0, cursor='hand2', command = previous)
Button_previous.place(x = 170, y = 270)
Button_rewind = Button(frame2, image = icono_rewind_sub, borderwidth = 0, cursor='hand2', command = rewind)
Button_rewind.place(x = 270, y = 245)
Button_play_pause = Button(frame2, image = icono_play_sub, borderwidth = 0, cursor='hand2', command = change_img)
Button_play_pause.place(x = 405, y = 245)
Button_next = Button(frame2, image = icono_next_sub, borderwidth = 0, cursor='hand2', command = next)
Button_next.place(x = 540, y = 270)
Button_random = Button(frame2, image = icono_random_sub, borderwidth = 0, cursor='hand2', command = randomorder)
Button_random.place(x = 640, y = 290)


style = ttk.Style()
style.configure("Horizontal.TScale", bordercolor = 'green2', background = 'green2', foreground = 'green2', lightcolor = 'green2', darkcolor = 'black')

boton_global1 = Button(tab2, image = menu_con_fondo_sub, borderwidth = 0, cursor='hand2', command = stop).place(x=10, y=10)

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


boton_global2 = Button(tab3, image = menu_con_fondo_sub, borderwidth = 0, cursor='hand2', command = travel_global).place(x=10, y=10)
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


adelante = Button(tab4, image = adelante_con_fondo_sub, borderwidth = 0, cursor='hand2', command = frontt).place(x=225, y=55)
derecha = Button(tab4, image = derecha_con_fondo_sub, borderwidth = 0, cursor='hand2', command = right).place(x=395, y=135)
izquierda = Button(tab4, image = izquierda_con_fondo_sub, borderwidth = 0, cursor='hand2', command = left).place(x=75, y=135)
reversa = Button(tab4, image = reversa_con_fondo_sub, borderwidth = 0, cursor='hand2', command = backward).place(x=225, y=215)

intermitente = Button(tab4, image = icono_intermitentes_sub, borderwidth = 0, cursor='hand2', command = intermitentes_ligths).place(x=600, y=55)
faros = Button(tab4, image = icono_fog_sub, borderwidth = 0, cursor='hand2', command = fog_ligths).place(x=600, y=200)

boton_global3 = Button(tab4, image = menu_con_fondo_sub, borderwidth = 0, cursor='hand2', command = travel_global).place(x=10, y=10)
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


mensaje_1 = Button(tab5, text= " Mensaje 1 ", borderwidth = 0, cursor='hand2', height="3", width="80",font=('Calibri',10),command = mensaje1).place(x=120, y=80)
mensaje_2 = Button(tab5, text= " Mensaje 2 ", borderwidth = 0, cursor='hand2', height="3", width="80",font=('Calibri',10),command = mensaje2).place(x=120, y=150)
mensaje_3 = Button(tab5, text= " Mensaje 3 ", borderwidth = 0, cursor='hand2', height="3", width="80",font=('Calibri',10),command = mensaje3).place(x=120, y=220)
mensaje_4 = Button(tab5, text= " Mensaje 4 ", borderwidth = 0, cursor='hand2', height="3", width="80",font=('Calibri',10),command = mensaje4).place(x=120, y=290)


boton_global4 = Button(tab5, image = menu_con_fondo_sub, borderwidth = 0, cursor='hand2', command = travel_global).place(x=10, y=10)
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


AlexNu = Button(tab6, text= " Alex N ", borderwidth = 0, cursor='hand2', height="3", width="80",font=('Calibri',10), command = llamada_AlexN).place(x=120, y=80)
AnaP = Button(tab6, text= " Ana P ", borderwidth = 0, cursor='hand2', height="3", width="80",font=('Calibri',10), command = llamada_AnaP).place(x=120, y=150)
Contacto3 = Button(tab6, text= " Contacto 3 ", borderwidth = 0, cursor='hand2', height="3", width="80",font=('Calibri',10)).place(x=120, y=220)
Contacto4 = Button(tab6, text= " Contacto 4 ", borderwidth = 0, cursor='hand2', height="3", width="80",font=('Calibri',10)).place(x=120, y=290)

boton_global5 = Button(tab6, image = menu_con_fondo_sub, borderwidth = 0, cursor='hand2', command = travel_global).place(x=10, y=10)


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

boton_global6 = Button(tab7, image = menu_con_fondo_sub, borderwidth = 0, cursor='hand2', command = travel_global).place(x=10, y=10)
# Create an infinite loop
root.mainloop()