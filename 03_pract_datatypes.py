# number = int(input("Enter number: ")) #1452
# num_4 = number % 10 #2
# number //=10 # number = number // 10 => 145
# num_3 = number % 10 # 5
# number //=10 # number = number // 10 => 14
# num_2 = number % 10 # 4
# number //=10 # number = number // 10 => 1
# num_1 = number

# print(num_1, num_2, num_3, num_4)

# print(chr(9556) + chr(9552)*5 + chr(9574) + chr(9552)*5+ chr(9559))
# print(chr(9562) + chr(9552)*5 + chr(9577) + chr(9552)*5 + chr(9565))


# Завдання 1
# Користувач вводить з клавіатури грошову суму в гривнях і копійках (гривні і копійки
# вводяться в різні змінні). Сума може бути введена як правильно (наприклад 19 грн 90
# коп), так і неправильно (наприклад 22 грн 978 коп). Написати програму, яка,
# використовуючи тільки лінійний алгоритм, здійснить коригування введення грошової
# суми в правильну форму.
# Наприклад, якщо користувач ввів 11 грн 150 коп, програма має вивести на екран суму 12
# грн 50 .

uah = int(input("Enter value uah :: ")) #11
pennies = int(input("Enter value pennies :: "))#150
uah += pennies // 100 
pennies %= 100
print("{} грн {} коп.".format(uah,pennies))


# task 6
print(chr(9556) + chr(9552)*50 + chr(9559))
print()
print(chr(9553) + ' '*15 + 'Pory Roku' + ' ' * 26 + chr(9553))
print()
print(chr(9568) + chr(9552)*11 + chr(9574) + chr(9552)*14 +
      chr(9574) + chr(9552)*11 + chr(9574) + chr(9552)*11 + chr(9571))
print()
print(chr(9553) + ' '*3 + 'Zyma' + ' '*4 + chr(9553) + ' '*4 + "Vesna" + ' ' * 5 +
      chr(9553) + ' '*3 + 'Lito' + ' '*4 + chr(9553) + ' '*3 + 'Osin' + ' '*4 + chr(9553))
print()
print(chr(9562) + chr(9552)*11 + chr(9577) + chr(9552)*14 +
      chr(9577) + chr(9552)*11 + chr(9577) + chr(9552)*11 + chr(9565))
