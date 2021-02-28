import os
import playsound
from gtts import gTTS
from my_voice import speak
from voice_bot import bot,voice_bot
# main
while True:
    you = speak()
    you = you.lower()
    bot(you) 