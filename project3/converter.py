#Youtube video to mp converter
from pytube import YouTube
from moviepy.editor import *
"""
Import the OS module used to modify or delete a file 
(in this we will need to delete the mp4 file since I only want the mp3 file) and we also import the shutil module to copy the file to the destination
"""
import os, shutil


#Inserting the youtube link to convert
link = str(input("Insert a Youtube link:"))
print("Converting...")
#Converting video file to audio file
mp4 = YouTube(link).streams.get_highest_resolution().download()
mp3 = mp4.split(".mp4", 1)[0] + f".mp3"

file_video = VideoFileClip(mp4)
file_audio = file_video.audio
file_audio.write_audiofile(mp3)

file_audio.close()
file_video.close()
#We insert where we want to save the audio file
destination = "/home/niccolo/Audio"
os.remove(mp4)
#We move the mp3 file to the folder we want and delete it from this
shutil.copy(mp3, destination)
os.remove(mp3)


