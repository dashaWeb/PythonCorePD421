
directory = '21_binary_file'
filename_t = 'file.txt'
filename_b = 'file.dat'
filename_j = 'file.json'

text = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque eget velit euismod, feugiat sem eget, semper lorem. Suspendisse eget venenatis felis, in congue turpis. Mauris sagittis, nibh gravida sollicitudin lobortis, purus ipsum ullamcorper augue, a rhoncus massa purus nec massa. Nulla mattis, ligula sit amet malesuada posuere, dui ante imperdiet libero, quis elementum nisi dui vitae felis. Nulla quis ipsum sit amet felis elementum varius accumsan sed nisl. Mauris metus enim, auctor sit amet turpis at, sagittis malesuada lectus. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Donec imperdiet, turpis at posuere consectetur, leo massa feugiat tortor, nec mattis libero massa eget orci. Duis quis leo sapien. Nam dictum pellentesque libero, et cursus felis dapibus vel. Sed congue accumsan mi, vitae fermentum enim pellentesque quis. Suspendisse dignissim ipsum id metus euismod, nec sodales ex pellentesque. Vestibulum ultricies, tellus aliquam auctor lobortis, dolor lacus pharetra tellus, non dignissim nulla purus at nunc.'

list_ = ['red', 'green', 'blue', 'pink', 'orange', 'brown', 'black', 'yellow']

dict_ = {'name': 'table', 'width': 1000,
         'height': 1500, 'length': 750, 'color': 'white'}

users = [{
    "first_name": "Dal",
    "last_name": "Toppas",
    "email": "dtoppas0@amazon.co.uk",
    "birthday": "27.01.2022"
}, {
    "first_name": "Millisent",
    "last_name": "Itzkov",
    "email": "mitzkov1@ucoz.com",
    "birthday": "23.02.2023"
}, {
    "first_name": "Jarrett",
    "last_name": "Greatbanks",
    "email": "jgreatbanks2@jimdo.com",
    "birthday": "07.03.2022"
}, {
    "first_name": "Jodi",
    "last_name": "Huge",
    "email": "jhuge3@issuu.com",
    "birthday": "07.03.2023"
}, {
    "first_name": "Lilia",
    "last_name": "Brinson",
    "email": "lbrinson4@cargocollective.com",
    "birthday": "04.05.2023"
}, {
    "first_name": "Alyda",
    "last_name": "Maytum",
    "email": "amaytum5@yahoo.co.jp",
    "birthday": "01.12.2023"
}, {
    "first_name": "Erroll",
    "last_name": "Bohden",
    "email": "ebohden6@wufoo.com",
    "birthday": "06.08.2023"
}, {
    "first_name": "Wendie",
    "last_name": "McHarry",
    "email": "wmcharry7@vinaora.com",
    "birthday": "03.07.2023"
}, {
    "first_name": "Gale",
    "last_name": "Ree",
    "email": "gree8@usatoday.com",
    "birthday": "15.09.2023"
}, {
    "first_name": "Camellia",
    "last_name": "Raistrick",
    "email": "craistrick9@nsw.gov.au",
    "birthday": "26.06.2022"
}
]

def printUsers(users):
    for user in users:
        print(user)

printUsers(users)
filter_users = list(filter(lambda x: int(x['birthday'].split('.')[0]) > 15, users))
print()
printUsers(filter_users)

sorted_users = sorted(users,key=lambda x:x['first_name'])
print()
printUsers(sorted_users)

def filter_map(user):
    if int(user['birthday'].split('.')[0]) > 15:
        user['email']+='*'
        return user
    return user

map_users = list(map(filter_map,users))
print()
printUsers(map_users)

# import pickle

# with open(f'{directory}/{filename_t}','w') as file:
#     file.write(text)

# with open(f'{directory}/{filename_b}','wb') as file:
#     pickle.dump(text,file)
#     print(pickle.dumps(text))


# with open(f'{directory}/{filename_t}','w') as file:
#     file.write(str(list_))

# with open(f'{directory}/{filename_b}','wb') as file:
#     pickle.dump(list_,file)
#     # print(pickle.dumps(text))


# with open(f'{directory}/{filename_t}','w') as file:
#     file.write(str(dict_))

# with open(f'{directory}/{filename_b}','wb') as file:
#     pickle.dump(dict_,file)
#     # print(pickle.dumps(text))


# with open(f'{directory}/{filename_t}','w') as file:
#     file.write(str(users))

# with open(f'{directory}/{filename_b}','wb') as file:
#     pickle.dump(users,file)
    # print(pickle.dumps(text))

# with open(f'{directory}/{filename_b}','rb') as file:
#     res_users = pickle.load(file)
#     print(type(res_users))
#     for user in res_users:
#         print(user,type(user))

