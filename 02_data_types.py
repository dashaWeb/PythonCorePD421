

# print(3,type(3),sep=" ---- ") # number (int)
# print(3.5,type(3.5),sep=" ---- ") # number (float)
# print('3.5',type('3.5'),sep=" ---- ") # string (str)
# print(True,type(True),sep=" ---- ") # boolean (bool)

name = "Sasha"
Name = "Masha"
first_name = "Oleg"
name2 = "Pasha"
age = 18
flag = True
PI = 3.14

print(name, Name, first_name, age, flag, PI)
# print(name + Name + first_name + age + flag + PI) error TypeError: can only concatenate str (not "int") to str
print(age + flag)  # True = 1; False = 0

day = 25
month = 10
year = 2009
age = 14
# 4.6.2025
print(day, month, year, sep='.')
# 25.10.09 (14 років)

print('{}.{}.{} ({} років)'.format(day, month, year, age))


# Operators
# **, //, %
# *, /
# +, -

first_number = 2
second_number = 3.5
res_sum = first_number+second_number
# 2 + 3 = 5
print('{} + {} = {}'.format(first_number, second_number, res_sum))
# 2 - 3 = 5
res_sub = first_number - second_number
print('{} - {} = {}'.format(first_number, second_number, res_sub))
# 2 * 3 = 5
res_mult = first_number * second_number
print('{} * {} = {}'.format(first_number, second_number, res_mult))
# 2 / 3 = 5
res_div = first_number / second_number
print('{} / {} = {}'.format(first_number, second_number, res_div))

# 2 ** 3 = 5
res_pow = first_number ** second_number
print('{} ** {} = {}'.format(first_number, second_number, res_pow))

# 2 // 3 = 5
res_div_int = first_number // second_number
print('{} // {} = {}'.format(first_number, second_number, res_div_int))


# 2 % 3 = 5
res_mod = first_number % second_number
print('{} % {} = {}'.format(first_number, second_number, res_mod))

test_sum = 5 - True

# int()
# float()
# str()

print(int(8 / 3))
print(name + ' ' + Name + ' ' + first_name + str(age) + str(flag) + str(PI))

line_1 = "Hyper"
line_2 = "Text"
line_3 = "Markup"
line_4 = "Language"

# res_line = line_1 + line_2 + line_3 + line_4
res_line = "{} {} {} {} ".format(line_1, line_2, line_3, line_4)
print('-'*40)
print(res_line)


# one = float(input("Enter first number :: "))
# two = input("Enter second number :: ")
# two = float(two)
# print(one+two)
# +=, -=, *=, /=, %=, **=, //=
# one = 5
# print(one)
# one += 1  # one = one + 1

# one = 3
# two = 3
# one = two = 3

# one = 5
# two = 7
# one, two = 5, 7


# numb = 200
# pers = 5

# res = numb / 100 * 5
# res = numb * 0.1



