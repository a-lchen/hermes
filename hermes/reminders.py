#!/usr/bin/env python

"""
Reminders module

Takes care of setting reminders through Hermes. Apple computer required.
"""

import subprocess
import sys
from datetime import datetime, timedelta
import timestring
from speech import *

#The OS script that runs the command to set the reminder
OSASCRIPT = ('<<END\n'
'on run argv\n'
'    set dateString to date (item 2 of argv & " " & item 3 of argv)\n'
'    tell application "Reminders"\n'
'        make new reminder with properties {name:item 1 of argv, due date:dateString}\n'
'    end tell\n'
'end run\n'
'END')


def new_reminder(remind_datetime, name):
    """
    Creates a new reminder and the runs the script to instantiate it.

    Returns a boolean variable indicating success of instantiation
    """
    timestr = remind_datetime.strftime("%I:%M:00%p")
    datestr = remind_datetime.strftime("%m/%d/%Y")
    # Execute applescript via shell to create a new reminder.
    command = 'osascript - "{n}" {d} {t} {osa}'.format(n=name, d=datestr,
                                                       t=timestr, osa=OSASCRIPT)
    with open('/dev/null', 'w') as devnull:
        status = subprocess.call(command, shell=True, stdout=devnull)
    return status

def setReminder(date, time, name):
    """
    Parses the date and time into a datetime object and runs
    new_reminder on it
    """
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
    """
    Gets user input for date, time, and name of reminder
    """
    talk('"Ok, what date would you like your reminder to be on"')
    date = take_input()
    talk('"What time?"')
    time = take_input()
    talk('"name?"')
    name = take_input()
    return (date, time, name)
