# ==, >, <, >=, <=, !=

a = 5
b = 7
password = 'mka5'

c = d = 9

print(f"{password} == mka5 --> {password == 'mka5'}")  # True
print(f"{a} == {b} --> {a == b}") #False
print(f"{a} != {b} --> {a != b}") #True
print(f"{a} > {b} --> {a > b}") #False
print(f"{a} < {b} --> {a < b}") #True
print(f"{c} < {d} --> {c < d}") #False
print(f"{c} <= {d} --> {c <= d}") #True
print(f"{c} >= {d} --> {c >= d}") #True

# res = a + True

# year = int(input('Enter year : '))
# days_in_year = 365
# is_leap = year % 4 == 0
# days_in_year += is_leap
# print(f"In {year} year = {days_in_year} days")

# and 
# or
# year = int(input('Enter year : '))
# days_in_year = 365 + (year % 4 == 0 and year % 100 != 0 or year % 400 == 0)
# print(f"In {year} year = {days_in_year} days")


# age = int(input("Enter age :: "))
# if age >= 18:
#     print("Hello")
# else:
#     print("Error")


day = int(input("Enter number of day :: "))

if day == 1:
    print("Monday")
elif day == 2:
    print("Tuesday")
elif day == 3:
    print("Wednesday")
else:
    print('Error')

# login = input('Хто прийшов? -> ')
# if login.lower() == 'Адмін'.lower():
#     password = input('Пароль? -> ')
#     if password == 'ШАГ':
#         print('Ласкаво просимо')
#     elif password.lower() == 'Скасувати'.lower():
#         print('Вхід скасований !')
#     else:
#         print('Пароль невірний!')
# elif login.lower() == 'Скасувати'.lower():
#     print('Вхід скасований !')
# else:
#     print('Я вас не знаю!')


# input('\t 1 - Sum \n \t 2 - Sub \n enter :: ')
