import numpy as np

# Take input for matrix dimensions
n = int(input("Enter number of rows: "))
m = int(input("Enter number of columns: "))

# Take input for matrix entries
matrix = []
for i in range(n):
    row = input("Enter row {} separated by spaces: ".format(i+1))
    row = list(map(float, row.split()))
    matrix.append(row)

# Convert the list of lists to NumPy array
matrix = np.array(matrix)

# Check for linear dependency
rank = np.linalg.matrix_rank(matrix)
if rank < min(n, m):
    print("The matrix is linearly dependent.")
else:
    print("The matrix is linearly independent")
