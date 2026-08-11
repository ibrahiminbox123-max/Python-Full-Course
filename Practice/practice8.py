units = int(input("Enter the number of units: "))

if(units <= 100):
    bill = units * 10
    print("Your Electricity Bill is: ", bill)
elif(units <= 200):
    bill2 = units * 15
    print(bill2)
elif(units <= 300):
    bill3 = units * 20
    print(bill3)
elif(units > 300):
    bill4 = units * 25
    print(bill4)
else:
    print("Your Electricity Bill is: ", bill4)