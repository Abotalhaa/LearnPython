import speech_recognition
from gtts import gTTS
from playsound import playsound

r = speech_recognition.Recognizer()
with speech_recognition.Microphone() as src:
    print('Say something....')
    audio = r.listen(src)
try:
    t = r.recognize_google(audio, language='ar-AR')
    print(t)
    f = open('text.txt', 'a', encoding='utf-8')
    f.writelines(t + '\n')
    f.close()
    obj = gTTS(text=t, lang='ar', slow=False)
    obj.save('text.mp3')
    playsound('text.mp3')
except speech_recognition.UnknownValueError as U:
    print(U)
except speech_recognition.RequestError as R:
    print(R)
