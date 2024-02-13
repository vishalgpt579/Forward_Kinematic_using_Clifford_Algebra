## To ignore all the NumbaDeprecationWarnings. GOD! too many of them.
from numba.core.errors import NumbaDeprecationWarning, NumbaPendingDeprecationWarning
import warnings
warnings.simplefilter('ignore', category=NumbaDeprecationWarning)
warnings.simplefilter('ignore', category=NumbaPendingDeprecationWarning)

import numpy as np
from clifford import Cl, conformalize
from clifford.tools.g3 import generate_rotation_rotor
from clifford.tools.g3c import generate_translation_rotor, apply_rotor

# Defining the Cl(3,1) signatures.
G3, blades_g2 = Cl(3)
G3c, blades_g3c, stuff = conformalize(G3)
# PUtting the symbolic variables in local namespace.
locals().update(blades_g3c)
locals().update(stuff)


def main():
	l0 = 2 # units length
	l1 = 2 # units length
	l2 = 2 # units length
	theta0 = np.radians(45)
	theta1 = np.radians(30)
	theta2 = np.radians(-45)

	print("\nTesting R _|_ R || R configuration similar to Clifford API docs...")
	R0 = generate_rotation_rotor(theta0,e1,e3)
	R1 = generate_rotation_rotor(theta1,e1,e2)
	Rl1 = 1 - 0.5*l1*(e1^einf)
	R2 = generate_rotation_rotor(theta2,e1,e2)
	Rl2 = 1 - 0.5*l2*(e1^einf)
	R = R0*R1*Rl1*R2*Rl2
	EE = down(R*up(eo)*~R)
	print("The end-effector for R_|_R || R Config is at: ",EE)


if __name__ == '__main__':
	main()