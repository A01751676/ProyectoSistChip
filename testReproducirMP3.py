# PROYECTO DE IMPLEMENTACION DE SISTEMAS EN CHIP
from pygame import mixer
import os


def leerListaCanciones():
    os.listdir("CancionesSistChip")
    pass
####

mixer.init()
mixer.music.load('CancionesSisTChip\sound1.mp3')
mixer.music.play()

import eyed3
from eyed3 import mp3


## para sacar la info de la cancion
c = eyed3.load("CancionesSisTChip\sound1.mp3")
f = mp3.Mp3AudioFile("CancionesSisTChip\sound1.mp3")


print ("Artista: " + str(c.tag.artist))
print ("Album: " + str(c.tag.album))
print ("Titulo: " + str(c.tag.title))
print ("Year: " + str(c.tag.getBestDate()).split("-")[0])
print ("Frec Muestreo: " + str(f.info.sample_freq))
print ("Bit Rate: " + str(f.info.bit_rate[1]) + " kbps")
print ("Canales: " + str(mixer.get_init()[2]))



##mixer.music.play() # inicia cancion desde el inicio 
##mixer.music.pause() # pausa la cancion
##mixer.music.unpause() # inicia la cancion de donde se quedo
##mixer.music.rewind() # inicio de la cancion
## pygame.mixer.music.queue('welcome.mp3') ## siguiente cancion

# import os 
# os.listdir() # ls
# os.chdir("Humanoides") # cd 