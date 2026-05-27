import numpy as np
import time

# Function to check tridiagonal matrix
def is_tridiagonal(A):
    n = len(A)

    for i in range(n):
        for j in range(n):

            if abs(i - j) > 1 and A[i][j] != 0:
                return False

    return True


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

# Check tridiagonal
print("\nChecking whether matrix is tridiagonal...")

if is_tridiagonal(A):
    print("Matrix is tridiagonal.")
else:
    print("Matrix is NOT tridiagonal.")
    print("Thomas Algorithm cannot be applied.")
    exit()

# Extract diagonals
a = np.zeros(n)
b = np.zeros(n)
c = np.zeros(n)

for i in range(n):
    b[i] = A[i][i]

    if i > 0:
        a[i] = A[i][i - 1]

    if i < n - 1:
        c[i] = A[i][i + 1]

start = time.time()

# Forward elimination
for i in range(1, n):

    factor = a[i] / b[i - 1]

    b[i] = b[i] - factor * c[i - 1]
    B[i] = B[i] - factor * B[i - 1]

# Back substitution
X = np.zeros(n)

X[n - 1] = B[n - 1] / b[n - 1]

for i in range(n - 2, -1, -1):
    X[i] = (B[i] - c[i] * X[i + 1]) / b[i]

end = time.time()

print("\nSolution Vector:")

for i in range(n):
    print(f"x{i+1} = {X[i]}")

print("\nTime Taken =", end - start, "seconds")