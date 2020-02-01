import matplotlib.pyplot as plt
import funciones as fc
import numpy as np
import Grafo as g

import random
from mpl_toolkits.mplot3d import Axes3D

#Todos tienen valor 1 indicando que hay un camino
matriz=np.ones((100,100,100))

CONSTANTE=99

obstaculos=[]

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
for i in range(0,100):
    xs = random.randint(0,CONSTANTE)
    ys = random.randint(0, CONSTANTE)
    zs=random.randint(0,CONSTANTE)
    #Validamos que el obstaculo no esté agregado en la lista
    while [xs, ys, zs] in obstaculos or (xs == 0 and ys == 0 and zs == 0):
        xs = random.randint(0, CONSTANTE)
        ys = random.randint(0, CONSTANTE)
        zs = random.randint(0, CONSTANTE)
    obstaculos.append([xs,ys,zs])

    ax.scatter(xs,ys,zs, s=7)

#plt.scatter(x,y,z)
plt.show()

"""Cambiamos el valor de la matrizOriginal de 1 a 0, indicando que dicho camino está obstaculizado"""
for indiceObstaculo in obstaculos:
    matriz[indiceObstaculo[0],indiceObstaculo[1],indiceObstaculo[2]]=0
print(matriz)

x=[]
y=[]
z=[]
weights=[]



print(x)
print(y)
print(z)
print(obstaculos)
graf=g.Graph(x,y,weights, directed=False)
#graf.print_r()



#a = fc.matriz_3d(x,y,z)