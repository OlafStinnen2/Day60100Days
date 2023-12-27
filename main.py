import datetime

today = datetime.date.today() 

print("🌟Event Countdown Timer🌟\n")

event = input("Input the event > ")

year = int(input("Input the year > "))

month = int(input("Input the month > "))

day = int(input("Input the day > "))

#🎉🎉Nan's 100th birthday is today! 🎉🎉

event_date = datetime.date(year, month, day)


delta = (event_date - today).days
if event_date > today: 
  print(f"The {event} is coming soon in {delta} days.")
elif event_date < today: 
  print(f"The {event} has already passed for {-1*delta} days.")
else:
  print(f"🎉🎉 {event} is today! 🎉🎉")