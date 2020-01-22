import matplotlib.pyplot as plt
import funciones as fc
import numpy as np
import random
from mpl_toolkits.mplot3d import Axes3D

x=[]
y=[]
z=[]
valor=[]

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
for i in range(0,100):
    xs = random.randint(0,100)
    x.append(xs)
    ys = random.randint(0, 100)
    y.append((ys))
    zs=random.randint(0,100)
    z.append(zs)
    valor.append(0)
    ax.scatter(xs,ys,zs, s=7)
#plt.scatter(x,y,z)
plt.show()

#a = fc.matriz_3d(x,y,z)

