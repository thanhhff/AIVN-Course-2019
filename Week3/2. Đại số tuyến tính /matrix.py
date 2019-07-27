import numpy as np

def matrix_multiplication(matrix1, matrix2):
    matrix1_nrows = len(matrix1)
    matrix1_ncols = len(matrix1[0])

    matrix2_nrows = len(matrix2)
    matrix2_ncols = len(matrix2[0])

    result = [[0]*matrix2_ncols for i in range(matrix1_nrows)]
    for i in range(matrix1_nrows):
        for j in range(matrix2_ncols):
            for k in range(matrix2_nrows):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    
    return result

# matrix 3x3
matrix1 = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]

# matrix 3x4
matrix2 = [[1, 1, 2, 1],
           [1, 2, 1, 1],
           [1, 1, 1, 2]]

print(matrix_multiplication(matrix1, matrix2))
