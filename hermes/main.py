#!/usr/bin/env python

"""
Main program of Hermes

Repeatedly takes input from user and reacts according to the input
"""

import threading
import speech_recognition as sr
import subprocess
import time
import Queue
from music import *
from speech import *
from ai import *

def main():
    ai = Bot()
    for x in range (100):
            inp = take_input()
            ai.parse(inp)

if __name__ == "__main__":
    main()
