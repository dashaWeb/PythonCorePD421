
month = int(input('Enter month :: '))
offset = int(input('Enter start day :: '))


if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
    days = 31
elif month == 4 or month == 6 or month == 9 or month == 11:
    days = 30
elif month == 2:
    year = int(input('Enter year --> '))
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        days = 29
    else:
        days = 28
else:
    print('Error')

offset-=1
print('  \t' * (offset),end='')
i = 1
counter = 0
last_line = (days + offset) // 7
while i <= days:
    if i < 10:
        print(f'0{i}\t',end='')
    else:
        print(f'{i}\t',end='')
    if (i + offset) % 7 == 0:
        print()
        last_line-=1
        counter+=1
        if i - 1 > 0:
            counter+=1  
    i+=1
    if last_line == 0 and (days + offset) % 7 == 6 and i == days:
        counter+=1
print()
print('number ', counter)