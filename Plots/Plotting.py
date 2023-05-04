import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_xlim([-5, 5])
ax.set_ylim([-5, 5])
ax.set_zlim([-5, 5])

while True:
    # Generate an array of 10 3D points
    points = np.array([
        (-5, -5, -5),
        (-4, -4, -4),
        (-3, -3, -3),
        (-2, -2, -2),
        (-1, -1, -1),
        (0, 0, 0),
        (1, 1, 1),
        (2, 2, 2),
        (3, 3, 3),
        (4, 4, 4)
    ])

    # Clear the plot and plot the new points
    ax.clear()
    ax.scatter(points[:, 0], points[:, 1], points[:, 2])
    plt.draw()
    plt.pause(0.1)
q