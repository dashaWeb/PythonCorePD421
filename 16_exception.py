
# number = int(input('Enter number :: '))

# print(f'Result:: {number}')
# print('Finally program')

# -----------------------------
# while True:
#     try:
#         number = int(input('Enter number :: '))

#         print(f'Result:: {number}')
#         print('Finally try')
#         break
#     except ValueError:
#         print('Error number !!!')

# print('End')


# while True:
# try:
#     number_1 = int(input('Enter number :: '))
#     number_2 = int(input('Enter number :: '))

#     print(f'Result :: {number_1} / {number_2} = {number_1 / number_2}')
#     print('Finally try')

# except ValueError:
#     print('Error number !!!')
# except ZeroDivisionError:
#     print('division by zero')
# except Exception:
#     print('Base exception')
# else:
#     print('Good')
# finally:
#     print('Finally')
# print('End')

# -----------------------------------------
# try:
#     number_1 = int(input('Enter number :: '))
#     number_2 = int(input('Enter number :: '))

#     print(f'Result :: {number_1} / {number_2} = {number_1 / number_2}'+1+5)
#     print('Finally try')

# except (ValueError,ZeroDivisionError):
#     print('Error number !!!')
# except Exception as ex:
#     print('Base exception',ex)
# else:
#     print('Good')
# finally:
#     print('Finally')
# print('End')


# def printNumb(numb):
#     if numb < 0 :
#         raise ValueError('number < 0')
#     if numb > 10_000:
#         raise TypeError('numb > 10_000')
#     print(f'Ok --> {numb}')


# while True:
#     try:
#         numb = int(input('Enter number --> '))
#         printNumb(numb)
#     except ValueError as ex:
#         print(ex)
#     except TypeError as ex:
#         print(ex)
#     except:
#         print('Error')


# # Task 1
# try:
#     numb_1 = int(input('Enter number --> '))
#     numb_2 = int(input('Enter number --> '))
#     print(f'{numb_1} / {numb_2} = {numb_1 / numb_2}')
# except ZeroDivisionError as ex:
#     print(ex)

# Task 2.1
# def division(a,b):
#     print(f'{a} / {b} = {a / b}')

# numb_1 = int(input('Enter number --> '))
# numb_2 = int(input('Enter number --> '))
# try:
#     division(numb_1,numb_2)
# except ZeroDivisionError as ex:
#     print(ex)

# Task 2.2
# def division(numb_1, numb_2):
#     try:
#         print(f'{numb_1} / {numb_2} = {numb_1 / numb_2}')
#     except ZeroDivisionError as ex:
#         print(ex)

# numb_1 = int(input('Enter number --> '))
# numb_2 = int(input('Enter number --> '))
# division(numb_1,numb_2)