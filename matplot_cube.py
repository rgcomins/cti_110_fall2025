import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np
#pip install matplot

# Create a new figure and a 3D subplot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# --- Define the Cube ---
# Vertices of the cube
cube_vertices = np.array([
    [0, 0, 0], [1, 0, 0], [1, 1, 0], [0, 1, 0],  # Bottom face
    [0, 0, 1], [1, 0, 1], [1, 1, 1], [0, 1, 1]   # Top face
])

# Faces of the cube (indices of vertices)
cube_faces = [
    [cube_vertices[0], cube_vertices[1], cube_vertices[2], cube_vertices[3]], # Bottom
    [cube_vertices[4], cube_vertices[5], cube_vertices[6], cube_vertices[7]], # Top
    [cube_vertices[0], cube_vertices[1], cube_vertices[5], cube_vertices[4]], # Front
    [cube_vertices[2], cube_vertices[3], cube_vertices[7], cube_vertices[6]], # Back
    [cube_vertices[1], cube_vertices[2], cube_vertices[6], cube_vertices[5]], # Right
    [cube_vertices[0], cube_vertices[3], cube_vertices[7], cube_vertices[4]]  # Left
]

# Add the cube to the plot
ax.add_collection3d(Poly3DCollection(cube_faces, facecolors='cyan', linewidths=1, edgecolors='r', alpha=.25))

# --- Define the Pyramid ---
# Vertices of the pyramid (placed on top of the cube)
pyramid_base_center_x = 0.5
pyramid_base_center_y = 0.5
pyramid_base_z = 1 # Top of the cube
pyramid_height = 1.0
pyramid_base_side = 1.0 # Size of the pyramid base

pyramid_vertices = np.array([
    [pyramid_base_center_x - pyramid_base_side/2, pyramid_base_center_y - pyramid_base_side/2, pyramid_base_z], # Base corner 1
    [pyramid_base_center_x + pyramid_base_side/2, pyramid_base_center_y - pyramid_base_side/2, pyramid_base_z], # Base corner 2
    [pyramid_base_center_x + pyramid_base_side/2, pyramid_base_center_y + pyramid_base_side/2, pyramid_base_z], # Base corner 3
    [pyramid_base_center_x - pyramid_base_side/2, pyramid_base_center_y + pyramid_base_side/2, pyramid_base_z], # Base corner 4
    [pyramid_base_center_x, pyramid_base_center_y, pyramid_base_z + pyramid_height] # Apex
])

# Faces of the pyramid (indices of vertices)
pyramid_faces = [
    [pyramid_vertices[0], pyramid_vertices[1], pyramid_vertices[2], pyramid_vertices[3]], # Base
    [pyramid_vertices[0], pyramid_vertices[1], pyramid_vertices[4]], # Side 1
    [pyramid_vertices[1], pyramid_vertices[2], pyramid_vertices[4]], # Side 2
    [pyramid_vertices[2], pyramid_vertices[3], pyramid_vertices[4]], # Side 3
    [pyramid_vertices[3], pyramid_vertices[0], pyramid_vertices[4]]  # Side 4
]

# Add the pyramid to the plot
ax.add_collection3d(Poly3DCollection(pyramid_faces, facecolors='yellow', linewidths=1, edgecolors='blue', alpha=.5))

# Set plot limits
ax.set_xlim([0, 1])
ax.set_ylim([0, 1])
ax.set_zlim([0, 2])

# Set labels
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Display the plot
plt.show()