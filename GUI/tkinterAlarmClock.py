

from tkinter import *
import datetime
import time
import winsound


def alarm(set_alarm_timer):
    while True:
        time.sleep(1)
        current_time = datetime.datetime.now()
        now = current_time.strftime("%H:%M:%S")
        date = current_time.strftime("%D:%M:%Y")
        print("Today's Set Date is:", date)
        print(now)
        if now == set_alarm_timer:
            print("Time to Wake Up Sir")
        winsound.PlaySound("sound.wav", winsound.SND_ASYNC)
        break

def actual_time():
    set_alarm_timer = f"{hour.get()}:{min.get()}:{sec.get()}"
    alarm(set_alarm_timer)


clock = Tk()
clock.title("GhostRiders Alarm Clock")
clock.geometry("400×200")

time_foramt = Label(clock, text = " Enter time in 24 hour format Sir!!", fg = "red", bg = "black", font = "Serif").place(x = 70, y = 140)
addTime = Label(clock, text = "Hour Min Sec", font = 70).place(x = 130)
setYourAlarm = Label(clock, text = "what time to wake you up Sir", fg = "blue", relief = "solid", font = ("Arial", 10, "bold")).place(x = 0, y = 40)


# these values required to set the alarm
hour = StringVar()
min = StringVar()
sec = StringVar()


# Time required to set the alarm cock
hourTime = Entry(clock, textvariable = hour, bg = "purple", width = 25).place(x = 120, y = 40)
minTime = Entry(clock, textvariable = min, bg = "purple", width = 25).place(x = 160, y = 40)
hourTime = Entry(clock, textvariable = sec, bg = "purple", width = 25).place(x = 220, y = 40)

# take the time through standard inputs from users
submit = Button(clock, text = "Set Alarm Sir", fg = "red", width = 20, command = actual_time).place(x = 120, y = 80)

# finally execution 
clock.mainloop()

