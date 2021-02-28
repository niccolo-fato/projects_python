import os
import playsound
from gtts import gTTS
from random import randrange
import time
def voice_bot(greetings_out):
    print("Bot:", greetings_out)
    tts = gTTS(text=greetings_out, lang='it')
    filename = "voice.mp3"
    if os.path.exists(filename):
        os.remove(filename)
    tts.save(filename)
    playsound.playsound(filename)
def bot(you):
    if "ciao" in you:
        voice_bot("ciao fato")