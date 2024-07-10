import math


def printMessage(name='User'):
    print(f"Hello {name}")

# printMessage('Igor')
# printMessage('Sasha')
# # name = input('Enter name --> ')
# # printMessage(name)


# printMessage()

def sumNum(a, b):
    return a + b


def subNum(a, b):
    return a - b


def multNum(a, b):
    return a * b


def divNum(a, b):
    if b == 0:
        print('Error. division by zero')
    else:
        return a / b


def calculate(a=0, b=0, op=' '):
    match op:
        case '+':
            return sumNum(a, b)
        case '-':
            return subNum(a, b)
        case '*':
            return multNum(a, b)
        case '/':
            return divNum(a, b)


def getOperation(line):
    if line.find('+') != -1:
        return '+'
    if line.find('-') != -1:
        return '-'
    if line.find('*') != -1:
        return '*'
    if line.find('/') != -1:
        return '/'

# reg = input(' Enter ex (2 + 2) > ') # 2 + 3
# op = getOperation(reg)
# numb = [float(item) for item in reg.split(op)]
# print(numb)
# print(f'{reg} = {calculate(op=op,b = numb[1], a = numb[0])}')


def minTest(*args):
    min_ = args[0]
    for item in args:
        if min_ > item:
            min_ = item
    return min_


# def calcNumb(op, *args):
    # if op == '+':
    #     sum_ = args[0]
    #     for i in range(1, len(args)):
    #         sum_ += args[i]
    #     return sum_
    # if op == '-':
    #     sub_ = args[0]
    #     for i in range(1, len(args)):
    #         sub_ -= args[i]
    #     return sub_
    # if op == '*':
    #     mult_ = args[0]
    #     for i in range(1, len(args)):
    #         mult_ *= args[i]
    #     return mult_
    #     res = args[0]
    #     for i in range(1, len(args)):
    #         if op == '+':
    #             res += args[i]
    #         elif op == '-':
    #             res -= args[i]
    #         elif op == '*':
    #             res *= args[i]
    #     return res

    # print(calcNumb('+', 1, 2, 5, 4, 7, 8, 5, 4))

print('Ceil',math.ceil(3.2))
print('Fllor',math.floor(3.9))
print('sqrt',math.sqrt(4))