# bill
# 1 hour --> 50
# 1 min --> 1
# 5 hour --> 200

hours = int(input("Enter number of hours: "))
minutes = int(input("Enter number of minutes: "))
bill = 0

if hours < 0 or hours>7:
    print("Invalid input")
else:
    if(hours>=0 and hours <5):
        bill = (50 * hours) +  minutes
        print(f"Your bill is {bill} rupees")
    elif(hours>=5 and hours <=7):
        newhr = hours-5
        bill = 200 + (newhr * 50) + minutes
        print(f"Your bill is {bill} rupees")
# print(f"Your bill is {bill} rupees") 
