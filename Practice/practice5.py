note500 = 2
note100 = 3
note50 = 5
note20 = 2
note10 = 11

withdraw = 780

total =  withdraw // 500
withdraw = withdraw % 500

print('In 780 you wil take ', total, "500 note")
print("remaining amount",withdraw)

total2 = withdraw // 100
withdraw = withdraw % 100

print('In 280 you wil take ', total2, "100 note")

total3 = withdraw // 50
withdraw = withdraw % 50

print('In 80 you wil take ', total3, "50 note")

total4 = withdraw // 20
withdraw = withdraw % 20

print('In 20 you wil take ', total4, "20 note")

total5 = withdraw // 10
withdraw = withdraw % 10

print('In 10 you wil take ', total5, "10 note")                                           