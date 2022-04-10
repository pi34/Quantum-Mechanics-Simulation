from debugpy import connect
import numpy as np
import random
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button

import sqlite3

plt.style.use('dark_background')

figur = plt.figure()
axs = plt.axes(projection="3d")

axs.set_xlim(-8e-10, 8e-10)
axs.set_ylim(-8e-10, 8e-10)
axs.set_zlim(-8e-10, 8e-10)


def coord (arr, b, r):
    a = arr[0]
    x = r*np.sin(b) * np.cos(a)
    y = r*np.sin(b) * np.sin(a)
    z = r*np.cos(b)
    return x, y, z

def spher (x, y, z):
    r = np.sqrt(x**2 + y**2 + z**2)
    b = np.arccos(z/r)
    if x > 0:
        a = np.arctan(y/x)
    elif x < 0 and y >= 0:
        a = np.arctan(y/x) + np.pi
    elif x < 0 and y < 0:
        a = np.arctan(y/x) - np.pi
    elif x == 0 and y > 0:
        a = np.pi/2
    elif x == 0 and y < 0:
        a = -np.pi / 2
    return a, b, r

#print(coord(spher(1, 1, 1)))

a0= 5.29177210903*(10**(-11))

def wave(x, y, z, n):
    r= np.sqrt(x**2+y**2+z**2)
    sphericalC = spher(x, y, z)
    if n==1:
    # 1s
        A= (1/a0)**1.5
        B= (1/np.sqrt(np.pi))*A
        C= (1/a0)*r
        W=B*(np.e**((-1)*C))
    elif n==2:
    # 2s
        A = (1/a0)**1.5
        B = (1/np.sqrt(32*np.pi))*A
        C = (1/a0)*r
        W = B*(2-C)*np.e**(-C/2)
    elif n==3:
    # 2pz
        A = (1/a0)**1.5
        B = (1/np.sqrt(32*np.pi))*A
        C = (1/a0) * sphericalC[2]
        W = B * C * np.e**(-1/2 * C) * np.cos(sphericalC[1])
    elif n==4:
    # 2px
        A = (1/a0)**1.5
        B = (1/np.sqrt(64*np.pi))*A
        C = (1/a0) * sphericalC[2]
        W = B * C * np.e**(-1/2 * C) * np.sin(sphericalC[1]) * np.e ** (1j * sphericalC[0])
    elif n==5:
    # 2py
        A = (1/a0)**1.5
        B = (1/np.sqrt(64*np.pi))*A
        C = (1/a0) * sphericalC[2]
        W = B * C * np.e**(-1/2 * C) * np.sin(sphericalC[1]) * np.e ** (-1j * sphericalC[0])
    elif n==6:
    # 3s
        A = (1/a0)**1.5
        B = (1/81*np.sqrt(3*np.pi))*A
        C = (1/a0) * sphericalC[2]
        W = B * (27 - 18*C + 2*C**2) * np.e ** (-C/3)
    elif n==7:
    # 3pz
        A = (1/a0)**1.5
        B = (1/81)*(np.sqrt(2/np.pi)) * A
        C = (1/a0) * sphericalC[2]
        W = B * (6*sphericalC[2] - C**2) * np.e ** (-C/3) * np.cos(sphericalC[1])
    elif n==8:
    # 3px
        A = (1/a0)**1.5
        B = (1/(81*np.sqrt(np.pi))) * A
        C = (1/a0) * sphericalC[2]
        W = B * (6*C - C**2) * np.e ** (-sphericalC[2]/3) * np.sin(sphericalC[1]) * np.e ** (1j * sphericalC[0])
    elif n==9:
    # 3py
        A = (1/a0)**1.5
        B = (1/(81*np.sqrt(np.pi))) * A
        C = (1/a0) * sphericalC[2]
        W = B * (6*C - C**2) * np.e ** (-sphericalC[2]/3) * np.sin(sphericalC[1]) * np.e ** (-1j * sphericalC[0])
    elif n==10:
    # 3dx1
        A = (1/a0)**1.5
        B = (1/(81*np.sqrt(np.pi))) * A
        C = (1/a0) * sphericalC[2]
        W = B * (C**2) * (np.e ** (-C/3)) * np.sin(sphericalC[1]) * np.cos(sphericalC[1]) * np.e ** (1j * sphericalC[0])
    elif n==11:
    # 3dx2
        A = (1/a0)**1.5
        B = (1/(81*np.sqrt(np.pi))) * A
        C = (1/a0) * sphericalC[2]
        W = B * (C**2) * (np.e ** (-C/3)) * np.sin(sphericalC[1]) * np.cos(sphericalC[1]) * np.e ** (-1j * sphericalC[0])
    elif n==12:
    # 3dz
        A = (1/a0)**1.5
        B = (1/(81*np.sqrt(6*np.pi))) * A
        C = (1/a0) * sphericalC[2]
        W = B * (C**2) * (np.e ** (-C/3)) * ((3 * np.cos(sphericalC[1])**2) -1)
    elif n==13:
    # 3dy1
        A = (1/a0)**1.5
        B = (1/(162*np.sqrt(np.pi))) * A
        C = (1/a0) * sphericalC[2]
        W = B * (C**2) * (np.e ** (-C/3)) * np.sin(sphericalC[1])**2 * np.e ** (2j * sphericalC[0])
    elif n==14:
    # 3dy2
        A = (1/a0)**1.5
        B = (1/(162*np.sqrt(np.pi))) * A
        C = (1/a0) * sphericalC[2]
        W = B * (C**2) * (np.e ** (-C/3)) * np.sin(sphericalC[1])**2 * np.e ** (-2j * sphericalC[0])
    
    return W

def probdist(x, y, z, n):
    return wave(x, y, z, n)**2

arry = []

i = -(8)**-10
j = -(8)**-10
k = -(8)**-10



while i < 8**-10:
    j = -(8)**-10
    while j < 8**-10:
        k = -(8)**-10
        while k < 8**-10:
            if (i != 0 and j != 0 and k != 0):
                r = np.sqrt(i**2 + j**2 + k**2)
                if (k != r):
                    arry.append([i, j, k, probdist(i, j, k, 6)*(10**-27)])
                    
            k = k + 10**-11
        j = j + 10**-11
    i = i + 10**-11


arr = []

connct = sqlite3.connect('data.sqlite')
cur = connct.cursor()

for i in range (len(arry)):
    for j in range(int(arry[i][3])):
        arr.append([arry[i][0], arry[i][1], arry[i][2]])
        cur.execute(f'INSERT INTO ThreesShell (x, y, z) values ({arry[i][0]}, {arry[i][1]}, {arry[i][2]})')
        connct.commit()

#cur.execute('SELECT * FROM TwopxShell')
#arr = cur.fetchall()

connct.close()

axs.plot(0, 0, 0, 'bo')

for i in range (1000):
    point = random.choice(arr)
    axs.plot(point[0], point[1], point[2], 'ro')

"""n = 1

def gen(N):

    axs.clear()
    axs.plot(0, 0, 0, 'bo')

    if N==1:
        cur.execute('SELECT * FROM sShell')
    elif N==2:
        cur.execute('SELECT * FROM TwosShell')
    elif N==3:
        cur.execute('SELECT * FROM TwopzShell')
    elif N==4:
        cur.execute('SELECT * FROM TwopxShell')
    elif N==5:
        cur.execute('SELECT * FROM TwopyShell')
    elif N==6:
        cur.execute('SELECT * FROM ThreesShell')
    elif N==7:
        cur.execute('SELECT * FROM ThreepzShell')
    elif N==8:
        cur.execute('SELECT * FROM ThreepxShell')
    elif N==9:
        cur.execute('SELECT * FROM ThreepyShell')
    elif N==10:
        cur.execute('SELECT * FROM Threedx1Shell')
    elif N==11:
        cur.execute('SELECT * FROM Threedx2Shell')
    elif N==12:
        cur.execute('SELECT * FROM ThreedzShell')
    elif N==13:
        cur.execute('SELECT * FROM Threedy1Shell')
    elif N==14:
        cur.execute('SELECT * FROM Threedy2Shell')
    arr = cur.fetchall()
    connct.close()

    axs.plot(0, 0, 0, 'bo')

    for i in range (1000):
        point = random.choice(arr)
        axs.plot(point[0], point[1], point[2], 'ro')

    plt.show()

    

ax3 = (plt.axes([0.25, 0.12, 0.65, 0.03]))
sN = Slider(ax3, "N", 1, 14, valinit=n)

def update(val):
    gen(val)

sN.on_changed(update)"""

plt.show()

