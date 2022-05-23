# -*- coding: utf-8 -*-
"""
Created on Mon May 16 12:26:02 2022

@author: apisl
"""


# Import the required module for text 
# to speech conversion
from gtts import gTTS
  
# This module is imported so that we can 
# play the converted audio
import os
  
# The text that you want to convert to audio
mytext = 'Hola Dofsi, te quiero wilis'
  
# Language in which you want to convert
language = 'es'
  
# Passing the text and language to the engine, 
# here we have marked slow=False. Which tells 
# the module that the converted audio should 
# have a high speed
myobj = gTTS(text=mytext, lang=language, slow=False)
  
# Saving the converted audio in a mp3 file named
# welcome 
myobj.save("welcom2.mp3")
  
# Playing the converted file
#os.system("start welcome.mp3")
#os.system("start welcome.mp3")
