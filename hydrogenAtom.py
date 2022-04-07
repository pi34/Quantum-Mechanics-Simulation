import numpy as np
import random
import matplotlib.pyplot as plt

figur = plt.figure()
axs = plt.axes(projection="3d")

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
    sphericalC = spher(x, y, z)
    if n==1:
        A= (1/a0)**1.5
        B= (1/np.sqrt(np.pi))*A
        C= (1/a0)
        r= np.sqrt(x**2+y**2+z**2)
        W=B*(np.e**((-1)*C*r))
    elif n==2:
        A = (1/a0)**1.5
        B = (1/np.sqrt(32*np.pi))*A
        C = (1/a0) * sphericalC[2]
        W = B * C * np.e**(-1/2 * C) * np.cos(sphericalC[1])
    return W

def probdist(x, y, z, n):
    return wave(x, y, z, n)**2

arry = []

i = -(10)**-10
j = -(10)**-10
k = -(10)**-10



while i < 10**-10:
    j = -(10)**-10
    while j < 10**-10:
        k = -(10)**-10
        while k < 10**-10:
            if (i != 0 and j != 0 and k != 0):
                r = np.sqrt(i**2 + j**2 + k**2)
                if (k != r):
                    arry.append([i, j, k, probdist(i, j, k, 1)*(10**-29)])
                    #print([i, j, k, probdist(i, j, k, 2)*(10**-29)])
            k = k + 10**-12
        j = j + 10**-12
    i = i + 10**-12

print (len(arry))

sum = 0

#for i in range (len(arry)):
 #   sum = sum + int(arry[i][3])
    #print(arry[i][3])

#print(sum)

arr = []

for i in range (len(arry)):
    for j in range(int(arry[i][3])):
        arr.append([arry[i][0], arry[i][1], arry[i][2]])
        #print([arry[i][0], arry[i][1], arry[i][2]])

axs.plot(0, 0, 0, 'bo')

for i in range (100):
    point = random.choice(arr)
    print(point)
    axs.plot(point[0], point[1], point[2], 'go')

plt.show()

"""x = rsintheta cosphi
y = rsintheta sinphi
z = rcos theta"""
