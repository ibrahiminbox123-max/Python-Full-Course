mint = int(input('Enter the number of minutes: '))

hour = mint // 60
remainingmin = mint % 60

print(hour, 'hours', remainingmin, 'minutes')