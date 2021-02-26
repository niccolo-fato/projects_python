import speech_recognition as sr

recognizer_instance = sr.Recognizer()

with sr.Microphone() as source:
    recognizer_instance.adjust_for_ambient_noise(source)
    print("Speak I'm listening...")
    audio = recognizer_instance.listen(source)
    print("Ok, I'm processing the message ...")

try:
    text = recognizer_instance.recognize_google(audio, language="it-IT")
    print("You said: \n ", text)
except sr.UnknownValueError:
    print("Sorry,i did not get that!")
