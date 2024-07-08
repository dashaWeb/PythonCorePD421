# matx = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
# mtrx_3D = [
#     [
#         [1,2,3],
#         [4,5,6]
#     ],
#     [
#         [7,8,9]
#     ]
# ]
# print(mtrx_3D[0][1][1])
import random

# fill matrix
# way 1
# matrix = []
# for i in range(3):
#     row = []
#     for j in range(5):
#         row.append(random.randint(1,50))
#     matrix.append(row)

# way 2
row,col = 5,7
matrix = [[random.randint(1,20) for j in range(col)] for i in range(row)] # [0,2,4]
# print(matrix)
# matrix = [
#     [18],
#     [8],
#     [3]
# ]
# print(matrix[1][0])
# print matrix
for row in matrix:
    for num in row:
        print(num,end='\t')
    print()

# sum_ = 0
# # for i in range(3): 
# #     for j in range(5):
# #         sum_ += matrix[i][j]

# for i in range(3): 
#     sum_ += sum(matrix[i])

# # print(f"Sum all :: {sum_}")
# # sum_ = sum(matrix[0]) Error
# print(f"Sum all :: {sum_}")

# max_ = matrix[0][0]
# min_ = matrix[0][0]
# for i in range(3):
#     for j in range(5):
#         if max_ < matrix[i][j]:
#             max_ = matrix[i][j]
#         if min_ > matrix[i][j]:
#             min_ = matrix[i][j]
# print(f"Max :: {max_}")
# print(f"Min :: {min_}")

# max_ = max(matrix[0])
# min_ = min(matrix[0])
# for i in range(1,3):
#     if max_ < max(matrix[i]):
#         max_ = max(matrix[i])
#     if min_ > min(matrix[i]):
#         min_ = min(matrix[i])

# min_ = []
# max_ = []
# for row in matrix:
#     min_.append(min(row))
#     max_.append(max(row))

# print(f"Max :: {max(max_)}")
# print(f"Min :: {min(min_)}")

min_ = min([min(row) for row in matrix])
max_ = max([max(row) for row in matrix])
print(f"Max :: {max_}")
print(f"Min :: {min_}")


copy_matrix = []

for row in matrix:
    copy_matrix.append(row.copy())

print(id(matrix),matrix,sep='\n')
print()
print(id(copy_matrix),copy_matrix,sep='\n')

print()
copy_matrix[0][0] = 33
print(id(matrix),matrix,sep='\n')
print()
print(id(copy_matrix),copy_matrix,sep='\n')

for i in range(3):
    print(f'copy :: {id(matrix[i])}; origin :: {id(copy_matrix[i])}')

    