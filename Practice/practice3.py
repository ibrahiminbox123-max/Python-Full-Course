amount = 780

original_amount = amount

total1 = amount // 500
amount = amount % 500               

total2 = amount //100
amount = amount % 100               

total3 = amount // 50
amount = amount % 50               

total4 = amount // 20
amount = amount % 20               

total5 = amount // 10
amount = amount % 10               


print("In", original_amount, "you will get", total1, "500 notes" )
print("In", original_amount, "you will get", total2, "100 notes")
print("In", original_amount, "you will get", total3, "50 notes")
print("In", original_amount, "you will get", total4, "20 notes")
print("In", original_amount, "you will get", total5, "10 notes")