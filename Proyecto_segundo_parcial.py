import matplotlib.pyplot as plt
import numpy as np
import Grafo as g
import AStar as Astar
from time import time #importamos la función time para capturar tiempos
import random
from mpl_toolkits.mplot3d import Axes3D


DIMENSION=3   #Dimension de la matriz
OBSTACULOS=18 #Obstaculos (dimension^3)-1

#Todos tienen valor 1 indicando que hay un camino
matriz=np.ones((DIMENSION,DIMENSION,DIMENSION))

obstaculos=[]

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
for i in range(0,OBSTACULOS):
    xs = random.randint(0,DIMENSION-1)
    ys = random.randint(0, DIMENSION-1)
    zs=random.randint(0,DIMENSION-1)
    #Validamos que el obstaculo no esté agregado en la lista ni en la posicion inicial
    while [xs, ys, zs] in obstaculos or (xs == 0 and ys == 0 and zs == 0):
        xs = random.randint(0, DIMENSION-1)
        ys = random.randint(0, DIMENSION-1)
        zs = random.randint(0, DIMENSION-1)
    obstaculos.append([xs,ys,zs])

    ax.scatter(xs,ys,zs, s=7)

#plt.scatter(x,y,z)
plt.show()

"""Cambiamos el valor de la matrizOriginal de 1 a 0, indicando que dicho camino está obstaculizado"""
for indiceObstaculo in obstaculos:
    matriz[indiceObstaculo[0],indiceObstaculo[1],indiceObstaculo[2]]=0


x=[]
y=[]
z=[]
weights=[]

valores=[]
#Los valores de la matriz son transformados en lista y almacenados en "valores"
for i in range(DIMENSION):
    for j in range(DIMENSION):
        for k in range(DIMENSION):
            valores.append(matriz[i, j, k])

#Selecciona los nodos con valor de 1, y los agrupa.
for i in range(DIMENSION**3):
    if valores[i] == 1:
        saltoUno = 1+i
        saltoDos = DIMENSION+i
        saltoTres =(DIMENSION**2)+i
        if saltoUno < (DIMENSION**3) and valores[int(saltoUno)] == 1.0:
            x.append(i)
            y.append(saltoUno)
            z.append(saltoTres)
            weights.append(1)
        if saltoDos < (DIMENSION**3) and valores[int(saltoDos)] == 1.0:
            x.append(i)
            y.append(saltoDos)
            z.append(saltoTres)
            weights.append(1)
        if saltoTres < (DIMENSION**3) and valores[int(saltoTres)] == 1.0:
            x.append(i)
            y.append(saltoTres)
            z.append(saltoTres)
            weights.append(1)


"""graf=g.Graph(x,y,weights, directed=False)
graf.print_r()"""
print("Dijkstra\n")
tiempo_inicial = time()
G = g.Graph(x,y,weights)
G.create_network(x, y, weights)
G.dijkstra()
tiempo_final = time()
tiempo_ejecucion = tiempo_final - tiempo_inicial
print('El tiempo de ejecucion Dijkstra con dimension {0} y obstaculo {1} fue: {2} '.format(DIMENSION,OBSTACULOS,tiempo_ejecucion) )
G.print_distances()


print("FloydWarshall\n")
G1 = g.Graph(x,y,weights)
G1.create_network(x, y, weights)
G1.floyd_warshall()
tiempo_final = time()
tiempo_ejecucion = tiempo_final - tiempo_inicial
print('El tiempo de ejecucion Floyd Warshall dimension {0} y obstaculo {1} fue: {2} '.format(DIMENSION,OBSTACULOS,tiempo_ejecucion))
G1.print_distances()

""" 
fig1 = plt.figure()
ax1 = fig1.add_subplot(111,projection='3d')
ax1.plot_wireframe(np.array([x]) , np.array([y]), np.array([z]))
plt.show()
"""



#graf.draw()
#graf.print_r()

"""start = (0, 0)
end = (7, 6)"""

#path = Astar.astar(maze, start, end)
#print(path)

#a = fc.matriz_3d(x,y,z)

