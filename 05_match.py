

# day = input('Enter number of day --> ')
# match int(day): # day == 1
#     case 1:
#         print('Monday')
#     case 2:
#         print('Tuesday')
#     case 3:
#         print('Wednesday')
#     case _:
#         print('Error')

# month = int(input('Enter month --> '))
# days = 0
# match month:
#     case 1:
#         days = 31
#     case 3:
#         days = 31
#     case 5:
#         days = 31
#     case 7:
#         days = 31
#     case 8:
#         days = 31
#     case 10:
#         days = 31
#     case 12:
#         days = 31
#     case 4:
#         days = 30
#     case 6:
#         days = 30
#     case 9:
#         days = 30
#     case 11:
#         days = 30
#     case 2:
#         year = int(input('Enter year --> '))
#         if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#             days = 29
#         else:
#             days = 28
# if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
#     days = 31
# elif month == 4 or month == 6 or month == 9 or month == 11:
#     days = 30
# elif month == 2:
#     year = int(input('Enter year --> '))
#     if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#         days = 29
#     else:
#         days = 28
# else:
#     print('Error')

# print(days)

# 31.12.2004
# 01.01.2005

day = int(input('Enter day --> '))
month = int(input('Enter month --> '))
year = int(input('Enter year --> '))

if day < 10:
    print('0',end='')
print(f'{day}.',end='')
if month < 10:
    print('0',end='')
print(f'{month}.',end='')
print(f'{year}')
full_days = 0
if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
    full_days = 31
elif month == 4 or month == 6 or month == 9 or month == 11:
    full_days = 30
elif month == 2:
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        full_days = 29
    else:
        full_days = 28
else:
    print('Error')
if day > full_days or month > 12:
    print('Error')
else:
    day+= 1
    if day > full_days:
        day = 1
        month+=1
    if month > 12:
        month = 1
        year+=1

    if day < 10:
        print('0',end='')
    print(f'{day}.',end='')
    if month < 10:
        print('0',end='')
    print(f'{month}.',end='')
    print(f'{year}')