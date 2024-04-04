#TTS(Text To Speech)

from gtts import gTTS
from playsound import playsound

text = "If you are reaching out regarding to your phone screen and onsite interview scheduling change, please reply to our scheduling coordinator who sent you the scheduling intake. They will help you on that. If you are reaching out for other inquires, please expect my reply on April 15th."
file_name = "sample.mp3"
tts_en = gTTS(text=text, lang = 'en')
tts_en.save(file_name)
# playsound(file_name)

text = '파이썬을 배우기를 잘한 것 같아요. 재미 있어요.'
tts_ko = gTTS(text=text, lang='ko')
tts_ko.save(file_name)
# playsound(file_name)

#Long Sentence(loading file)
with open('sample.txt', 'r', encoding='utf8') as f:
    text = f.read()

tts_ko = gTTS(text=text, lang='ko')
tts_ko.save(file_name)
playsound(file_name)


