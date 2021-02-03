
rojo = [255, 0, 0]
verde = [0, 255, 0]
azul = [0, 0, 255]
negro = [0, 0, 0]

print(len(negro+azul))
print(negro+rojo)

import numpy as np

rojo = np.array(rojo)
negro = np.array(negro)

print(type(rojo))

print(rojo + negro)