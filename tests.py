from matrix_class import Matrix

matrix1 = Matrix([[1,2,3],
                 [4,5,6],
                 [7,8,9]])


matrix2 = matrix1

matrix3 = matrix1 + matrix2

matrix3 = matrix1 * matrix2

print(matrix3)

for row in matrix3:
    print(row)