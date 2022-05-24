# Ana Patricia Islas Mainou     A01751676
# Alex Federico Núñez Escobar   A01751559
# Interfaz Gráfica proyecto DISEÑO DE CHIPS

# Using tkinter, firstafull you need to create things and then you show that things

from cgitb import text
from tkinter import *          # importamos toda la libreria de 'tkinter' 
from tkinter import Button, Label,Tk,filedialog, ttk, Frame, PhotoImage
from click import open_file
import pygame                  # Libreria para reproducir música
from gtts import *             # Libreria para convertir texto a audio
import random
import mutagen


# Start Tkinter fro the interface
root = Tk()

# Principal window
root.title('Carrito')     # Define title
root.geometry('800x480')  # configure sice of screen
root.config(bg = 'black')
root.resizable(0,0)  

# We include tab panel
nb = ttk.Notebook(root)
nb.pack(pady = 15)

# Creating tabs
tab1 = Frame(nb, width = 500, height = 500, bg = 'blue')
tab2 = Frame(nb, width = 500, height = 500, bg = 'red')
tab3 = Frame(nb, width = 500, height = 500, bg = 'grey')
tab4 = Frame(nb, width = 500, height = 500, bg = 'yellow')
tab5 = Frame(nb, width = 500, height = 500, bg = 'orange')
tab6 = Frame(nb, width = 500, height = 500, bg = 'white')
tab7 = Frame(nb, width = 500, height = 500, bg = 'black')

# pack Tabs
tab1.pack(fill = "both", expand = 1)
tab2.pack(fill = "both", expand = 1)
tab3.pack(fill = "both", expand = 1)
tab4.pack(fill = "both", expand = 1)
tab5.pack(fill = "both", expand = 1)
tab6.pack(fill = "both", expand = 1)
tab7.pack(fill = "both", expand = 1)

# Images for tabs
globa = PhotoImage(file = 'file.png')
musica = PhotoImage(file = 'file.png')
mapa = PhotoImage(file = 'play.png')
motor = PhotoImage(file = 'unpause.png')
luces = PhotoImage(file = 'pause.png')
telefono = PhotoImage(file = 'continue.png')
camara = PhotoImage(file = 'backward.png')

# Adding tabs to screen 
nb.add(tab1, image = globa)
nb.add(tab2, image = musica)
nb.add(tab3, image = mapa)
nb.add(tab4, image = motor)
nb.add(tab5, image = luces)
nb.add(tab6, image = telefono)
nb.add(tab7, image = camara)

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

def travel_musica():
    global status_musica    
    if (status_musica == False):
        nb.add(tab2, image = musica)
        nb.select(1)

def travel_mapa():
    global status_mapa    
    if (status_mapa == False):
        nb.add(tab3, image = mapa)
        nb.select(2)

def travel_motor():
    global status_motor    
    if (status_motor == False):
        nb.add(tab4, image = motor)
        nb.select(3)

def travel_luces():
    global status_luces    
    if (status_luces == False):
        nb.add(tab5, image = luces)
        nb.select(4)

def travel_telefono():
    global status_telefono    
    if (status_telefono == False):
        nb.add(tab6, image = telefono)
        nb.select(5)

def travel_camara():
    global status_camara    
    if (status_camara == False):
        nb.add(tab7, image = camara)
        nb.select(6)

boton_mus = Button(tab1, image = musica, command = travel_musica).place(x=200, y=70)
boton_mapa = Button(tab1, image = mapa, command = travel_mapa).place(x=600, y=70)
boton_motor = Button(tab1, image = motor, command = travel_motor).place(x=200, y=190) 
boton_luces = Button(tab1, image = luces, command = travel_luces).place(x=600, y=190)
boton_telefono = Button(tab1, image = telefono, command = travel_telefono).place(x=200, y=310)
boton_camara = Button(tab1, image = camara, command = travel_camara).place(x=600, y=310)








# Components of TAB2 -------------------------------------------------------------------------------------

pygame.mixer.init()
pygame.mixer.init(frequency = 44100)
actual_song = ''
direction = ''

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


def start():
    global actual_song

    pygame.mixer.music.load(actual_song)
    pygame.mixer.music.play()
    start_playback()

def backward():
    global pos, n

    if (pos > 0):
        pos = pos - 1
    else:
        pos = 0

    amount['text'] = str(pos) + '/' + str(n)

def forward():
    global pos, n

    if (pos == n - 1):
        pos = 0
    else: 
        pos = pos + 1
    
    amount['text'] = str(pos) + '/' + str(n)

def stop_effect():
    bar1['value'] = 50
    bar2['value'] = 60
    bar3['value'] = 70
    bar4['value'] = 80
    bar5['value'] = 90
    bar6['value'] = 100
    bar7['value'] = 90
    bar8['value'] = 80
    bar9['value'] = 70
    bar10['value'] = 60
    bar11['value'] = 60
    bar12['value'] = 70
    bar13['value'] = 80
    bar14['value'] = 90
    bar15['value'] = 100
    bar16['value'] = 90
    bar17['value'] = 80
    bar18['value'] = 70
    bar19['value'] = 60
    bar20['value'] = 50

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

# Colores aleatorios
color1 = ["#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])]
color2 = ["#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])]
color3 = ["#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])]
color4 = ["#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])]

# estyle
estilo = ttk.Style()
estilo.theme_use('clam')
estilo.configure("Vertical.TProgressbar", foreground = color1, background = color2,troughcolor = 'black', bordercolor = 'black', lightcolor = color3, darkcolor = color4)

# Bar Frames
frame1 = Frame(tab2, bg = 'black', width = 800, height = 440)
frame1.place(x=0, y=0)
frame2 = Frame(tab2, bg = 'black', width = 800, height = 440)
frame2.place(x=0, y=0)

# Bars
bar1 = ttk.Progressbar(frame1, orient = 'vertical', length = 200, maximum = 300, style = 'Vertical.TProgressbar')
bar1.place(x=20, y=70)
bar2 = ttk.Progressbar(frame1, orient = 'vertical', length = 200, maximum = 300, style = 'Vertical.TProgressbar')
bar2.place(x=25, y=70)
bar3 = ttk.Progressbar(frame1, orient = 'vertical', length = 200, maximum = 300, style = 'Vertical.TProgressbar')
bar3.place(x=30, y=70)
bar4 = ttk.Progressbar(frame1, orient = 'vertical', length = 200, maximum = 200, style = 'Vertical.TProgressbar')
bar4.place(x=35, y=70)
bar5 = ttk.Progressbar(frame1, orient = 'vertical', length = 200, maximum = 200, style = 'Vertical.TProgressbar')
bar5.place(x=40, y=70)
bar6 = ttk.Progressbar(frame1, orient = 'vertical', length = 200, maximum = 200, style = 'Vertical.TProgressbar')
bar6.place(x=45, y=70)
bar7 = ttk.Progressbar(frame1, orient = 'vertical', length = 200, maximum = 200, style = 'Vertical.TProgressbar')
bar7.place(x=50, y=70)
bar8 = ttk.Progressbar(frame1, orient = 'vertical', length = 200, maximum = 200, style = 'Vertical.TProgressbar')
bar8.place(x=55, y=70)
bar9 = ttk.Progressbar(frame1, orient = 'vertical', length = 200, maximum = 200, style = 'Vertical.TProgressbar')
bar9.place(x=60, y=70)
bar10 = ttk.Progressbar(frame1, orient = 'vertical', length = 200, maximum = 200, style = 'Vertical.TProgressbar')
bar10.place(x=65, y=70)
bar11 = ttk.Progressbar(frame1, orient = 'vertical', length = 200, maximum = 200, style = 'Vertical.TProgressbar')
bar11.place(x=70, y=70)
bar12 = ttk.Progressbar(frame1, orient = 'vertical', length = 200, maximum = 200, style = 'Vertical.TProgressbar')
bar12.place(x=75, y=70)
bar13 = ttk.Progressbar(frame1, orient = 'vertical', length = 200, maximum = 200, style = 'Vertical.TProgressbar')
bar13.place(x=80, y=70)
bar14 = ttk.Progressbar(frame1, orient = 'vertical', length = 200, maximum = 200, style = 'Vertical.TProgressbar')
bar14.place(x=85, y=70)
bar15 = ttk.Progressbar(frame1, orient = 'vertical', length = 200, maximum = 200, style = 'Vertical.TProgressbar')
bar15.place(x=90, y=70)
bar16 = ttk.Progressbar(frame1, orient = 'vertical', length = 200, maximum = 200, style = 'Vertical.TProgressbar')
bar16.place(x=95, y=70)
bar17 = ttk.Progressbar(frame1, orient = 'vertical', length = 200, maximum = 200, style = 'Vertical.TProgressbar')
bar17.place(x=100, y=70)
bar18 = ttk.Progressbar(frame1, orient = 'vertical', length = 200, maximum = 200, style = 'Vertical.TProgressbar')
bar18.place(x=105, y=70)
bar19 = ttk.Progressbar(frame1, orient = 'vertical', length = 200, maximum = 200, style = 'Vertical.TProgressbar')
bar19.place(x=110, y=70)
bar20 = ttk.Progressbar(frame1, orient = 'vertical', length = 200, maximum = 200, style = 'Vertical.TProgressbar')
bar20.place(x=115, y=70)

# Song information 

style1 = ttk.Style()
style1.theme_use('clam')
style1.configure("Horizontal.TProgressbar", foreground = 'red', background = 'black', troughcolor = 'DarkOrchid1', bordercolor = '#970BD9', lightcolor = '#970BD9', darkcolor = 'black')

tiempo = ttk.Progressbar(frame2, orient = 'horizontal', length = 390, mode = 'determinate',style="Horizontal.TProgressbar")
tiempo.place(x = 120, y = 90)
texto = Label(frame2, bg ='black', fg ='green2', width = 5)
texto.place(x = 125, y = 90)

name = Label(frame2, bg = 'black', fg = 'red', width = 55)
name.place(x = 80, y = 90)
amount = Label(frame2, bg = 'black', fg = 'green2')
amount.place(x = 120, y = 70)

image1 = PhotoImage(file = 'file.png')
image2 = PhotoImage(file = 'play.png')
image3 = PhotoImage(file = 'unpause.png')
image4 = PhotoImage(file = 'pause.png')
image5 = PhotoImage(file = 'continue.png')
image6 = PhotoImage(file = 'backward.png')
image7 = PhotoImage(file = 'forward.png')

Button_open_file = Button(frame2, image = image1, bg = color1, command = open_file)
Button_open_file.place(x = 20, y = 400)
Button_start = Button(frame2, image = image2, bg = color2, command = start)
Button_start.place(x = 40, y = 400)
Button_stop = Button(frame2, image = image3, bg = color3, command = stop)
Button_stop.place(x = 60, y = 400)
Button_pause = Button(frame2, image = image4, bg = color4, command = pause)
Button_pause.place(x = 80, y = 400)
Button_continue = Button(frame2, image = image5, bg = color3, command = continuar)
Button_continue.place(x = 100, y = 400)
Button_backward = Button(frame2, image = image6, bg = color2, command = backward)
Button_backward.place(x = 120, y = 400)
Button_forward = Button(frame2, image = image7, bg = color1, command = forward)
Button_forward.place(x = 140, y = 400)

volumen = ttk.Scale(frame2, to = 10, from_ = 0, orient = 'horizontal', length = 90, style = 'Horizontal.TScale')
volumen.place(x = 160, y = 90)

style = ttk.Style()
style.configure("Horizontal.TScale", bordercolor = 'green2', troughcolor = 'black', background = 'green2', foreground = 'green2', lightcolor = 'green2', darkcolor = 'black')

level = Label(frame2, bg = 'black', fg = 'green2', width = 3)
level.place(x = 180, y = 90)



boton_global1 = Button(tab2, image = musica, command = travel_global).place(x=10, y=10)

# Components of TAB3 -------------------------------------------------------------------------------------
boton_global2 = Button(tab3, image = musica, command = travel_global). pack(padx = 10,pady = 10)



# Components of TAB4 -------------------------------------------------------------------------------------
boton_global3 = Button(tab4, image = musica, command = travel_global). pack(padx = 10,pady = 10)



# Components of TAB5 -------------------------------------------------------------------------------------
boton_global4 = Button(tab5, image = musica, command = travel_global). pack(padx = 10,pady = 10)



# Components of TAB6 -------------------------------------------------------------------------------------
boton_global5 = Button(tab6, image = musica, command = travel_global). pack(padx = 10,pady = 10)



# Components of TAB7 -------------------------------------------------------------------------------------
boton_global6 = Button(tab7, image = musica, command = travel_global). pack(padx = 10,pady = 10)





# Create an infinite loop
root.mainloop()