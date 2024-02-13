import clifford as cf
import numpy as np
import matplotlib.pyplot as plt

# Define the algebra
layout, blades = cf.Cl(3)

# Define the vectors and rotation axis
v = blades['e1']
u = (1/np.sqrt(2)) * (blades['e1'] + blades['e2'])

# Define the rotation angle
theta = np.pi / 4

# Compute the rotor
rotor = np.cos(theta/2) + np.sin(theta/2) * blades['e12']

# Rotate the vector
v_rotated = rotor * v * ~rotor

# Visualization
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Extract components for quiver
orig_x, orig_y, orig_z = 0, 0, 0
v_x, v_y, v_z = v.value[1], v.value[2], v.value[3]
v_rotated_x, v_rotated_y, v_rotated_z = v_rotated.value[1], v_rotated.value[2], v_rotated.value[3]

# Plot the original and rotated vectors
ax.quiver(orig_x, orig_y, orig_z, v_x, v_y, v_z, color='b', label='Original Vector')
ax.quiver(orig_x, orig_y, orig_z, v_rotated_x, v_rotated_y, v_rotated_z, color='r', label='Rotated Vector')

ax.set_xlim([0, 1])
ax.set_ylim([0, 1])
ax.set_zlim([0, 1])
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.legend()

plt.show()

