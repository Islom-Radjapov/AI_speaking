import pyttsx3                              # Speaking librery call
import datetime as dt                       # date and time definition librery call

engine = pyttsx3.init()                     # object creation
engine.setProperty('rate', 125)             # setting voice rate
en_voice_id = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'         # english voice id
engine.setProperty('voice', en_voice_id)    # schoice english voice acting

data = dt.date.today()                      # determine the day
time = dt.datetime.now()                    # determine the time

engine.say(f"Today is the {data.day}th day of the {data.month}th month of {data.year}"
           f", it is now {time.hour} hour {time.minute} minutes {time.second} seconds.")                 # pronounce the date and time in full
engine.runAndWait()                         # start pronounce
