import time
currenttime=time.strftime("%H:%M:%S")
print(currenttime)
currenttime=int(time.strftime('%H'))
if(currenttime<=00 or currenttime>=12):
    print("GOOD MORNING")
elif(currenttime<=13 or currenttime>=16):
    print("GOOD AFTERNOON")
elif(currenttime<=17 or currenttime>=20):
    print("GOOD EVENING")
else:
    print("GOOD NIGHT")

        
