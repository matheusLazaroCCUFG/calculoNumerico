import numpy as np

def forward_substitution(L, b):
    #source https://johnfoster.pge.utexas.edu/numerical-methods-book/LinearAlgebra_LU.html
    #Get number of rows
    n = len(L)
    #Allocating space for the solution vector
    y = np.zeros_like(b, dtype=np.double);
    #Here we perform the forward-substitution.
    #Initializing  with the first row.
    y[0] = b[0] / L[0, 0]
    #Looping over rows in reverse (from the bottom  up),
    #starting with the second to last row, because  the
    #last row solve was completed in the last step.
    for i in range(1, n):
        y[i] = (b[i] - np.dot(L[i,:i], y[:i])) / L[i,i]
    return y

def back_substitution(U, y):
    #source https://johnfoster.pge.utexas.edu/numerical-methods-book/LinearAlgebra_LU.html
    #Number of rows
    n = len(U)
    #Allocating space for the solution vector
    x = np.zeros_like(y, dtype=np.double);
    #Here we perform the back-substitution.
    #Initializing with the last row.
    x[-1] = y[-1] / U[-1, -1]
    #Looping over rows in reverse (from the bottom up),
    #starting with the second to last row, because the
    #last row solve was completed in the last step.
    for i in range(n-2, -1, -1):
        x[i] = (y[i] - np.dot(U[i,i:], x[i:])) / U[i,i]
    return x

def plu(A):
    #source pge.utexas.edu/numerical-methods-book/LinearAlgebra_LU.html
    #Get the number of rows
    n = len(A)
    #Allocate space for P, L, and U
    U = A.copy()
    L = np.eye(n, dtype=np.double)
    P = np.eye(n, dtype=np.double)
    #Loop over rows
    for i in range(n):
        #Permute rows if needed
        for k in range(i, n):
            if ~np.isclose(U[i, i], 0.0):
                break
            U[[k, k+1]] = U[[k+1, k]]
            P[[k, k+1]] = P[[k+1, k]]
        #Eliminate entries below i with row
        #operations on U and #reverse the row
        #operations to manipulate L
        factor = U[i+1:, i] / U[i, i]
        L[i+1:, i] = factor
        U[i+1:] -= factor[:, np.newaxis] * U[i]
    return P, L, U

def plu_inverse(A):
    #source: https://johnfoster.pge.utexas.edu/numerical-methods-book/LinearAlgebra_LU.html
    n = len(A)
    b = np.eye(n)
    Ainv = np.zeros((n, n))
    P, L, U = plu(A)
    for i in range(n):
        y = forward_substitution(L, np.dot(P, b[i, :]))
        Ainv[i, :] = back_substitution(U, y)
    # return Ainv
    print(Ainv)

A = np.array(
    [
        [4,     -1,     0,      -1,     0,      0],
        [-1,    4,      -1,     0,      -1,     0],
        [0,     -1,     4,      0,      0,      -1],
        [-1,    0,      0,      4,      -1,     0],
        [0,     -1,     0,      -1,     4,      -1],
        [0,     0,      -1,     0,      -1,     4]
    ]
)

plu_inverse(A)