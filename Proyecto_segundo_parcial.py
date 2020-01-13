import matplotlib.pyplot as plt
import numpy as np
import random
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
for i in range(0,100):
    ax.scatter(xs=random.randint(0,100),ys=random.randint(0,100),zs=random.randint(0,100), s=7)
#plt.scatter(x,y,z)
plt.show()