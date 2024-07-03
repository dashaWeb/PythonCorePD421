color = ['red','purple','yellow','blue','violet','orange']
print(type(color),id(color), color,sep='\n')

print(color[1])
color[1] = 'black'
print(color)

# for item in color:
#     print(item.upper())
#     for chr in item:
#         print(chr+' - ',end='')
#     print()
# [start:end:step]
print('Size list :: ',len(color))
# color = ['red','purple','yellow','blue','violet','orange']
print(color[2:]) #['yellow', 'blue', 'violet', 'orange']
print(color[:4]) #['red', 'black', 'yellow', 'blue']
print(color[::2]) #['red', 'yellow', 'violet']
print(color[::-1]) #['orange', 'violet', 'blue', 'yellow', 'black', 'red'] -- reverse

# Додати новий елемент до списку в кінець
print(" list.append ".center(70,'='))
print(f'\tBefore :: {color}')
color.append('lime')
print(f'\tAfter  :: {color}')

# Додати новий елемент до списку за індексом
print(" list.insert ".center(70,'='))
print(f'\tBefore :: {color}')
color.insert(2,'gold')
print(f'\tAfter  :: {color}')

# Додати нові елементи до списку
print(" list.extend ".center(70,'='))
print(f'\tBefore :: {color}')
color.extend(['magenta','cyan','green'])
print(f'\tAfter  :: {color}')


# Видалити елемент зі списку в кінці або за індексом
print(" list.pop ".center(70,'='))
print(f'\tBefore :: {color}')
color.pop()
print(f'\tAfter  :: {color}')

print(" list.pop(2) ".center(70,'='))
print(f'\tBefore :: {color}')
color.pop(2)
print(f'\tAfter  :: {color}')

# Видалити елемент зі списку вза вмістом
print(" list.remove ".center(70,'='))
print(f'\tBefore :: {color}')
# if 'Orange' in color:
#     color.remove('Orange')
color.remove('orange')
print(f'\tAfter  :: {color}')

print(" list.clear ".center(70,'='))
print(f'\tBefore :: {color}')
# color.clear()
print(f'\tAfter  :: {color}')


print(" list.index ".center(70,'='))
print(f'\t Example :: {color}')
ind = color.index('lime')
print(f'\t find \'lime\' has index :: {ind}')
# ind = color.index('gold')
# print(f'\t find \'gold\' has index :: {ind}')

for i in range(3):
    color.append('red')
print(" list.count ".center(70,'='))
print(f'\t Example :: {color}')
ind = color.count('red')
print(f'\t Number of repetitions of the word \'red\' :: {ind}')


print(" list.reverse ".center(70,'='))
print(f'\tBefore :: {color}')
color.reverse()
print(f'\tAfter  :: {color}')


# sort a - z
print(" list.sort ".center(70,'='))
print(f'\tBefore :: {color}')
color.sort()
print(f'\tAfter  :: {color}')

# sort z - a
print(" list.sort ".center(70,'='))
print(f'\tBefore :: {color}')
color.sort(reverse=True)
print(f'\tAfter  :: {color}')
# test = [True, 'lorem', 45, 4.3]
# print(test)
print()
copy_color = color.copy()
print(f'copy   :: {id(color)}')
print(f'origin :: {id(copy_color)}')
print(f'\tOrigin :: {color}')
print(f'\tCopy  :: {copy_color}')

print()
copy_color[0] = 'brown'
print(f'\tOrigin :: {color}')
print(f'\tCopy  :: {copy_color}')

print('\n\n')
number = [1,2,58,6,5,9]

number = []

for i in range(10):
    number.append(i)

print(number)

import random
number = []

for i in range(10):
    number.append(random.randint(1,10))
    
print(number)

number = [i+2 for i in range(10)]
print(number)

number = [random.randint(1,10) for i in range(10)]
print(number)

number = []
for i in range(1,4):
    for j in range(1,4):
        number.append(i * j)
print()
number = [i*j for i in range(1,4) for j in range(1,4)]
print(number)
print(min(number))
print(max(number))
print(sum(number))
print(sorted(number))
print(sorted(number,reverse=True))

# number = []
# for i in range(10):
#     number.append(int(input('Enter mark --> ')))


mark = [int(i) for i in input('Enter mark --> ').split(' ')]
print(mark)
print(' '.join(str(i) for i in mark))