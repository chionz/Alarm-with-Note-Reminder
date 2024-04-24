import datetime
import winsound



def set():
    print("Welcome to Simple Alarm\n")
    purpose = input("What is Your Purpose of this Alarm? ")
    hour = int(input("Set hour: "))
    minutes = int(input("Set minutes: "))
    am_pm = input("am or pm? ")
    print(f"Reminder Set for: {hour}:{minutes} {am_pm}", "Purpose:", purpose)
    ampm(hour,am_pm,minutes, purpose)

def ampm(hour,am_pm,minutes, purpose):
    if am_pm == 'pm':
        hour += 12

    elif hour == 12 and am_pm == 'am':
        hour -= 12
        
    else:
        pass
    ring(hour,minutes,purpose)

def ring(hour,minutes,purpose):
    while True:
        if hour == datetime.datetime.now().hour and minutes == datetime.datetime.now().minute:

            print("\nIt's the time for!", purpose,"\n")
            winsound.Beep(1000, 1000)
            for i in range(0,3):
                winsound.Beep(1000, 1000)
                
            snooze = input("Snooze (y/n)")
            if snooze == "y":
                if hour >= 12:
                    print("Alarm Snoozed by 1min!", hour-12,":",minutes+1)
                elif hour < 12:
                    print("Alarm Snoozed by 1min!", hour,minutes+1)
                ring(hour,minutes +1,purpose)
            elif snooze == "n":
                yn = input("Do you want to set another alarm? (y/n)")
                if yn == "y":
                    set()
                elif yn == "n":
                    return
               
            break

set()