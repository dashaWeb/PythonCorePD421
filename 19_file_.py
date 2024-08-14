# відкрити файл
# прочитати файл
# виконати запис у файл
# закрити файл


# --------------- Read file -----------------
# url = r"C:\Users\konopelko\Desktop\PythonCore_PD421\19_file\my_read.txt"

# fileHandler = open(url)
# print(type(fileHandler), fileHandler)
# text = fileHandler.read()
# print(text, type(text),sep='\n')
# fileHandler.close()


# fileHandler = open(url)
# text = fileHandler.read(15)
# print(text, type(text),sep='\n')

# fileHandler.seek(0)
# text = fileHandler.readline()
# print(text, type(text),sep='\n')


# fileHandler.seek(0)
# for line in fileHandler:
#     print(line)

# fileHandler.seek(0)
# lines = fileHandler.readlines()
# print(lines[0], type(text),sep='\n')

# fileHandler.close()

# file = None
# try:
#     file = open(r'test.txt')
#     print(file.read())
# except FileNotFoundError as ex:
#     print(ex)
# finally:
#     file.close()

# with open(url) as file:
#     print(file.read())


# ----------------- Write file ---------------------

# word = "World"
# url = r'19_file/my_write.txt'
# with open(url,'w') as file:
#     file.write(word)

# word = 'Привіт'
# url = r'19_file/my_write_app_ua.txt'
# # with open(url,'a',encoding='utf-8') as file:
# #     file.write(word)
# with open(url,'r',encoding='utf-8') as file:
#     print(file.read())


def readFileAll(url):
    with open(url) as file:
        return file.read()
    
# def writeLines(url,lines,mode='w'):
#     with open(url,mode) as file:
#         for line in lines:
#             file.write(line)

def writeLines(url,lines,mode='w'):
    with open(url,mode) as file:
        file.writelines(lines)

# print(readFileAll(r'19_file/my_read.txt'))
# print(readFileAll(r'19_file/my_write.txt'))

# writeLines('19_file/test_func.txt',['line 1 \n', 'line 2 \n', 'line 3 \n'])
# writeLines('19_file/test_func.txt',['line 4 \n', 'line 5 \n'],'a')