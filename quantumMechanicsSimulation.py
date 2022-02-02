import numpy as np
import matplotlib.pyplot as plt
import random
from matplotlib.widgets import Slider, Button

L = float(input())
N = 2

plt.style.use('dark_background')

fig = plt.figure()
ax = fig.subplots()

def wave (x, l = L, N = 2):
    return (np.sqrt(2/l)) * np.sin(((N * np.pi) / l) * x)

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
    
def gen(N):

    area = []

    curr = 0

    while curr <= L:
        area.append(int((probDist(wave(curr, N)) * 0.01) * 10000))
        curr = curr + 0.01

    probailities = []

    for i in range(len(area)):
        for j in range(area[i]+1):
            probailities.append(0.01 * j)

    point = random.choice(probailities)
    ax.plot(point, 0, 'go')

plot, = ax.plot(x, y, color="red")
plot2, = ax.plot(x, proby, color="blue")
ax.plot(x1, y1)
gen(N)

plt.subplots_adjust(bottom=0.25)

ax3 = (plt.axes([0.25, 0.12, 0.65, 0.03]))
ax4 = (plt.axes([0.8, 0.05, 0.1, 0.05]))

allowed_amplitudes = np.concatenate([np.linspace(1, 1, 100), range(1, 101)])

sN = Slider(ax3, "Energy Level", 1, 100, valinit=N, valstep=allowed_amplitudes)

button = Button(ax4, 'Plot', color='darkgoldenrod', hovercolor='indigo')

def func(event):
    gen(sN.val)

button.on_clicked(func)

def update(val):
    y = wave(x, L, sN.val)
    proby = probDist(y)
    plot.set_ydata(y)
    plot2.set_ydata(proby)

sN.on_changed(update)

plt.show()
