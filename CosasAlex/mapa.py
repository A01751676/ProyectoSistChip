# Mapa interactivo para el carrito

from tkinter import Button, Label,Tk,filedialog, ttk, Frame, PhotoImage
import pygame
import random
import mutagen


# Start Tkinter for the interface
root = Tk()

# Principal window
root.title('Carrito')     # Define title
root.geometry('800x300')  # configure sice of screen
root.config(bg = 'black')
root.resizable(0,0) 

import folium
from folium import*

popuptext = "<b>Carrito</b>"

Carrito = folium.Map(location = [19.597111,-99.227274], zoom_start = 16, control_scale = True)   #Latitud y Longitud

folium.Marker(location=[19.597111,-99.227274]).add_to(Carrito)       #Agregamos marcador y le indicamos que es de "Carrito"

folium.Circle(location=[19.597111,-99.227274],color="blue", fill_color="red", radius=40, weight=4, fill_opacity=0.2, tooltip="Carrito").add_to(Carrito)

mapa = Label(root, )
mapa.grid(row = 0, column = 0)
Carrito.save('D:\descargas\Trabajos_phyton\Carrito_test.html')


# Create an infinite loop
root.mainloop()