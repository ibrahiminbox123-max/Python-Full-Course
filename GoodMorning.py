import time

TimeStamp = time.strftime('%H:%M:%S')
Hour = int(time.strftime('%H'))

if Hour >= 8 and Hour < 12:
    print("Good Morning")

elif Hour >= 12 and Hour < 17:
    print("Good Evening")

elif Hour >= 17 and Hour < 24:
    print("Good Night")