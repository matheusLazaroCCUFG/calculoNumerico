import numpy as np

def matrizHilbert(n):
    H = np.zeros((n, n))
    for i in range(1, n+1):
        for j in range(1, n+1):
            H[i-1, j-1] = 1 / (i + j - 1)
    return H

H5 = np.array([
    [1,     1/2,    1/3,    1/4,    1/5],
    [1/2,   1/3,    1/4,    1/5,    1/6],
    [1/3,   1/4,    1/5,    1/6,    1/7],
    [1/4,   1/5,    1/6,    1/7,    1/8],
    [1/5,   1/6,    1/7,    1/8,    1/9],
])

# cond = np.linalg.cond(H5)
# print(cond)

for i in range(2, 11):
    # print("Matriz:")
    H = matrizHilbert(i)
    print("n = ", i)
    print("Cond = ",np.linalg.cond(H, 2))