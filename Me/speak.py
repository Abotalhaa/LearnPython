from gtts import gTTS
from playsound import playsound
import speech_recognition as sr
r = sr.Recognizer()
with sr.Microphone() as src:
    print('Say something....')
    audio = r.listen(src)
try:
    t = r.recognize_google(audio, language='eng-ENG')
    print(t)
    f = open('NOM.txt', 'a', encoding='utf-8')
    f.writelines(t + '\n')
    f.close()
    obj = gTTS(text=t, lang='ar', slow=False)
    obj.save('nom.mp3')
    playsound('nom.mp3')
except sr.UnknownValueError as U:
    print(U)
except sr.RequestError as R:
    print(R)
except:
    print('Error')
