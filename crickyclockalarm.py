import tkinter
import time
import random
import webbrowser
from datetime import datetime, timedelta
from threading import Timer

song = 'https://www.youtube.com/watch?v=CDdvReNKKuk'

playlist = 'songs'
lasthour = 0
lastmin = 0

def get_last_info():
    global playlist
    global lasthour
    global lastmin
    with open('lastinfo.txt','r') as g:
        g_contents = g.readlines()
        #g_size = len(g_contents)
        playlist = g_contents[2]
        lasthour = g_contents[0]
        lastmin = g_contents[1]
        #print(playlist)

get_last_info()

# print(line)
#Creating the window
window = tkinter.Tk()

#Declaring the variables for the window
inp_hours = tkinter.IntVar(value=lasthour)
inp_minutes = tkinter.IntVar(value=lastmin)
songdoc = tkinter.StringVar(value=playlist)
#songdoc.set(playlist)

#Updating the window title
window.title("Cricky Clock (Alarm)")

#Hour label and input field
tkinter.Label(window, text = 'Hour').grid(row = 0, column = 0)
tkinter.Entry(window, textvariable=inp_hours).grid(row = 0, column = 1)

#Minute label and input field
tkinter.Label(window, text = 'Minute').grid(row = 1, column = 0)
tkinter.Entry(window, textvariable = inp_minutes).grid(row = 1, column = 1)

#Playlist
tkinter.Label(window, text = 'Playlist').grid(row = 4, column = 0)
tkinter.Entry(window, textvariable = songdoc).grid(row = 4, column = 1)

def alarmstart():
    intinp_hours = inp_hours.get()
    intinp_minutes = inp_minutes.get()
    playlist_ = songdoc.get()
    def save_data():
        with open('lastinfo.txt', 'r+') as h:
            h.truncate(0)
            h.write(str(intinp_hours) + '\n' + str(intinp_minutes) + '\n' + str(playlist_))
    window.title("Cricky Clock (Alarm - active)")
    x = datetime.today()
    y = x.replace(day=x.day,hour=intinp_hours,minute=intinp_minutes,second=0,microsecond=0)
    delta_t = y - x
    if(delta_t.days == 0):
        pass
    else:
        y = y + timedelta(days=1)
    delta_t = y - x
    secs = delta_t.seconds
    try:
        save_data()
    except:
        pass
    def playsong():
        songdoc_txt = playlist_ + '.txt'
        with open(songdoc_txt, 'r') as f:
            f_contents = f.readlines()
            f_size = len(f_contents)
            print(f_size)
            song = f_contents[random.randint(0,f_size-1)]
            #print(f_contents)
            webbrowser.open_new_tab(song)
    t = Timer(secs, playsong)
    t.start()

tkinter.Label(window, text = 'Use values for a 24 hour clock.').grid(row = 3, columnspan = 2)

tkinter.Button(window, text="Start Alarm", command=alarmstart).grid(row=4, column=4)

window.mainloop()