# -*- coding: utf-8 -*-
"""
Created on Sun May 22 12:31:18 2022

@author: apisl
"""

from SongRI import *
## --------------------------------------

first = True
songList = getSongList()
songList = randomSongOrder(songList)
songIndex = 0

# Iniciar MP3 Player
initMP3Player()
data = loadSong(songList [songIndex])

## Primera cancion
first = playSong(first)
print(data)

"""
while (True):

    # MONITOR SONG END
    if (knowSongEnd()):
        songIndex = playNext(songList, songIndex)
        
  """  