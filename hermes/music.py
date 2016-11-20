#!/usr/bin/env python

"""
Music module

Takes care of all music related queries
"""

import threading
import subprocess

from speech import *

class musicThread (threading.Thread):
    """
    Thread object that runs Shpotify to play a off one's spotify
    """
    def __init__(self, threadID, name, actionId, payload):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.actionId = actionId
        self.payload = payload

    def startMusic(self):
        talk('"okay, playing music for you now"')
        subprocess.call('spotify play', shell=True)

    def run(self):
        """Runs any music action depending on what action was requested"""
        print "Starting " + self.name
        if (self.actionId == "start"):
            print "starting music"
            self.startMusic()
        elif(self.actionId == "next"):
            subprocess.call('spotify next', shell=True)
        elif(self.actionId == 'pause'):
            subprocess.call('spotify pause', shell=True)
        elif(self.actionId == "quit"):
            subprocess.call('spotify quit', shell=True)
        elif(self.actionId == "song"):
            print "playing " + self.payload
            subprocess.call('spotify play '+ '"' + self.payload+'"', shell=True)
        print "Exiting " + self.name


def listenMusicCues(inp):
    """
    Determines what action to perform in the context of music depending on what
    the user said to Hermes

    Options include next, pause, or choosing a specific song

    Returns whether or not the music stayed on (musicOn)
    """
    musicOn = True
    if ("next" in inp):
        #subprocess.call('spotify next& \n', shell=True)
        print "next"
        startNext = musicThread(1, "Thread-1", "next", None)
        startNext.start()
    elif("pause" in inp):
        print "pausing"
        p = musicThread(1, "pause thread", "pause", None)
        p.start()
        musicOn = False

    elif("song" in inp):
        print "which song do you want to hear"
        a = listen()
        out = recognize(a)
        song = musicThread(1, "song thread", "song", out)
        song.start()
    return musicOn
