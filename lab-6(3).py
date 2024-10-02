import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

R = np.array([
    [0.866, -0.5, 0],
    [0.5, 0.866, 0],
    [0, 0, 1]
])

origin = np.array([0, 0, 0])
x_axis = R[:, 0]  # X-axis 
y_axis = R[:, 1]  # Y-axis 
z_axis = R[:, 2]  # Z-axis 

# Plotting
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.quiver(0, 0, 0, 1, 0, 0, color='r', label='Original X')
ax.quiver(0, 0, 0, 0, 1, 0, color='g', label='Original Y')
ax.quiver(0, 0, 0, 0, 0, 1, color='b', label='Original Z')
ax.quiver(0, 0, 0, x_axis[0], x_axis[1], x_axis[2], color='r', linestyle='--', label='Rotated X')
ax.quiver(0, 0, 0, y_axis[0], y_axis[1], y_axis[2], color='g', linestyle='--', label='Rotated Y')
ax.quiver(0, 0, 0, z_axis[0], z_axis[1], z_axis[2], color='b', linestyle='--', label='Rotated Z')
ax.set_xlim([-1, 1])
ax.set_ylim([-1, 1])
ax.set_zlim([-1, 1])

# Labels
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.legend()
plt.show()
