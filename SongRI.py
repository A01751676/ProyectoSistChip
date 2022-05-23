# BACKEND MUSIC REPRODUCTION AND INFORMATION

import os
from pygame import mixer
import eyed3
from eyed3 import mp3
import random
from mutagen.mp3 import MP3


def getSongList():
    """
    GENERATES THE SONG LIST TO REPRODUCE

    Returns
    -------
    LIST
        SONG LIST.

    """
    path = "C:/Users/apisl/OneDrive/Escritorio/CancionesSistChip"
    os.chdir(path)
    return os.listdir()

def getSongData(song):
    """
    GETS SONG METADATA

    Parameters
    ----------
    song : MP3 FILE
        SONG FILE

    Returns
    -------
    songData : DICT
        DICTIONARY WITH METADATA.

    """
    s1 = eyed3.load(song)
    s2 = mp3.Mp3AudioFile(song)
    songData = {
        "artist" : str(s1.tag.artist),
        "album" :str(s1.tag.album),
        "title" : str(s1.tag.title),
        "year" : str(s1.tag.getBestDate()).split("-")[0],
        "sampleRate" : str(s2.info.sample_freq) + " kbps"
        }
    
    return songData
    
def randomSongOrder(songList):
    """
    GENERATE RANDOM ORDER FOR SONGS

    Parameters
    ----------
    songList : LIST
        ORIGINAL ORDERED SONG LIST.

    Returns
    -------
    LIST
        RANDOMED SONG LIST.

    """
    return random.sample(songList, len(songList))

def initMP3Player():
    """
    INITIATES MP3 PLAYER WITH PYGAME

    Returns
    -------
    None.

    """
    mixer.init()
    
def loadSong(song):
    """
    LOADS SONG TO MIXER TO REPRODUCE

    Parameters
    ----------
    song : MP3 FILE
        SONG TO BE PLAYED.

    Returns
    -------
    DICT
        SONG METADATA.

    """
    mixer.music.load(song)
    return getSongData(song)

def playSong(first):

    if (first):
        mixer.music.play()
    else:
        mixer.music.unpause()
    return False

def pauseSong():
    """
    PAUSE SONG

    Returns
    -------
    None.

    """
    mixer.music.pause()
    
def playPrevious(songList, index):

    mixer.music.stop()
    newIndex = index-1
    
    if (newIndex != -1):
        data = loadSong(songList[newIndex])
        mixer.music.play()
        return newIndex, data
    
    else:
        mixer.music.play()
        return index, None
    
def playNext(songList, index):

    mixer.music.stop()
    newIndex = index+1
    
    if (newIndex < len(songList)):
        data = loadSong(songList[newIndex])
        mixer.music.play()
        return newIndex, data
    
    else:
        mixer.music.play()
        return index, None

def knowSongEnd():
    songEnd = mixer.music.get_pos()
    
    if (songEnd == -1):
        return True
    else:
        return False


