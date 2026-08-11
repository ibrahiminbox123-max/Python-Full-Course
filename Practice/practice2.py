sec = int(input('Enter the number of seconds: '))

min  = sec // 60
remainingsec = sec % 60 
hour = sec // 3000

print(hour, 'hours', min, 'minutes', remainingsec, 'seconds')