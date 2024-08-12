# import msvcrt
# import os

# while True:
#     key = ord(msvcrt.getch())
#     print(key)
#     if key == 27:
#         break
    




def reverse(numb):
    line = str(numb)
    if numb < 10:
        return str(numb)
    return line[-1] + reverse(numb//10)

print(reverse(123456))
































