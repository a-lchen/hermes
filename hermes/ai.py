from speech import *
from music import *
from reminders import *



class Bot:
    def __init__(self):
        self.musicOn = False
        self.active = False

    def parse(self, inp):
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
