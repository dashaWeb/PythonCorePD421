
# i = 0
# while i < 10:
#     i+=1
#     print(f'{i}',end='\t')

# print('End')

# i = 1
# while i <= 10:
#     print(f'{i}',end='\t')
#     i+=1

# i = 10
# while i >= 1:
#     print(f'{i}',end='\t')
#     i-=1
# print()

# numb = int(input('Enter number --> '))
# i = 1
# while i <= numb:
#     print(f'{i}',end='\t')
#     i+=1

# numb = int(input('Enter number --> '))
# i = 1
# if numb >= 1:
#     while i <= numb:
#         print(f'{i}',end='\t')
#         i+=1
# else:
#     while i >= numb:
#         print(f'{i}',end='\t')
#         i-=1

# while True:
#     start = int(input('Enter start range --> '))
#     end = int(input('Enter end range   --> '))
#     if start > end:
#         print('Error data!!!')
#     else:
#         break

# # if start > end:
# #     start,end = end,start

# while start <= end:
#     print(f'{start}',end='\t')
#     start+=1

# i = 0
# while i < 5:
#     i+=1
#     numb = int(input('Enter number : '))
#     if numb % 2 != 0:
#         continue
#     print(f'{numb} is even')
# else:
#     print('Finally')

# i = 0
# while i < 5:
#     i+=1
#     answer = int(input('2 + 2 = ? --> '))
#     if answer == 4:
#         break
# else:
#     print('Good!!!!')


# print(f' 1 x 2 = {1*2}')
# print(f' 2 x 2 = {2*2}')
# print(f' 3 x 2 = {3*2}')
# print(f' 4 x 2 = {4*2}')
# print(f' 5 x 2 = {5*2}')

# i = 1
# while i <= 10:
#     j = 1
#     while j <= 5:
#         print(f'{i} x {j} = {i * j}',end='\t')
#         j+=1
#     print()
#     i+=1  
# else:
#     print()

# i = 1
# while i <= 10:
#     j = 6
#     while j <= 10:
#         print(f'{i} x {j} = {i * j}',end='\t')
#         j+=1
#     print()
#     i+=1  
# else:
#     print()

line = 0
start_j, end = 1,5
while line < 2:
    line+=1
    i = 1
    while i <= 10:
        j = start_j
        while j <= end:
            print(f'{i} x {j} = {i * j}',end='\t')
            j+=1
        print()
        i+=1  
    else:
        print()
        start_j += 5
        end+=5


