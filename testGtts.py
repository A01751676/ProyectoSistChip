# -*- coding: utf-8 -*-
"""
Created on Mon May 16 12:26:02 2022

@author: apisl
"""

from gtts import gTTS
from SongRI import *
import time
import os
from mutagen.mp3 import MP3

messageList = ["Hola, ¿Cómo estás?", "¿Dónde es la clase de circuitos?"]

language = 'es'
mesageName = "MensajesMP3/message.mp3"

myobj = gTTS(text= messageList[0], lang=language, slow=False)
myobj.save(mesageName)

first = True
songList = getSongList()
songList = randomSongOrder(songList)
songIndex = 0

# Iniciar MP3 Player
initMP3Player()
data = loadSong("CancionesSistChip\sound1.mp3")

## Primera cancion
first = playSong(first)
print(data)

def readMessage():
    # PAUSE AND SAVE SONG INFO
    songPos = 0
    pauseSong()
    songPos = (getSongPos())/1000
    print(songPos)
    songPos = songPos
    print(songPos)
    #pauseSong()
    os.chdir("..")
    
    # LOAD AND PLAY MASAGE
    mixer.music.load(mesageName)
    audio = MP3(mesageName)
    
    mesageDuration = audio.info.length
    print(audio.info.length)
    
    playSong(True)
    time.sleep(mesageDuration)
    
    # RESUME SONG
    os.chdir("CancionesSistChip")
    print(songPos)
    setSongPosAndPlay(songList[songIndex],songPos)
    
while True:
    mess = int(input("Leer mensaje 1  == > 1: "))
    if mess == 0:
        break
    
    if mess  == 1:
        readMessage()
      
