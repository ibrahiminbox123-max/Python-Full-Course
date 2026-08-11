note500 = 2
note100 = 3
note50 = 5
note20 = 2
note10 = 11

withdrawamount = 2000

if(withdrawamount // 500 > 0):
    total = withdrawamount // 500
    print(total)

    if(total > note500):
        print('sorry')

    if(withdrawamount // 100 > 0):
        total2 = withdrawamount // 100
        print(total2)

        if(total2 > note100):
            print('sorry')
else:
    print(',not enoguh money')