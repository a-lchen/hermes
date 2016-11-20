#!/usr/bin/env python

"""
Reminders


"""

import subprocess
import sys
from datetime import datetime, timedelta
import timestring
from speech import *


OSASCRIPT = ('<<END\n'
'on run argv\n'
'    set dateString to date (item 2 of argv & " " & item 3 of argv)\n'
'    tell application "Reminders"\n'
'        make new reminder with properties {name:item 1 of argv, due date:dateString}\n'
'    end tell\n'
'end run\n'
'END')

def new_reminder(remind_datetime, name):
    timestr = remind_datetime.strftime("%I:%M:00%p")
    datestr = remind_datetime.strftime("%m/%d/%Y")
    # Execute applescript via shell to create a new reminder.
    command = 'osascript - "{n}" {d} {t} {osa}'.format(n=name, d=datestr,
                                                       t=timestr, osa=OSASCRIPT)
    with open('/dev/null', 'w') as devnull:
        status = subprocess.call(command, shell=True, stdout=devnull)
    return status

def setReminder(date, time, name):
    d = timestring.Date(date)
    t = timestring.Date(time)
    dt = t.replace(day=d.day, month=d.month, year=d.year)
    status = new_reminder(dt.date, name)
    if status == 0:
        print("New Reminder:\n"
              "{0}: {1}".format(dt.date.strftime("%m/%d/%Y %H:%M"), name))
    else:
        print("Error occured")

def listenReminderCues():
    talk('"Ok, what date would you like your reminder to be on"')
    date = take_input()
    talk('"What time?"')
    time = take_input()
    talk('"name?"')
    name = take_input()
    return (date, time, name)
