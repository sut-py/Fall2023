import numpy as np

n, m = input().split()
n = int(n)
m = int(m)
matrices = []

for i in range(n):
    matrix = np.zeros((m, m))
    for j in range(m):
        row = input()
        for k in range(m):
            matrix[j, k] = row.split()[k]
    matrices.append(matrix)

x, y = 0, 0
greatest_determinant = -float('inf')
for i in range(n):
    for j in range(i + 1, n):
        current_determinant = np.linalg.det(
            matrices[i]) * np.linalg.det(matrices[j])
        if current_determinant > greatest_determinant:
            greatest_determinant = current_determinant
            x = i
            y = j

product_matrix = np.zeros((m, m))
if np.linalg.det(matrices[x]) >= np.linalg.det(matrices[y]):
    product_matrix = np.matmul(matrices[x], matrices[y])
else:
    product_matrix = np.matmul(matrices[y], matrices[x])

inverse_matrix = np.linalg.inv(product_matrix)

for i in range(m):
    for j in range(m):
        print("%.3f" % inverse_matrix[i, j], end="")
        if j == m - 1:
            print("\n", end="")
        else:
            print(" ", end="")