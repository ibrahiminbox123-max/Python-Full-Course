a = int(input("Enter Your Age: "))
print("Your Age Is:", a)

# Conditional operators

# > greater than
# < less than
# >= greater than or equal to
# <= less than or equal to    
# == equal to                

if (a > 18):
    print("You Are Able To Drive")
else:
    print('You Are Not Able To Drive')


appleprice = 10
budget = 200

if(budget - appleprice > 50):
    print("You Can Buy Apple")
elif(budget - apple > 70):
    print("Okay, You Can Buy Apple")
else:
    print("You Can't Buy Apple")

# Nested If Else

num = 18

if(num < 0):
    print("Number IS Negative")
elif(num > 0):
    if(num <= 10):
        print("Number Is between 1-10")
    elif(num >=18 and num <= 20):
        print("Number Is 10-20")
    else:
        print("Number Is greather than 20")
else:
    print("Number Is 0")

