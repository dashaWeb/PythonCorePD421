import random


def showMessage():
    print('Hello World')


showMessage()


def lmbMessage(): return print("Hello Lambda")


lmbMessage()


def sum_n(a, b):
    return a + b


def sum_numb(a, b): return a + b


res = sum_numb(5, 7)
print(sum_numb(3, 10))


def printList(list):
    for item in list:
        print(item, end='\t')
    print()


numbers = [random.randint(-20, 20) for i in range(10)]

printList(numbers)
def numb2(x):
    return x * 2


def revers_numb(list):
    clone = list.copy()
    for i in range(len(list)):
        clone[i] = numb2(clone[i])
    return clone


clone = revers_numb(numbers)
printList(clone)


print('-'*50)


def numb(x):
    return x * -1

print('Map')
test_map = list(map(numb, numbers))
printList(test_map)
test_map_lmb = list(map(lambda x: x*2, numbers))
printList(test_map_lmb)
print('-'*50)
print('Filter')
printList(test_map)
positive_numb = list(filter(lambda x: x>0,test_map))
printList(positive_numb)
even_numb = list(filter(lambda x: x%2==0 and x>0,test_map))
printList(even_numb)