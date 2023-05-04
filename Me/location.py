# import geocoder
# location = geocoder.ip("161.185.160.93")
# print(location)


import musicpy as mp
# from musicpy.musicpy import C, play
#
# # a nylon string guitar plays broken chords on a chord progression
#
# guitar = (C('CM7', 3, 1 / 4, 1 / 8) ^ 2 |
#           C('G7sus', 2, 1 / 4, 1 / 8) ^ 2 |
#           C('A7sus', 2, 1 / 4, 1 / 8) ^ 2 |
#           C('Em7', 2, 1 / 4, 1 / 8) ^ 2 |
#           C('FM7', 2, 1 / 4, 1 / 8) ^ 2 |
#           C('CM7', 3, 1 / 4, 1 / 8) @ 1 |
#           C('AbM7', 2, 1 / 4, 1 / 8) ^ 2 |
#           C('G7sus', 2, 1 / 4, 1 / 8) ^ 2) * 2
#
# play(guitar, bpm=100, instrument=25)
# print(guitar)
# ----------------------------------
import speech_recognition as sr

# Initialize the recognizer
r = sr.Recognizer()

# Using the microphone as input source
with sr.Microphone() as source:
    print("I'm listening, say something...")
    audio = r.listen(source)

    try:
        print("You said: " + r.recognize_google(audio))

        # Open or create a file to write
        with open("output.txt", "a") as file:
            # Write the recognized text
            file.write(r.recognize_google(audio))

    # If speech is not recognized
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand")

    # If the recognizer is unable to access the internet or recognize the audio
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
