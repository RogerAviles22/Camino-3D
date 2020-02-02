import numpy as np

def matriz_3d(x,y,z):
    return np.ones((x,y,z))

from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np

# Creamos la figura
fig = plt.figure()

# Agrrgamos un plano 3D
ax1 = fig.add_subplot(111,projection='3d')


# plot_wireframe nos permite agregar los datos x, y, z. Por ello 3D
# Es necesario que los datos esten contenidos en un array bi-dimensional
ax1.plot_wireframe(np.array([1,2,3,4,5,6,7,8,9,10]),np.array([5,6,7,8,2,5,6,3,7,2]), np.array([1,2,6,3,2,7,3,3,7,2]))

# Mostramos el gráfico
plt.show()