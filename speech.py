#!/usr/bin/env python

"""
Speech module

Contains function pertaining to the input and output of Hermes
"""

import subprocess
import speech_recognition as sr

r = sr.Recognizer()

def talk (s):
    """talks to user by executing a bash script"""
    print "talking"
    subprocess.call(('espeak -v en-us ' + s), shell = True)

def recognize (audio):
    """Recognizes user input"""
    try:
        inp = r.recognize_google(audio)
        print inp
        return inp
    except sr.UnknownValueError:
        print("Computer could not understand audio")
        a = listen()
        return recognize(a)
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        a = listen()

        return recognize(a)

def take_input():
    """Takes user input"""
    with sr.Microphone() as source:
        print "listening"
        audio = r.listen(source)
    print "done listening"
    try:
        print "trying to recognize"
        inp = r.recognize_google(audio)
        print inp
        return inp
    except sr.UnknownValueError:
        print("Hermes could not understand audio")
    except sr.RequestError as e:
        print("Hermes cannot connect to his speech recognition server; {0}".format(e))
