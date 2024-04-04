import time, os
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound

r = sr.Recognizer()
m = sr.Microphone()

# Speech to text
# def listen(recognizer, audio):
def listen(audio):
    try:
        text = r.recognize_whisper(audio,language='en')
        print('User :' + text)
        return text

    except sr.UnknownValueError:
        print("Could't Recognized")
    except sr.RequestError as e:
        print('Request Error : {0}'.format(e))

# Answer : need to connect with GPT or LLM model
def answer(input_text):
    answer_text = ''
    if 'hi' in input_text:
        answer_text = 'Hello? Nice to meet you Sir'
    elif 'weather' in input_text:
        answer_text = 'It is good to die'
    elif 'thank' in input_text:
        answer_text = 'your welcome'
    elif 'bye' or 'end' in input_text:
        answer_text = 'Have a good day'
        # stop_listening(wait_for_stop=False)
    else:
        answer_text = 'Could you please say again?'
    
    speak(answer_text)

# TTS
def speak(text):
    print('[AI Speaker]' + text)
    file_name = 'voice.mp3'
    tts = gTTS(text=text, lang='en')
    tts.save(file_name)
    playsound(file_name)
    if os.path.exists(file_name):
        os.remove(file_name)
 
 #mic
def microphone():
    with m as source :
        print("'I'm hearing")
        audio = r.listen(source, timeout=7, phrase_time_limit=2)
    return audio

speak('What can I help you?')
# stop_listening = r.listen_in_background(microphone, listen)
while True:   
    audio = microphone()
    text = listen(audio)
    answer(text)
    time.sleep(0.1)
