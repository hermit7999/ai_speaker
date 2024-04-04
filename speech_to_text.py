#STT(Speech To Text)
import speech_recognition as sr
r = sr.Recognizer()
with sr.Microphone() as source :
    print("'I'm hearing")
    audio = r.listen(source, timeout=7, phrase_time_limit=2)
    # audio = r.listen(source)    # listen from micro phone

#exception case
try:
    # English
    text = r.recognize_whisper(audio,language='en')
    print(text)
    # korean
    # text = r.recognize_whisper(audio,language='ko')
    # print(text)
except sr.UnknownValueError:
    print("Couldn't recognized")
except sr.RequestError as e: 
    print('Request fail : {0}' .format(e))