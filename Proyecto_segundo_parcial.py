import matplotlib.pyplot as plt
import funciones as fc
import numpy as np
import Grafo as g
import AStar as Astar
from time import time #importamos la función time para capturar tiempos

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


nodos=[]
for i in range(1000):
    nodos.append(i)

x=[]
y=[]
weights=[]

valores=[]
#Los valores de la matriz son transformados en lista y almacenados en "valores"
for i in range(100):
    for j in range(100):
        for k in range(100):
            valores.append(matriz[i, j, k])

#Selecciona los nodos con valor de 1, y los agrupa.
for i in range(1000000):
    if valores[i] == 1:
        saltoUno=1+i
        saltoDos=100+i
        saltoTres=10000+i
        if saltoUno < 1000000 and valores[int(saltoUno)] == 1.0:
            x.append(i)
            y.append(saltoUno)
            weights.append(1)
        if saltoDos < 1000000 and valores[int(saltoDos)] == 1.0:
            x.append(i)
            y.append(saltoDos)
            weights.append(1)
        if saltoTres < 1000000 and valores[int(saltoTres)] == 1.0:
            x.append(i)
            y.append(saltoTres)
            weights.append(1)


graf=g.Graph(x,y,weights, directed=False)

tiempo_inicial = time()
tiempo_final = time()
tiempo_ejecucion = tiempo_final - tiempo_inicial
print('El tiempo de ejecucion fue:', tiempo_ejecucion)

#graf.draw()
#graf.print_r()

start = (0, 0)
end = (7, 6)

#path = Astar.astar(maze, start, end)
#print(path)

#a = fc.matriz_3d(x,y,z)