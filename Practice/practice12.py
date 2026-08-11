balance = 5000
while True:

        print('1.Check Balance')
        print('2.Withdraw')
        print('3.Deposit')
        print('4,Exit')

        choice = int(input('Enter your choice: '))

        if(choice == 1):
            print('Your Balance is: ', balance)
        elif(choice == 2):
            withdrawamount = int(input('Enter The Amount To Withdraw: '))
            if(withdrawamount <= balance):
                balance = balance - withdrawamount
                print(balance, '-', withdrawamount, '=', balance )
                print(balance,'is your balance')
            else:
                print('You Have Insufficient Balance')
        elif(choice == 3):
            depositamount = int(input('Enter The Amount to deposit: '))
            balance = balance + depositamount
            print(depositamount,'+', balance, '=', balance)
        elif(choice == 4):
            break
        else:
            print('Invalid Input')
print('Thanks For Using The ATM')
                    