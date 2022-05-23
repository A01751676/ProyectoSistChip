
# IMPORT LIBRARIES AND DEFINITIONS
from tkinter import * # importamos toda la libreria de 'tkinter' 
from SongRI import *

# START TKINTER INTERFACE AND SET GLOBAL VARIABLES
root = Tk()
root.title('Carrito')
root.geometry('800x480')

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

## ---------------------------------------

## MP3 PLAYER COMMANDS TO BUTTONS --------------------------------------------
def updateLabels():
    try:
        SongLabel.config(text = data["title"])
        ArtistLabel.config(text = data["artist"])
        AlbumLabel.config(text = data["album"])
        YearLabel.config(text = data["year"])
        SampleRateLabel.config(text = data["sampleRate"])
    except: 
        pass
    
# PLAY PREVIOUS SONG
def MP3MusicC1():
    global data
    global songIndex
    songIndex, data = playPrevious(songList, songIndex)
    updateLabels()

# PLAY AND PAUSE SONG
def MP3MusicC2():
    global first
    global status    

    if (status):
        pauseSong()
        status = False
    else:
       first = playSong(first)
       status = True
       
# PLAY NEXT SONG
def MP3MusicC3():
    global data
    global songIndex
    songIndex, data = playNext(songList, songIndex)
    updateLabels()
    

## ---------------------------------------------------------------------------

# APLICATION INTERFACE ON TKINTER
# BUTTONS DEFINITION
PlayPrevBoton = Button(root, text = "Previous", padx = 15, pady = 5, command = MP3MusicC1)
PlayPauseBoton = Button(root, text = "Play/Pause", padx = 15, pady = 5, command = MP3MusicC2)
PlayNextBoton = Button(root, text = "Next", padx = 15, pady = 5, command = MP3MusicC3)

# LABELS DEFINITION 
ArtistLabel = Label(root, text = data["artist"])
SongLabel = Label(root, text = data["title"])
AlbumLabel = Label(root, text = data["album"])
YearLabel = Label(root, text = data["year"])
SampleRateLabel = Label(root, text = data["sampleRate"])

# INCLUDE OBJECTS ON INTERFACE
SongLabel.grid(row = 1, column = 2)
ArtistLabel.grid(row = 2, column = 2)
AlbumLabel.grid(row = 3, column = 2)
YearLabel.grid(row = 4, column = 2)
SampleRateLabel.grid(row = 5, column = 2)

PlayPrevBoton.grid(row = 6, column = 1)
PlayPauseBoton.grid(row = 6, column = 2)
PlayNextBoton.grid(row = 6, column = 3)

# APLICATION INFINATE LOOP
root.mainloop()