//WE CAN GREET BY JUST GETTING THE TIME FROM OUR OWN DESKTOP OR SYSTEM.THIS CODE CONTAIN IF-ELSE CONCEPT AND TIME MODULE FOR EXECUTING THE CODE.
import time
currenttime=time.strftime("%H:%M:%S")
print(currenttime)
currenttime=int(time.strftime('%H'))
if(currenttime<=00 and currenttime>=12):
    print("GOOD MORNING")
elif(currenttime<=13 and currenttime>=16):
    print("GOOD AFTERNOON")
elif(currenttime<=17 and currenttime>=20):
    print("GOOD EVENING")
else:
    print("GOOD NIGHT")

        

