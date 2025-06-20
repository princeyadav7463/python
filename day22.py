# day 22

import time
t = time.strftime('%H:%M:%S')  # %H is for hour, %M is for minute, %S is for second
hour = int(time.strftime('%H'))
hour = int(input("Enter hour: "))  
# print(hour)

if(hour>=0 and hour<12):
  print("Good Morning Sir!")  # this will be printed when the time is between 0 to 12
elif(hour>=12 and hour<17):
  print("Good Afternoon Sir!")  # this will be printed when the time is between 12 to 17
elif(hour>=17 and hour<0):
  print("Good Night Sir!")  # this will be printed when the time is between 17 to 0
