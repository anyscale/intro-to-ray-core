from itertools import product

def perform_naive_matrix_multiplication(n):
    matrix1 = matrix2 = [[1 for _ in range(n)] for _ in range(n)]

    result = [[0 for _ in range(n)] for _ in range(n)]
    for i, j, k in product(range(n), range(n), range(n)):
        result[i][j] += matrix1[i][k] * matrix2[k][j]

    return result
