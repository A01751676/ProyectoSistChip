# Mapa interactivo para el carrito

import folium
from folium.plugins import minimap

popuptext = "<b>Carrito</b>"

Carrito = folium.Map(location = [19.597111,-99.227274], zoom_start = 16, control_scale = True)   #Latitud y Longitud

folium.Marker(location=[19.597111,-99.227274]).add_to(Carrito)       #Agregamos marcador y le indicamos que es de "Carrito"

folium.Circle(location=[19.597111,-99.227274],color="blue", fill_color="red", radius=40, weight=4, fill_opacity=0.2, tooltip="Carrito").add_to(Carrito)

Carrito
Carrito.save('D:\descargas\Trabajos_phyton\Carrito_test.html')