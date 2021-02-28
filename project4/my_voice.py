import speech_recognition as sr
from voice_bot import voice_bot
def speak():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        text = ""
    try:
        voice_bot("Sto ascoltando dimmi pure...")
        text = r.recognize_google(audio, language="it-IT")
        print("Tu:",text)
    except Exception as e:
        print("Non ho capito")
    return text