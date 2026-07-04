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

#  input section 
n = int(input("Enter number of variables: "))

A = []
B = []

print("\nEnter coefficient matrix row wise:")
for i in range(n):
    row = list(map(float, input(f"Row {i+1}: ").split()))
    A.append(row)

print("\nEnter constants(RHS values):")
for i in range(n):
    value = float(input(f"B[{i+1}] = "))
    B.append(value)

A = np.array(A, dtype=float)
B = np.array(B, dtype=float)

# to heck whether the given system is tridiagonal or not

if is_tridiagonal(A):
    print("Matrix is tridiagonal.")
else:
    print("Matrix is not tridiagonal.")
    print("Thomas algorithm cannot be applied.")
    exit()

# to hold diagonals and constants 
a = np.zeros(n) # lower diagonal
b = np.zeros(n) # main diagonal
c = np.zeros(n) # upper diagonal
d = np.copy(B)  # constants (right hand side)

for i in range(n):
    b[i] = A[i][i]
    if i > 0:
        a[i] = A[i][i - 1]
    if i < n - 1:
        c[i] = A[i][i + 1]

start = time.time()

# arrays to hold  alpha, beta and final answers
alpha = np.zeros(n)
beta = np.zeros(n)
U = np.zeros(n) 

# STEP 1: forward Elimination for alpha we do
alpha[0] = b[0]
for i in range(1, n):
    alpha[i] = b[i] - (a[i] * c[i - 1]) / alpha[i - 1]

# STEP 2: forward elimination for beta we do 
beta[0] = d[0] / alpha[0]
for i in range(1, n):
    beta[i] = (d[i] - a[i] * beta[i - 1]) / alpha[i]

#STEP 3: we do backward substitution for unknowns (U) 
U[n - 1] = beta[n - 1] # starting with the last variable
for i in range(n - 2, -1, -1): # counting backwards to 0
    U[i] = beta[i] - (c[i] * U[i + 1]) / alpha[i]

end = time.time()

# conclusion
print("\n solutions are:")
for i in range(n):
    # based on number of variables given  U[0]=x, U[1]=y, U[2]=z like this.....
    print(f"variable {i+1} = {U[i]:.4f}")

print("\ntime taken =", end - start, "seconds")