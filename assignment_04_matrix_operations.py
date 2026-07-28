def matrix_operations(matrix_a, matrix_b):
    # Addition
    addition = [[matrix_a[i][j] + matrix_b[i][j] for j in range(len(matrix_a[0]))] for i in range(len(matrix_a))]
    
    # Subtraction
    subtraction = [[matrix_a[i][j] - matrix_b[i][j] for j in range(len(matrix_a[0]))] for i in range(len(matrix_a))]
    
    return addition, subtraction

if _name_ == "__main__":
    print("Matrix operations initialized.")
