# this code compares normal gauss seidel and with relaxation

import numpy as np
import time


# at first check diagonal dominance

def is_diagonally_dominant(A):
    n = len(A)
    for i in range(n):
        diag = abs(A[i][i])
        off = sum(abs(A[i][j]) for j in range(n) if j != i)
        if diag < off:
            return False
    return True


# solve with  gauss seidel (ω = 1, no over-relaxation)

def gauss_seidel(A, B, X0, tol, max_iter):
    n = len(A)
    X = X0.copy()
    history = []                     # store last few solutions
    for k in range(max_iter):
        old_X = X.copy()
        for i in range(n):
            s1 = sum(A[i][j] * X[j] for j in range(i))          # use updated values
            s2 = sum(A[i][j] * old_X[j] for j in range(i+1, n)) # use old values
            X[i] = (B[i] - s1 - s2) / A[i][i]
        history.append(X.copy())
        if len(history) > 3:   # keep only last 3
            history.pop(0)
            
        # check if the last 3 solutions are all within 'tol' of each other(meaning almost same)
        if len(history) == 3:
            max_diff = max(np.abs(history[-1] - history[-2]).max(),
                           np.abs(history[-2] - history[-3]).max(),
                           np.abs(history[-1] - history[-3]).max())
            if max_diff < tol:
                break
    else:
        k += 1   # if loop keep adding without break
    return X, k+1
        

# solve with SOR (Successive Over-Relaxation)

def sor_method(A, B, X0, omega, tol, max_iter):
    n = len(A)
    X = X0.copy()
    history = []
    for k in range(max_iter):
        old_X = X.copy()
        for i in range(n):
            s1 = sum(A[i][j] * X[j] for j in range(i))           # updated
            s2 = sum(A[i][j] * old_X[j] for j in range(i+1, n))  # old
            gauss_update = (B[i] - s1 - s2) / A[i][i]
            X[i] = (1 - omega) * old_X[i] + omega * gauss_update
            
        history.append(X.copy())
        if len(history) > 3:
            history.pop(0)

        if len(history) == 3:
            max_diff = max(np.abs(history[-1] - history[-2]).max(),
                           np.abs(history[-2] - history[-3]).max(),
                           np.abs(history[-1] - history[-3]).max())
            if max_diff < tol:
                break
    else:
        k += 1
    return X, k+1


# main


print("LINEAR SYSTEM SOLVER (GaussSeidel & Relaxation)")

# matrix input
n = int(input("How many variables does your system have? "))
A = []
B = []

print("\nEnter the coefficient matrix row by row (space separated):")
for i in range(n):
    row = list(map(float, input(f" Row {i+1}: ").split()))
    A.append(row)

print("\nEnter the right‑hand side constants:")
for i in range(n):
    val = float(input(f" B[{i+1}] = "))
    B.append(val)

A = np.array(A, dtype=float)
B = np.array(B, dtype=float)

#diagonal dominance check
print("\nchecking diagonal dominance ...")
if not is_diagonally_dominant(A):
    print("the matrix is not diagonally dominant.")
    print("The method may not converge.")
    proceed = input("Do you want to continue anyway? (yes/no): ").strip().lower()
    if proceed != 'yes':
        exit()
else:
    print("Matrix is diagonally dominant..!")

#decimal places 

decimals = input("\nHow many decimal places of accuracy you need? (default is 4): ").strip()
if decimals == "":
    decimals = 4
else:
    decimals = int(decimals)
tolerance = 10 ** (-decimals)
print(f"tolerance set to {tolerance}  (10^{{-{decimals}}})")

# max iterations 

use_fixed = input("\nEnter a fixed number of iterations (or press just no for default convergence): ").strip().lower()
if use_fixed == 'yes':
    max_iter = int(input("how many iterations? "))
    fixed_iter = True
    print(f"fixed mode, will run exactly {max_iter} iterations.")
else:
    max_iter = 5000 
    fixed_iter = False
    print("stopped when the last 3 iterations are almost same.")

# relaxation choice

use_relax = input("\n would you like to use the relaxation method (SOR)? (yes/no): ").strip().lower()
omega = 1.0
if use_relax == 'yes':
    omega_input = input(" Relaxation factor ω? (default is 1.25): ").strip()
    if omega_input == "":
        omega = 1.25
    else:
        omega = float(omega_input)
    print(f"   SOR ω = {omega}")
else:
    print(" Using standard gauss seidel (ω = 1).")

# initial guess

X0 = np.zeros(n)

print("start... ")


start_time = time.time()

if use_relax == 'yes':
    # run both methods for comparison
    
    print("\nRunning Gauss seidel (ω = 1) ...")
    X_gs, it_gs = gauss_seidel(A, B, X0, tolerance, max_iter)
    print("Running relaxation (SOR) ...")
    X_sor, it_sor = sor_method(A, B, X0, omega, tolerance, max_iter)
    elapsed = time.time() - start_time

    # comparison
    
    print("comparing when both stopped at the same tolerance")
    print("-" * 10)
    print(f"{'Method':<25} {'Iterations':<12} {'Solution'}")
    print("-" * 10)
    gs_str = ", ".join(f"{v:.{decimals}f}" for v in X_gs)
    sor_str = ", ".join(f"{v:.{decimals}f}" for v in X_sor)
    print(f"{'Gauss‑Seidel (ω=1)':<25} {it_gs:<12} {gs_str}")
    print(f"{'SOR (ω='+str(omega)+')':<25} {it_sor:<12} {sor_str}")
    print("-" * 10)
    print(f"Time taken: {elapsed:.4f} seconds")

else:
    # only gauss seidel
    X_gs, it_gs = gauss_seidel(A, B, X0, tolerance, max_iter)
    elapsed = time.time() - start_time
    print(f"\nGauss‑Seidel completed in {it_gs} iterations.")
    print("Solution:")
    for i in range(n):
        print(f"  x{i+1} = {X_gs[i]:.{decimals}f}")
    print(f"Time taken: {elapsed:.4f} seconds")
