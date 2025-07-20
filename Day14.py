# create a 3x3 matrix of numbers print it row by row unsing nested loops
matrix = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]
for row in matrix:
    print(row)

for row in matrix:
    for col in row:
        print(col) 

# print only the elements in second colum
for col in matrix:
    print(col[1])

# print the diagonal elements of the matrix
for i in range(len(matrix)):
    print(matrix[i][i])

# count how many odd numbers are in matrix
for row in matrix:
    for number in row:
        if number % 2 != 0:
            print(number)

