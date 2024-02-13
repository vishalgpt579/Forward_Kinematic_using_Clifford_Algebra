import clifford as cf
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the algebra
layout, blades = cf.Cl(3)

# Define the base and end-effector positions
base_position = np.array([0, 0, 0])
ee_position = np.array([1, 0, 0])

# Define joint angles (in radians)
theta1 = np.pi / 4
theta2 = np.pi / 3

# Compute rotors for joint rotations
rotor1 = np.cos(theta1/2) + np.sin(theta1/2) * blades['e23']
rotor2 = np.cos(theta2/2) + np.sin(theta2/2) * blades['e13']

# Rotate the end-effector position
ee_position_rotated = rotor1 * rotor2 * ee_position * ~rotor2 * ~rotor1

# Visualization
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the manipulator links
link_points = np.array([[base_position[0], ee_position_rotated[0]],
                        [base_position[1], ee_position_rotated[1]],
                        [base_position[2], ee_position_rotated[2]]])
ax.plot(link_points[0, :], link_points[1, :], link_points[2, :], 'bo-')

# Plot the base and end-effector positions
ax.scatter(*base_position, color='b', marker='o', label='Base')
ax.scatter(*ee_position_rotated, color='r', marker='o', label='End Effector')

ax.set_xlim([-1, 2])
ax.set_ylim([-1, 1])
ax.set_zlim([0, 1])
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.legend()

plt.show()
