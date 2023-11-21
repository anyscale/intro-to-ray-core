
def perform_naive_matrix_multiplication(n):
    """Performs naive matrix multiplication of two n x n matrices."""
    # Create two n x n matrices
    matrix1 = [[1 for _ in range(n)] for _ in range(n)]
    matrix2 = [[1 for _ in range(n)] for _ in range(n)]

    # Perform matrix multiplication using nested for loops
    # O(n^3) time complexity
    result = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += matrix1[i][k] * matrix2[k][j]

    return result
