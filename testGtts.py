# -*- coding: utf-8 -*-
"""
Created on Mon May 16 12:26:02 2022

@author: apisl
"""

from gtts import gTTS
from SongRI import *
import time

messageList = ["Hola, ¿Cómo estás?", "¿Dónde es la clase de circuitos?"]

language = 'es'
mesageName = "message.mp3"

myobj = gTTS(text= messageList[0], lang=language, slow=False)
myobj.save(mesageName)
myobj.close()
song = "CancionesSistChip/sound1.mp3"

while True:
    mess = int(input("Leer mensaje 1  == > 1: "))
    if mess  == 1:
        
        # PAUSE AND SAVE SONG INFO
        songPos = getSongPos()
        pauseSong()
        
        # LOAD AND PLAY MASAGE
        loadSong(mesageName)
        playSong(True)
        time.sleep(songPos/1000)
        
        # RESUME SONG
        setSongPosAndPlay(song,songPos)
      
# Playing the converted file
#os.system("start welcome.mp3")
#os.system("start welcome.mp3")
