import time
t = time.strftime('H:%M:%S')
hour = int(time.strftime('%H'))

if(hour>=0 and hour<=12):
    print("Good Morning")
elif(hour>12 and hour<=18):
    print("Good Afternoon")
else:
    print("Good Night")