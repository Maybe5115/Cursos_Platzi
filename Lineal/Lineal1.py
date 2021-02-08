
import numpy as np


a = np.array([1, 0, 0, 0])
b = np.array([0, 1, 0, 0])

print(np.dot(a,b))
print(a.T@b)

def p(x):
    return  np.array([1,2])@np.array([1,x])

print(p(5))