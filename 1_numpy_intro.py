import datetime
import time
from playsound import playsound

alarmHour = int(input("Enter Hour: "))
alarmMin = int(input("Enter Minute: "))
alarmSec = int(input("Enter Second: "))
alarmAm = input("am/pm: ")

if alarmAm == "pm":
    alarmHour += 12

while True:
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    print(current_time)
    if(alarmHour == datetime.datetime.now().hour and alarmMin == datetime.datetime.now().minute and alarmSec == datetime.datetime.now().second):
        print("Playing....")
        try:
            while (alarmMin == datetime.datetime.now().minute):
                playsound("Alarm.mp3")
        except KeyboardInterrupt:
            pass
        break
    time.sleep(1)
