import funciones as fc

x = int(input("Ingrese x: "))
y = int(input("Ingrese y: "))
z = int(input("Ingrese z: "))

a = fc.matriz_3d(x,y,z)

print(a)

r=int(input("Ingrese número de obstáculos: "))
#validar que sea menor a los elmentos de la matriz