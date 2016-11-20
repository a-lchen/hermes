#!/usr/bin/env python

"""
AI module

Functions that make up Hermes' intelligence and how he responds to inputs
"""
from speech import *
from music import *
from reminders import *

class Bot:
    """
    A Bot instance will holds a few environment variables and parses input accordingly
    """
    def __init__(self):
        self.musicOn = False
        self.active = False

    def parse(self, inp):
        """
        Parse any input given to the bot. Performs the action necessary given a stimulus
        otherwise, apologizes for not understanding

        Returns None after executing the correct actio
        """
        if ("Hermes" in inp or "hermes" in inp):
            self.active = True
            text = '"Yes?"'
            talk(text)
        if(self.active):
            if "reminder" in inp:
                print "starting reminder shenanigans"
                (date, time, name) = listenReminderCues()
                setReminder(date, time, name)
            if "music" in inp and (self.musicOn == False) and ("turn" in inp or "play" in inp):
                print "playing music now"
                startMusic = musicThread(1, "Thread-1", "start", None)
                startMusic.start()
                self.musicOn = True
            elif(self.musicOn):
                "listening to music cues"
                self.musicOn = listenMusicCues(inp)
            if "sleep" in inp and ("back" in inp or "go" in inp):
                    talk('"Good night"')
                    self.active = False
            if "thank you" in inp:
                talk('"You are welcome"')
            if "set" in inp or "reminder" in inp or "remind" in inp:
                setReminder(inp)
            else:
                talk('"sorry, I do not understand"')
