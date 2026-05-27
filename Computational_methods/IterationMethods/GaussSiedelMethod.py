import numpy as np
import time

# function to check diagonal dominant or not
def is_diagonally_dominant(A):
    n = len(A)

    for i in range(n):
        diagonal = abs(A[i][i])
        others = sum(abs(A[i][j]) for j in range(n) if j != i)

        if diagonal < others:
            return False

    return True


# input from user
n = int(input("Enter number of variables presents in equation: "))

A = []
B = []

print("\nEnter coefficient matrix row-wise with space:")

for i in range(n):
    row = list(map(float, input(f"Row {i+1}: ").split()))
    A.append(row)

print("\nEnter constants vector:")

for i in range(n):
    value = float(input(f"B[{i+1}] = "))
    B.append(value)

A = np.array(A)
B = np.array(B)

# check diagonal dominance
print("\nChecking diagonal dominant...")

if is_diagonally_dominant(A):
    print("Matrix is diagonally dominant.")
else:
    print("Matrix is not diagonally dominant.")
    print("Gauss-Seidel method may not converge.")
    exit()

# initial guess
X = np.zeros(n)

tolerance = 0.0001
max_iterations = 100

iteration_input = input(
    "\nEnter number of iterations (Press Enter for default convergence): "
)

start = time.time()

print("\nIteration Process:\n")


# CASE 1: if user provides number of iterations


if iteration_input != "":

    iterations = int(iteration_input)

    for k in range(iterations):

        for i in range(n):

            s1 = 0
            s2 = 0

            for j in range(i):
                s1 += A[i][j] * X[j]

            for j in range(i + 1, n):
                s2 += A[i][j] * X[j]

            X[i] = (B[i] - s1 - s2) / A[i][i]

        print(f"Iteration {k+1}: {X}")

# CASE 2: by default


else:

    print("automatic convergence.\n")

    for k in range(max_iterations):

        old_X = X.copy()

        for i in range(n):

            s1 = 0
            s2 = 0

            for j in range(i):
                s1 += A[i][j] * X[j]

            for j in range(i + 1, n):
                s2 += A[i][j] * X[j]

            X[i] = (B[i] - s1 - s2) / A[i][i]

        print(f"Iteration {k+1}: {X}")

        # Convergence check
        if np.all(np.abs(X - old_X) < tolerance):

            print("\nSolution converged automatically.")
            break

end = time.time()

print("\nApproximate solution:")

for i in range(n):
    print(f"x{i+1} = {X[i]}")

print("\nTotal iterations used =", k + 1)

print("\nTime Taken =", end - start, "seconds")