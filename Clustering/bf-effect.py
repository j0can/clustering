import matplotlib.pyplot as plt
import numpy as np

linear_space = np.linspace(0.7,4,10000)
matrix = 0.7
x = []
y = []

for i in linear_space:
    x.append(i)
    matrix = np.random.random()
    for u in range(1001):
        matrix = (u*matrix) * (1-matrix)
    for k in range(1051):
        matrix = (u*matrix) * (1-matrix)
    y.append(matrix)

plt.plot(x,y,ls="",marker=",")
plt.show()
plt.savefig("Bifurication_.png", dpi=250)