import numpy as np
import clifford as cf
from clifford.tools.g3 import generate_rotation_rotor

# Setting the CL3,0,0 configuration.
layout, blades = cf.Cl(3)
locals().update(blades) # making the symbolic blades 'e1', 'e12', local instance(I think) 
import warnings
warnings.filterwarnings("ignore")

## 
## Rotor = cos(Q)-sin(Q)*bivector
##
# def generate_rotation_rotor(theta, euc_vector_m, euc_vector_n):
#     euc_vector_n = euc_vector_n / abs(euc_vector_n)
#     euc_vector_m = euc_vector_m / abs(euc_vector_m)
#     bivector_B = (euc_vector_m ^ euc_vector_n)
#     bivector_B = bivector_B / (math.sqrt((-bivector_B * bivector_B)[()]))
#     rotor = math.cos(theta / 2) - bivector_B * math.sin(theta / 2)
#     return rotor

## Creating local Rotation rotors for each axes. 
# Rz = lambda theta: generate_rotation_rotor(np.radians(theta),e1,e2)
# Ry = lambda theta: generate_rotation_rotor(np.radians(theta),e1,e3)
# Rx = lambda theta: generate_rotation_rotor(np.radians(theta),e2,e3)


def main():
	l0 = 2 # units length
	l1 = 2 # units length
	l2 = 2 # units length
	theta0 = np.radians(45)
	theta1 = np.radians(30)
	theta2 = np.radians(-45)

	print("\n\nTesting R configuration with angle {0} and rotation about plane {1}...".format(30,e1^e2))
	R0 = generate_rotation_rotor(theta0,e1,e2)
	EE0 = R0*(l0*e1)*R0.inv()
	print("The end effector is at: ",EE0)

	print("\nTesting R || R configuration...")
	R1 = generate_rotation_rotor(theta1,e1,e2)
	R01 = R0*R1
	EE1 = EE0 + R01*(l1*e1)*R01.inv()
	print("The end effector for R||R Config is at: ",EE1)

	print("\nTesting R || R || R configuration...")
	R2 = generate_rotation_rotor(theta2,e1,e2)
	R02 = R01*R2
	EE2 = EE1 + R02*(l2*e1)*R02.inv()
	print("The end effector for R||R Config is at: ",EE2)

	## Might be working :/
	print("\nTesting R _|_ R configuration...")
	R0 = generate_rotation_rotor(theta0,e1,e3)
	EE0 = R0*(l0*e2)*R0.inv()
	R1 = generate_rotation_rotor(theta1,e1,e2)
	R01 = R0*R1
	EE1 = EE0 + R01*(l1*e1)*R01.inv()
	print("The end effector for R_|_R Config is at: ",EE1)

	## NOT TESTED YET :/
	print("\nTesting R _|_ R || R configuration...")
	R0 = generate_rotation_rotor(theta0,e1,e3)
	EE0 = R0*(l0*e2)*R0.inv()
	R1 = generate_rotation_rotor(theta1,e1,e2)
	R01 = R0*R1
	EE1 = EE0 + R01*(l1*e1)*R01.inv()
	R2 = generate_rotation_rotor(theta2,e1,e2)
	R02 = R01*R2
	EE2 = EE1 + R02*(l1*e1)*R02.inv()
	print("The end effector for R_|_R || R Config is at: ",EE2)

	## NOT TESTED YET :/
	print("\nTesting R _|_ R || R configuration similar to clifford docs...")
	R0 = generate_rotation_rotor(theta0,e1,e3)
	R1 = generate_rotation_rotor(theta1,e1,e2)
	R01 = R0*R1
	EE1 = R01*(l1*e1)*R01.inv()

	R2 = generate_rotation_rotor(theta2,e1,e2)
	R02 = R01*R2
	EE2 = EE1 + R02*(l1*e1)*R02.inv()
	print("The end effector for R_|_R || R Config is at: ",EE2)
	## The end effector for R_|_R || R Config is at:  (2.59077^e1) + (0.48236^e2) + (2.59077^e3)




if __name__ == '__main__':
	main()