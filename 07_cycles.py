
# word = "Hello"

# for letter in word:
#     print(letter+" _ ",end='')

# print()

# for i in range(10):
#     print(i+1)

# for i in range(1,11):
#     print(i)

# num = int(input("Enter number : "))
# for i in range(1,num+1,2):
#     print(i,end='\t')

# numb = int(input("Enter number :: "))
# counter = 0

# 8
# 1 2 3 4 5 6 7 8
# 8 / 1 true
# 8 / 2 true
# 8 / 3 false
# for i in range(1,numb+1):
#     if numb % i == 0:
#         counter+=1

# if counter > 2:
#     print('Complex number')
# else:
#     print('Prime number')


# numb = int(input("Enter number :: "))
# flag = True # prime
# for i in range(2,numb//2 + 1):
#     if numb % i == 0:
#         flag = False
#         break

# if not flag:
#     print('Complex number')
# else:
#     print('Prime number')

import random
# test random
# for i in range(5):
#     # rnd = random.random() -- 0 - 1
#     # rnd = random.randint(1,3) -- 1 - 3
#     # rnd = random.choice('rsp')  випадковий вибір символа
#     print(rnd)
#     input()
us = bt = d = 0
while True:
    user_score = 0
    bot_score = 0
    for i in range(3):
        while True:
            user = input('''
            [r] - rock
            [p] - paper
            [s] - scissors
                Enter your choose :: ''').lower()
            if user == 's' or user == 'p' or user == 'r':
                break
            else:
                print('Error. Enter true choose')
        bot = random.choice('rps')
        print('\t\t Bot \t User')
        print(f'\t\t [{bot}] \t  [{user}]')
        if user == 'p' and bot == 'r' or user == 'r' and bot =='s' or user == 's' and bot == 'p':
            user_score+=1
        elif bot == 'p' and user == 'r' or bot == 'r' and user =='s' or bot == 's' and user == 'p':
            bot_score+=1

    if user_score > bot_score:
        print('='*15 + ' Congratulation !!! ' + '='*15)
        us+=1
    elif bot_score > user_score:
        print('='*15 + ' Sorry!! You Loser !!! ' + '='*15)
        bt+=1
    else:
        print('='*15 + ' Draw ' + '='*15)
        d+=1
    
    exit = input('[y] - yes; [n] - no --> ')
    if exit == 'n':
        break
print(f'user - {us} bot - {bt}  draw - {d}')



# 163256
# 125