import numpy as np
import time

# Input section
n = int(input("Enter number of variables: "))

A = []
B = []

print("\nEnter coefficient matrix row-wise:")

for i in range(n):
    row = list(map(float, input(f"Row {i+1}: ").split()))
    A.append(row)

print("\nEnter constants vector:")

for i in range(n):
    value = float(input(f"B[{i+1}] = "))
    B.append(value)

A = np.array(A, dtype=float)
B = np.array(B, dtype=float)

L = np.zeros((n, n))
U = np.zeros((n, n))

start = time.time()

# LU Decomposition
for i in range(n):

    # Upper triangular matrix
    for k in range(i, n):

        sum1 = 0

        for j in range(i):
            sum1 += L[i][j] * U[j][k]

        U[i][k] = A[i][k] - sum1

    # Lower triangular matrix
    L[i][i] = 1

    for k in range(i + 1, n):

        sum2 = 0

        for j in range(i):
            sum2 += L[k][j] * U[j][i]

        L[k][i] = (A[k][i] - sum2) / U[i][i]

print("\nMatrix L:")
print(L)

print("\nMatrix U:")
print(U)

# Forward substitution: LY = B
Y = np.zeros(n)

for i in range(n):

    sum3 = 0

    for j in range(i):
        sum3 += L[i][j] * Y[j]

    Y[i] = B[i] - sum3

# Back substitution: UX = Y
X = np.zeros(n)

for i in range(n - 1, -1, -1):

    sum4 = 0

    for j in range(i + 1, n):
        sum4 += U[i][j] * X[j]

    X[i] = (Y[i] - sum4) / U[i][i]

end = time.time()

print("\nSolution Vector:")

for i in range(n):
    print(f"x{i+1} = {X[i]}")

print("\nTime Taken =", end - start, "seconds")