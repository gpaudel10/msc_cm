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


# taking input
n = int(input("Enter number of variables: "))

A = []
B = []

print("\nEnter coefficients row wise with space:")

for i in range(n):
    row = list(map(float, input(f"Enter row {i+1}: ").split()))
    A.append(row)

print("\nEnter constants vector:")

for i in range(n):
    value = float(input(f"B[{i+1}] = "))
    B.append(value)

A = np.array(A)
B = np.array(B)

# to check diagonal dominant
print("\nChecking diagonal dominance...")

if is_diagonally_dominant(A):
    print("Matrix is diagonally dominant.")
else:
    print("Matrix is not diagonally dominant.")
    print("Jacobi Method may not converge.")
    exit()

# tolerance value to match for convergence
tolerance = 0.0001

# safety limit for maximum iterations
max_iterations = 100

# input from user
iteration_input = input(
    "\nEnter number of iterations (or press Enter for automatic convergence): "
)

start = time.time()

print("\nIteration process:\n")

# so initial guess
X = np.zeros(n)


# CASE 1: if user provides number of iterations

if iteration_input != "":

    iterations = int(iteration_input)

    for k in range(iterations):

        X_new = np.zeros(n)

        for i in range(n):

            s = 0

            for j in range(n):

                if i != j:
                    s += A[i][j] * X[j]

            X_new[i] = (B[i] - s) / A[i][i]

        print(f"Iteration {k+1}: {X_new}")

        X = X_new.copy()

# CASE 2: else automatic convergence 

else:

    print("automatic convergence.\n")

    for k in range(max_iterations):

        X_new = np.zeros(n)

        for i in range(n):

            s = 0

            for j in range(n):

                if i != j:
                    s += A[i][j] * X[j]

            X_new[i] = (B[i] - s) / A[i][i]

        print(f"Iteration {k+1}: {X_new}")

        # Convergence check
        if np.all(np.abs(X_new - X) < tolerance):

            print("\nSolution converged here.")
            break

        X = X_new.copy()

end = time.time()

print("\nApproximate solution:")

for i in range(n):
    print(f"x{i+1} = {X_new[i]}")

print("\nTotal Iterations =", k + 1)

print("\nTime Taken =", end - start, "seconds")