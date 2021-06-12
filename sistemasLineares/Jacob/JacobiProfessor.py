import numpy as np

def jacobi(A,b,tol,nitmax):
    n=len(A)
    x=np.zeros(n)
    D=np.zeros([n,n])
    for i in range(n):
        D[i,i]=A[i,i]
    F=A-D
    invD=np.linalg.inv(D)
    nit=0
    while np.linalg.norm(np.dot(A,x)-b) > tol:
        x=-np.dot(invD,np.dot(F,x))+np.dot(invD,b)
        nit=nit+1
        if nit==nitmax:
            print("número de iterações máximas atingido")
            break
    return (x, nit)

A=np.array([[5.0,1,1],[3,4,1],[3,3,6]])
b=np.array([5.0,6,0])
tol=1e-8
nitmax=60
(x, nit)=jacobi(A,b,tol,nitmax)
print("A solução é: ", x)
print("O número de iterações realizadas é:", nit)