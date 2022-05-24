# Ana Patricia Islas Mainou     A01751676
# Alex Federico Núñez Escobar   A01751559
# Interfaz Gráfica proyecto DISEÑO DE CHIPS

# Using tkinter, firstafull you need to create things and then you show that things

from cgitb import text
from tkinter import *       # importamos toda la libreria de 'tkinter' 
from tkinter import Button, Label,Tk,filedialog, ttk, Frame, PhotoImage
from click import open_file
import pygame               # Libreria para reproducir música
from gtts import *          # Libreria para convertir texto a audio
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

boton_mus = Button(tab1, image = musica, command = travel_musica). pack(padx = 10,pady = 10)
boton_mapa = Button(tab1, image = mapa, command = travel_mapa). pack(padx = 30,pady = 10)
boton_motor = Button(tab1, image = motor, command = travel_motor). pack(padx = 50,pady = 10) 
boton_luces = Button(tab1, image = luces, command = travel_luces). pack(padx = 70,pady = 10)
boton_telefono = Button(tab1, image = telefono, command = travel_telefono). pack(padx = 90,pady = 10)
boton_camara = Button(tab1, image = camara, command = travel_camara). pack(padx = 110,pady = 10) 

# Components of TAB2 -------------------------------------------------------------------------------------
boton_global1 = Button(tab2, image = musica, command = travel_global). pack(padx = 10,pady = 10)



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