import matplotlib.pyplot as plt
import funciones as fc
import numpy as np
import Grafo as g

import random
from mpl_toolkits.mplot3d import Axes3D

x=[]
y=[]
z=[]
weights=[]

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
for i in range(0,100):
    xs = random.randint(0,100)
    x.append(xs)
    ys = random.randint(0, 100)
    y.append((ys))
    zs=random.randint(0,100)
    z.append(zs)
    weights.append(random.randint(0,1))
    ax.scatter(xs,ys,zs, s=7)
#plt.scatter(x,y,z)
plt.show()


graf=g.Graph(x,y,weights, directed=False)
graf.print_r()

#a = fc.matriz_3d(x,y,z)

