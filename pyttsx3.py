# program to convert text to speech using python
# pip install pyttsx3 

import pyttsx3
# to activate attributes
engine = pyttsx3.init()
# using say method to pass the input to be spoken
engine.say("Oii, you just wrote a cool code")
# runAndWait method to process voice command
engine.runAndWait()