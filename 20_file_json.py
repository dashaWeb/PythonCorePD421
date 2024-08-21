# import json

# stud = {
#     'name':'Igor',
#     'surname':'Bondar',
#     'age':15
#     }

# print(type(stud), stud)
# json_serial = json.dumps(stud)
# print(type(json_serial), json_serial)

# with open('20_file_obj/students.txt','w') as file:
#     file.write(json_serial)


students = [
    {'name':'Pasha' , 'age':16},
    {'name':'Olia' , 'age':15},
    {'name':'Oleg' , 'age':17},
]

students = sorted(students, key = lambda x :x['name'])
print(students)
# print(type(students), students)
# students_string = json.dumps(students)

# with open('20_file_obj/students_list.json','w') as file:
#     file.write(students_string)

# read json file

# with open('20_file_obj/students.txt') as file:
#     res_student = file.read()
# print(res_student, type(res_student))
# obj_student = json.loads(res_student)
# obj_student = dict(obj_student)
# print(obj_student, type(obj_student))
# print(obj_student['name'])

# for key, value in obj_student.items():
#     print(key, value)


# with open('20_file_obj/students_list.json') as file:
#     res_student = file.read()
# print(res_student, type(res_student))
# obj_student = json.loads(res_student)
# print(obj_student, type(obj_student))
# for item in obj_student:
#     print(item)

# obj_student.append({'name':'Sasha','age':14})
# print()
# for item in obj_student:
#     print(item)



# -------------------------------------------------------
# import requests
# import json
# # result = requests.get('https://api.privatbank.ua/p24api/pubinfo?exchange&coursid=5').json()
# # # result = json.loads(result.content)

# # print(result, type(result))
# # print(result[0]['sale'])


# # img = requests.get('https://cdn.creatureandcoagency.com/uploads/2021/03/nature-3238564.png').content
# # with open('20_file_obj/spring.png','wb') as file:
# #     file.write(img)

# url = 'https://pixabay.com/api/?key=14304821-db198647e0592cf253911c94a&q=yellow+animals&image_type=photo&pretty=true&per_page=50'
# images = requests.get(url).json()
# images = images['hits']
# counter = 1

# for img in images:
#     picture = requests.get(img['webformatURL']).content
#     with open(f'20_file_obj/{counter}.jpg', 'wb') as file:
#         file.write(picture)
#     counter+=1
