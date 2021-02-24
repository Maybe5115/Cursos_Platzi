import numpy as np

def gradF(z):
    return np.array([1-np.exp(z[1]-z[0]), np.exp(z[1]-z[0])])

z = np.array([1,2])
print("Grad F ", gradF(z))

def F(x):
    return x[0] + np.exp(x[1]-x[0])

print("F 1,2 ", F(z))

def taylor_F(x,z):
    fz = F(z)
    gz = gradF(z)
    return fz + gz@(x-z)

print("Taylor ", taylor_F(z, z))

