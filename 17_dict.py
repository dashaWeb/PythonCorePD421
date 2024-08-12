
stud = {
    'name':'Oleg',
    'age':24,
    'group':'PD421'
}
print(stud, type(stud), len(stud))

stud_2 = dict(name='Sasha',age=22,group = 'PV421')
print(stud_2, type(stud_2), len(stud_2))

print(stud['name']) # get value
print(stud_2['name'])
# print(stud['surname'])
print(stud.get('surname'))

print(stud.setdefault('name'))
print(stud.setdefault('surname'))
print(stud)

stud.update([('name','Pasha'), ('birthday','24.01.02')])
print(stud)

stud['name'] = 'Masha'
print(stud)
stud['rating'] = 10.0
print(stud)

del stud['surname']
print(stud)

stud.pop('group')
print(stud)

stud.popitem()
print(stud)

for key in stud.keys():
    print(key,end='\t')
print()

for key in stud.values():
    print(key,end='\t')
print()

for key,val in stud.items():
    print(key, val)
print()

clone = stud.copy()
print(clone)
print(stud)

stud.clear()

print(clone.keys())
new_stud = {}.fromkeys(clone.keys())
print(new_stud)

group = [
    {
        'name':'Pasha',
        'age':22
    },
    {
        'name':'Oleg',
        'age':20
    },
    {
        'name':'Petro',
        'age':19
    }
]

for stud in group:
    stud['name'] = stud['name'].upper()
    for key, val in stud.items():
        print(f'{key} :: {val}')

