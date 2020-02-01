import funciones as fc
import numpy as np

#xyz = int(input("Ingrese dimensión del arreglo: "))

#a = fc.matriz_3d(xyz,xyz,xyz)

#print(a[0][0])

#b=[ [ [1,2,3], [1,2,4],[1,2,3]], [[2,2,3],[3,2,3],[4,2,3]], [[5,2,3],[6,2,3],[7,2,3]]]
#print(b.__len__())
#print(b[0][1][0])
#print(b)

#c=np.array([[ [1,2,3], [1,2,4],[1,2,3]], [[2,2,3],[3,2,3],[4,2,3]], [[5,2,3],[6,2,3],[7,2,3]]],int)
#print(c[0][0])
#r=int(input("Ingrese número de obstáculos: "))
#validar que sea menor a los elmentos de la matriz

"""
a=[]
a.append([1,2,5])
if([1,2,3] in a):
    print("si esta 123")
elif([[1,2,3]] in a):
    print("dentro123")
else:
    print("nop")
print(a[0][2])"""

b=[ [[1,2,3], [1,2,4],[1,2,3]], [[2,2,3],[3,2,3],[4,2,3]], [[5,2,3],[6,2,3],[7,2,3]]]
h=[[0,1,2],[1,1,2],[1,1,2]]

d=np.array(b)
print(d[0,2])
#d[0,2]= np.array([0,0,0])
#d[2,2]= [0,0,0]
print(d.sum())
for ind in h:
    d[ind[0],ind[1],ind[2]]=0

indic= np.where(d=1)
print(indic)


#f[0,0,0]=[0,0,0]
#print(f)
""" 
import Grafo as g
import random
from mpl_toolkits.mplot3d import Axes3D

xyz = int(input("Ingrese dimensión del arreglo: "))

obstaculos=int(input("Ingrese número de obstáculos: "))
while(obstaculos>=(xyz*xyz*xyz) or obstaculos<0):
    obstaculos = int(input("Ingrese cantidad de obstáculos menores a la dimensión ingresada: "))

x=[]
y=[]
z=[]
weights=[]

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
for i in range(0,obstaculos):
    xs = random.randint(0,xyz)
    ys = random.randint(0, xyz)
    zs=random.randint(0,xyz)
    while(xs==0 and ys==0 and zs==0):
        xs = random.randint(0, xyz)
        ys = random.randint(0, xyz)
        zs = random.randint(0, xyz)

    y.append(ys)
    x.append(xs)
    z.append(zs)
    weights.append(random.randint(0,1))
    ax.scatter(xs,ys,zs, s=7)
#plt.scatter(x,y,z)

print("{0}\n{1}\n{2}".format(x,y,z))
plt.show()


graf=g.Graph(x,y,weights, directed=False)
graf.print_r()

#a = fc.matriz_3d(x,y,z)

"""