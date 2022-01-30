import numpy as np
import matplotlib.pyplot as plt
import random

L = float(input())
N = int(input())

def wave (x):
    return (np.sqrt(2/L)) * np.sin(((N * np.pi) / L) * x)

def probDist (wave):
    return wave ** 2

plt.style.use('dark_background')

x = np.arange(0, L, 0.001)
y = wave(x)
   
x1 = []
y1 = []

proby = probDist(y)

for i in range (int(L)+1):
    x1.append(i)
    y1.append(0)

area = []

curr = 0

while curr <= L:
    area.append(int((probDist(wave(curr)) * 0.01) * 10000))
    curr = curr + 0.01

probailities = []

for i in range(len(area)):
    for j in range(area[i]+1):
        probailities.append(0.01 * j)

point = random.choice(probailities)

plt.plot(x, y, color="red")
plt.plot(x, proby, color="blue")
plt.plot(x1, y1)
plt.plot(point, 0, color="green")
plt.show()
