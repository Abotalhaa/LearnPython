from gtts import gTTS
import os

# النص العربي
text = "مرحبًا بالعالم"

# تحويل النص إلى نطق باللغة الإنجليزية
tts = gTTS(text, lang='en')
tts.save("hello.mp3")

# تشغيل ملف الصوت
os.system("mpg321 hello.mp3")
