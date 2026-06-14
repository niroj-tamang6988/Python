import time 

timestamp = time.strftime('%H:%M:%S')
print(timestamp)

hour = int(time.strftime('%H'))
print(hour)


if hour > 5:
    print("Good morning")

elif(hour > 12):
    print("Good Afternoon")

elif(hour > 18):
    print("Good afternoon")

else:
    print("Good night")
     