import random
matrix = [[random.randint(1,20)for j in range(4)] for i in range(3)]
for row in matrix:
    sum1 = sum(row)
    row.append(sum1)

for row in matrix:
    for j in row:
        print(end="\t")
    print()






for i in matrix:
    for j in i:
        print(j,end='\t')
    print()