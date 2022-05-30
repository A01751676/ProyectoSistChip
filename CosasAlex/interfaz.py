# Ana Patricia Islas Mainou     A01751676
# Alex Federico Núñez Escobar   A01751559
# Interfaz Gráfica proyecto DISEÑO DE CHIPS

# Using tkinter, firstafull you need to create things and then you show that things

from cgitb import text
from tkinter import *          # importamos toda la libreria de 'tkinter' 
from tkinter import Button, Label,Tk,filedialog, ttk, Frame, PhotoImage
from click import open_file
from gtts import *             # Libreria para convertir texto a audio
import random
import mutagen
# Librerias para mapa -----------------------------
import tkintermapview
# Libreria para musica
from SongRI import *

# Start Tkinter fro the interface
root = Tk()

# Principal window
root.title('Carrito')     # Define title
root.geometry('800x440')  # configure sice of screen
root.config(bg = 'black')
root.resizable(0,0)  

# We include tab panel
nb = ttk.Notebook(root)
nb.pack(pady = 0)

# Colores aleatorios
color1 = ["#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])]
color2 = ["#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])]
color3 = ["#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])]
color4 = ["#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])]

# Fondo Tab
fondo_menu = PhotoImage(file = 'fondo_menu.png')
fondo_musica = PhotoImage(file = 'fondo_musica.png')
fondo_mapa = PhotoImage(file = 'fondo_mapa.png')
fondo_motores = PhotoImage(file = 'fondo_motores.png')
fondo_luces = PhotoImage(file = 'fondo_menu.png')
fondo_telefono = PhotoImage(file = 'fondo_menu.png')
fondo_camara = PhotoImage(file = 'fondo_menu.png')


# Creating tabs
tab1 = Frame(nb, width = 500, height = 500)
tab2 = Frame(nb, width = 500, height = 500)
tab3 = Frame(nb, width = 500, height = 500)
tab4 = Frame(nb, width = 500, height = 500)
tab5 = Frame(nb, width = 500, height = 500)
tab6 = Frame(nb, width = 500, height = 500)
tab7 = Frame(nb, width = 500, height = 500)

# Creamos canvas para fondos
tab1bg = Canvas( tab1, width = 800, height = 700)
tab1bg.place(x = 0, y = 0)
tab1bg.create_image(0,0, image = fondo_menu, anchor = "nw")

# pack Tabs
tab1.pack(fill = "both", expand = 1)
tab2.pack(fill = "both", expand = 1)
tab3.pack(fill = "both", expand = 1)
tab4.pack(fill = "both", expand = 1)
tab5.pack(fill = "both", expand = 1)
tab6.pack(fill = "both", expand = 1)
tab7.pack(fill = "both", expand = 1)



tab2bg = Label( tab2, image = fondo_musica) 
tab2bg.place(x = 0, y = 0) 
tab3bg = Label( tab3, image = fondo_mapa) 
tab3bg.place(x = 0, y = 0) 
tab4bg = Label( tab4, image = fondo_motores) 
tab4bg.place(x = 0, y = 0) 
tab5bg = Label( tab5, image = fondo_luces) 
tab5bg.place(x = 0, y = 0) 
tab6bg = Label( tab6, image = fondo_telefono) 
tab6bg.place(x = 0, y = 0) 
tab7bg = Label( tab7, image = fondo_camara) 
tab7bg.place(x = 0, y = 0) 

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


#Reduce las dimensiones de la imagen en un (ancho_imagen / 2)

# Menu
fondo_menu_sub = fondo_menu.subsample(20)
menu_con_fondo_sub = menu_con_fondo.subsample(32)
menu_sin_fondo_sub = menu_sin_fondo.subsample(20)

# Música
fondo_musica_sub = fondo_musica.subsample(20)
musica_con_fondo_sub = musica_con_fondo.subsample(7)
musica_sin_fondo_sub = musica_sin_fondo.subsample(20)

# Mapa
fondo_mapa_sub = fondo_mapa.subsample(20)
mapa_con_fondo_sub = mapa_con_fondo.subsample(7)
mapa_sin_fondo_sub = mapa_sin_fondo.subsample(20)

# Motores
fondo_motores_sub = fondo_motores.subsample(20)
motores_con_fondo_sub = motores_con_fondo.subsample(7)
motores_sin_fondo_sub = motores_sin_fondo.subsample(20)

# Mensajes
fondo_mensajes_sub = fondo_mensajes.subsample(20)
mensajes_con_fondo_sub = mensajes_con_fondo.subsample(7)
mensajes_sin_fondo_sub = mensajes_sin_fondo.subsample(20)

# Telefono
fondo_telefono_sub = fondo_telefono.subsample(20)
telefono_con_fondo_sub = telefono_con_fondo.subsample(7)
telefono_sin_fondo_sub = telefono_sin_fondo.subsample(20)

# Camara
fondo_camara_sub = fondo_camara.subsample(20)
camara_con_fondo_sub = camara_con_fondo.subsample(7)
camara_sin_fondo_sub = camara_sin_fondo.subsample(20)

# Adding tabs to screen 
nb.add(tab1, image = menu_sin_fondo_sub)
nb.add(tab2, image = musica_sin_fondo_sub)
nb.add(tab3, image = mapa_sin_fondo_sub)
nb.add(tab4, image = motores_sin_fondo_sub)
nb.add(tab5, image = mensajes_sin_fondo_sub)
nb.add(tab6, image = telefono_sin_fondo_sub)
nb.add(tab7, image = camara_sin_fondo_sub)

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

boton_mus = Button(tab1, image = musica_con_fondo_sub, borderwidth = 0 , command = travel_musica).place(x=70, y=20)
boton_mapa = Button(tab1, image = mapa_con_fondo_sub, borderwidth = 0 , command = travel_mapa).place(x=320, y=20)
boton_motor = Button(tab1, image = motores_con_fondo_sub, borderwidth = 0 , command = travel_motor).place(x=570, y=20) 
boton_luces = Button(tab1, image = mensajes_con_fondo_sub, borderwidth = 0 , command = travel_luces).place(x=70, y=200)
boton_telefono = Button(tab1, image = telefono_con_fondo_sub, borderwidth = 0 , command = travel_telefono).place(x=320, y=200)
boton_camara = Button(tab1, image = camara_con_fondo_sub, borderwidth = 0 , command = travel_camara).place(x=570, y=200)








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
songList = randomSongOrder(songList)
songIndex = 0
status = False # status 0 => pause, 1 => play

# INITIATE MP3 OBJETCT WITH FIRST SONG
initMP3Player()
data = loadSong(songList [songIndex])

def open_file():
    global direction, pos, n, actual_song
    pos = 0
    n = 0
    direction = filedialog.askopenfilenames(initialdir = '/', title = 'Choose the song', filetype = (('mp3 files', '*.mp3'),('All files', '*.*')))

    n = len(direction)
    actual_song = direction[pos]

    song_name = actual_song.split('/')
    song_name = song_name[-1]

lista = []
for i in range (50,200,10):
    lista.append(i)

def start_playback():
    global actual_song, direction, pos, n, actualizar 
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

    actual_song = direction[pos]
    song_name = actual_song.split('/')
    song_name = song_name[-1]
    name['text'] = song_name

    time = pygame.mixer.music.get_pos()
    x = int(int(time)*0.001)
    tiempo['value'] = x

    y = float(int(volumen.get())*0.1)
    pygame.mixer.music.set_volume(y)
    level['text'] = int(y*100)

    audio = mutagen.File(actual_song)
    log = audio.info.length
    minutes, seconds = divmod(log, 60)

    minutes, seconds = int(minutes), int (seconds)
    tt = minutes * 60 + seconds
    tiempo['maximum'] = tt      # time of song
    texto['text'] = str(minutes) + ":" + str(seconds)

    actualizar = tab2.after(100, start_playback)

    if (x == tt):
        tab2.after_cancel(actualizar)
        texto['text'] = "00:00"
        stop_effect()

        if (pos != n):
            pos = pos + 1
            tab2.after(100, start_playback)
            pygame.mixer.music.play()

        if (pos == n):
            pos = 0   


def play():
    global actual_song

    pygame.mixer.music.load(actual_song)
    pygame.mixer.music.play()
    start_playback()

def previous():
    global pos, n

    if (pos > 0):
        pos = pos - 1
    else:
        pos = 0

    amount['text'] = str(pos) + '/' + str(n)

def next():
    global pos, n

    if (pos == n - 1):
        pos = 0
    else: 
        pos = pos + 1
    
    amount['text'] = str(pos) + '/' + str(n)

def stop_effect():
    bar1['value'] = 20
    bar2['value'] = 30
    bar3['value'] = 40
    bar4['value'] = 50
    bar5['value'] = 60
    bar6['value'] = 70
    bar7['value'] = 60
    bar8['value'] = 50
    bar9['value'] = 60
    bar10['value'] = 70
    bar11['value'] = 50
    bar12['value'] = 60
    bar13['value'] = 50
    bar14['value'] = 40
    bar15['value'] = 50
    bar16['value'] = 60
    bar17['value'] = 70
    bar18['value'] = 60
    bar19['value'] = 50
    bar20['value'] = 40

def stop():
    global actualizar
    pygame.mixer.music.stop()
    tab2.after_cancel(actualizar)
    stop_effect()

def pause():
    global actualizar
    pygame.mixer.music.pause()
    tab2.after_cancel(actualizar)
    stop_effect()

def continuar():
    pygame.mixer.music.unpause()
    tab2.after(100, start_playback)

# estyle
estilo = ttk.Style()
estilo.theme_use('clam')
estilo.configure("Vertical.TProgressbar", foreground = color1, background = color2, lightcolor = color3, darkcolor = color4)

# Bar Frames
frame1 = Frame(tab2, width = 800, height = 440)
frame1.place(x=0, y=0)
frame2 = Frame(tab2, width = 800, height = 440)
frame2.place(x=0, y=0)

# Bars
bar1 = ttk.Progressbar(tab2, orient = 'vertical', length = 150, maximum = 300, style = 'Vertical.TProgressbar')
bar1.place(x=50, y=50)
bar2 = ttk.Progressbar(tab2, orient = 'vertical', length = 150, maximum = 300, style = 'Vertical.TProgressbar')
bar2.place(x=70, y=50)
bar3 = ttk.Progressbar(tab2, orient = 'vertical', length = 150, maximum = 300, style = 'Vertical.TProgressbar')
bar3.place(x=90, y=50)
bar4 = ttk.Progressbar(tab2, orient = 'vertical', length = 150, maximum = 300, style = 'Vertical.TProgressbar')
bar4.place(x=110, y=50)
bar5 = ttk.Progressbar(tab2, orient = 'vertical', length = 150, maximum = 300, style = 'Vertical.TProgressbar')
bar5.place(x=130, y=50)
bar6 = ttk.Progressbar(tab2, orient = 'vertical', length = 150, maximum = 300, style = 'Vertical.TProgressbar')
bar6.place(x=150, y=50)
bar7 = ttk.Progressbar(tab2, orient = 'vertical', length = 150, maximum = 300, style = 'Vertical.TProgressbar')
bar7.place(x=170, y=50)
bar8 = ttk.Progressbar(tab2, orient = 'vertical', length = 150, maximum = 300, style = 'Vertical.TProgressbar')
bar8.place(x=190, y=50)
bar9 = ttk.Progressbar(tab2, orient = 'vertical', length = 150, maximum = 300, style = 'Vertical.TProgressbar')
bar9.place(x=210, y=50)
bar10 = ttk.Progressbar(tab2, orient = 'vertical', length = 150, maximum = 300, style = 'Vertical.TProgressbar')
bar10.place(x=230, y=50)
bar11 = ttk.Progressbar(tab2, orient = 'vertical', length = 150, maximum = 300, style = 'Vertical.TProgressbar')
bar11.place(x=250, y=50)
bar12 = ttk.Progressbar(tab2, orient = 'vertical', length = 150, maximum = 300, style = 'Vertical.TProgressbar')
bar12.place(x=270, y=50)
bar13 = ttk.Progressbar(tab2, orient = 'vertical', length = 150, maximum = 300, style = 'Vertical.TProgressbar')
bar13.place(x=290, y=50)
bar14 = ttk.Progressbar(tab2, orient = 'vertical', length = 150, maximum = 300, style = 'Vertical.TProgressbar')
bar14.place(x=310, y=50)
bar15 = ttk.Progressbar(tab2, orient = 'vertical', length = 150, maximum = 300, style = 'Vertical.TProgressbar')
bar15.place(x=330, y=50)
bar16 = ttk.Progressbar(tab2, orient = 'vertical', length = 150, maximum = 300, style = 'Vertical.TProgressbar')
bar16.place(x=350, y=50)
bar17 = ttk.Progressbar(tab2, orient = 'vertical', length = 150, maximum = 300, style = 'Vertical.TProgressbar')
bar17.place(x=370, y = 50)
bar18 = ttk.Progressbar(tab2, orient = 'vertical', length = 150, maximum = 300, style = 'Vertical.TProgressbar')
bar18.place(x=390, y=50)
bar19 = ttk.Progressbar(tab2, orient = 'vertical', length = 150, maximum = 300, style = 'Vertical.TProgressbar')
bar19.place(x=410, y=50)
bar20 = ttk.Progressbar(tab2, orient = 'vertical', length = 150, maximum = 300, style = 'Vertical.TProgressbar')
bar20.place(x=430, y=50)
# Song information 

style1 = ttk.Style()
style1.theme_use('clam')
style1.configure("Horizontal.TProgressbar", foreground = 'red', troughcolor = 'DarkOrchid1', bordercolor = '#970BD9', lightcolor = '#970BD9', darkcolor = 'black')

tiempo = ttk.Progressbar(frame2, orient = 'horizontal', length = 390, mode = 'determinate',style="Horizontal.TProgressbar")
tiempo.place(x = 50, y = 230)
texto = Label(frame2, fg ='green2', width = 5)
texto.place(x = 440, y = 230)

name = Label(frame2, fg = 'red', width = 55)
name.place(x = 60, y = 210)
amount = Label(frame2, fg = 'green2')
amount.place(x = 120, y = 200)

# Imágenes para el reproductor de música
icono_previous = PhotoImage(file = 'icono_previous.png')     # previous
icono_play = PhotoImage(file = 'icono_play.png')         # play
icono_pause = PhotoImage(file = 'icono_pause.png')        # pause
icono_next = PhotoImage(file = 'icono_next.png')         # next
icono_random = PhotoImage(file = 'icono_next.png')       # random



#Reduce las dimensiones de la imagen en un (ancho_imagen / 2)
icono_previous_sub = icono_previous.subsample(20)
icono_play_sub = icono_play.subsample(20)
icono_pause_sub = icono_pause.subsample(20)
icono_next_sub = icono_next.subsample(20)
icono_random_sub = icono_random.subsample(20)


# Botones para el reproductor de música
Button_previous = Button(frame2, image = icono_previous_sub, borderwidth = 0, bg = 'white', command = previous)
Button_previous.place(x = 30, y = 280)
Button_play = Button(frame2, image = icono_play_sub, borderwidth = 0, bg = 'white', command = play)
Button_play.place(x = 100, y = 280)
Button_pause = Button(frame2, image = icono_pause_sub, borderwidth = 0, bg = 'white', command = pause)
Button_pause.place(x = 170, y = 280)
Button_next = Button(frame2, image = icono_next_sub, borderwidth = 0, bg = 'white', command = next)
Button_next.place(x = 240, y = 280)
Button_random = Button(frame2, image = icono_random_sub, borderwidth = 0, bg = 'white', command = randomm)
Button_random.place(x = 310, y = 280)

volumen = ttk.Scale(frame2, to = 10, from_ = 0, orient = 'horizontal', length = 90, style = 'Horizontal.TScale')
volumen.place(x = 480, y = 210)

style = ttk.Style()
style.configure("Horizontal.TScale", bordercolor = 'green2', background = 'green2', foreground = 'green2', lightcolor = 'green2', darkcolor = 'black')

level = Label(frame2, fg = 'green2', width = 3)
level.place(x = 450, y = 210)

# LABELS DEFINITION 
ArtistLabel = Label(tab2, text = data["artist"])
SongLabel = Label(tab2, text = data["title"])
AlbumLabel = Label(tab2, text = data["album"])
YearLabel = Label(tab2, text = data["year"])
SampleRateLabel = Label(tab2, text = data["sampleRate"])

# INCLUDE OBJECTS ON INTERFACE
SongLabel.place(x = 450, y = 100)
ArtistLabel.place(x = 450, y = 150)
AlbumLabel.place(x = 450, y = 200)
YearLabel.place(x = 450, y = 250)
SampleRateLabel.place(x = 450, y = 300)


boton_global1 = Button(tab2, image = menu_con_fondo_sub, borderwidth = 0, command = travel_global).place(x=10, y=10)

# Components of TAB3 -------------------------------------------------------------------------------------
# Mapa ---------------------------------------------------------------------------------------------------

frame_map = LabelFrame(tab3)
#frame_map.pack(padx = 20, pady = 20)
frame_map.place(x = 60, y = 10)

map_widget = tkintermapview.TkinterMapView(frame_map, width = 700, height = 340, corner_radius = 0)
map_widget.set_position(19.597111,-99.227274)
map_widget.set_zoom(16)

# Marker
marker_1 = map_widget.set_marker(19.597111,-99.227274, text="Carrito")

map_widget.pack()


boton_global2 = Button(tab3, image = menu_con_fondo_sub, borderwidth = 0, command = travel_global).place(x=10, y=10)
# Components of TAB4 -------------------------------------------------------------------------------------
# MOTOR --------------------------------------------------------------------------------------------------

# Imágenes para el motor
adelante_con_fondo = PhotoImage(file = 'musica_con_fondo.png')       # adelante
reversa_con_fondo = PhotoImage(file = 'musica_con_fondo.png')        # reversa
derecha_con_fondo = PhotoImage(file = 'musica_con_fondo.png')        # derecha
izquierda_con_fondo = PhotoImage(file = 'musica_con_fondo.png')      # izquierda
front_con_fondo = PhotoImage(file = 'musica_con_fondo.png')          # Delante
back_con_fondo = PhotoImage(file = 'musica_con_fondo.png')           # Reversa
stopp_con_fondo = PhotoImage(file = 'musica_con_fondo.png')          # Parking
right_con_fondo = PhotoImage(file = 'musica_con_fondo.png')          # Derecha
left_con_fondo = PhotoImage(file = 'musica_con_fondo.png')           # Izquierda

#Reduce las dimensiones de la imagen en un (ancho_imagen / 2)
adelante_con_fondo_sub = adelante_con_fondo.subsample(20)
reversa_con_fondo_sub = reversa_con_fondo.subsample(20)
derecha_con_fondo_sub = derecha_con_fondo.subsample(20)
izquierda_con_fondo_sub = izquierda_con_fondo.subsample(20)
front_con_fondo_sub = front_con_fondo.subsample(20)
back_con_fondo_sub = back_con_fondo.subsample(20)
stopp_con_fondo_sub = stopp_con_fondo.subsample(20)
right_con_fondo_sub = right_con_fondo.subsample(20)
left_con_fondo_sub = left_con_fondo.subsample(20)

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

if (velocidad == 0):
    print("stop")
elif(velocidad == 1):
    print("stop")
elif(velocidad == 2):
    print("stop")
elif(velocidad == 3):
    print("stop")
elif(velocidad == 4):
    print("stop")

adelante = Button(tab4, image = adelante_con_fondo_sub, borderwidth = 0, command = frontt).place(x=175, y=50)
derecha = Button(tab4, image = derecha_con_fondo_sub, borderwidth = 0, command = right).place(x=300, y=150)
izquierda = Button(tab4, image = izquierda_con_fondo_sub, borderwidth = 0, command = left).place(x=50, y=150)
reversa = Button(tab4, image = reversa_con_fondo_sub, borderwidth = 0, command = backward).place(x=175, y=250)

boton_global3 = Button(tab4, image = menu_con_fondo_sub, borderwidth = 0, command = travel_global).place(x=10, y=10)
# Components of TAB5 -------------------------------------------------------------------------------------
# LUCES --------------------------------------------------------------------------------------------------

boton_global4 = Button(tab5, image = menu_con_fondo_sub, borderwidth = 0, command = travel_global).place(x=10, y=10)
# Components of TAB6 -------------------------------------------------------------------------------------
# TELEFONO -----------------------------------------------------------------------------------------------

boton_global5 = Button(tab6, image = menu_con_fondo_sub, borderwidth = 0, command = travel_global).place(x=10, y=10)
# Components of TAB7 -------------------------------------------------------------------------------------
# CAMARA -------------------------------------------------------------------------------------------------

boton_global6 = Button(tab7, image = menu_con_fondo_sub, borderwidth = 0, command = travel_global).place(x=10, y=10)





# Create an infinite loop
root.mainloop()