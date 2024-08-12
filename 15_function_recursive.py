'''
!5 = 5 * !4
!4 = 4 * !3
!3 = 3 * !2
!2 = 2 * !1
!1 = 1
!0 = 1 
'''


def factorial(number):
    if number == 0 or number == 1:
        return 1
    return number * factorial(number-1)


print(factorial(5))


# 1 - 10 (sum)
# 1 + 2-10
# 2 + 3 - 10
# 3 + 4 - 10
def sumRange(a, b):
    if a == b:
        return a
    return a + sumRange(a+1, b)


print(sumRange(1, 10))

# 2^4 --> 2 * 2^3
# 2^3 --> 2 * 2^2
# 2^2 --> 2 * 2^1
# 2^1 --> 2

def powRec(numb, pow):
    if pow == 1:
        return numb
    return numb * powRec(numb, pow -1)



print(powRec(2, 4))


# def star(n):
#     if n == 0:
#         return None
#     print('*',end='')
#     star(n-1)

def star(n):
    if n > 0:
        print('*',end='')
        star(n-1)
star(5)
