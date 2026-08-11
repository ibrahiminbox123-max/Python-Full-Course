number = 123456789
even = 0
odd = 0

while(number >0  ):
    digit = number % 10
    number = number // 10
    if(digit % 2 == 0 ):
        even = even + 1
        print(digit,'is even')
    else:
        odd = odd + 1
        print(digit,'is odd')
        
print(odd,'odd numbers')
print(even,'even numbers')