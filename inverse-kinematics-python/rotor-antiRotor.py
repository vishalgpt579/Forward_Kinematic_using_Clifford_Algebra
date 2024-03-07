## To ignore all the NumbaDeprecationWarnings. GOD! too many of them.
from numba.core.errors import NumbaDeprecationWarning, NumbaPendingDeprecationWarning
import warnings
warnings.simplefilter('ignore', category=NumbaDeprecationWarning)
warnings.simplefilter('ignore', category=NumbaPendingDeprecationWarning)

import numpy as np
from clifford import Cl, conformalize
from clifford.tools.g3 import generate_rotation_rotor
from clifford.tools.g3c import apply_rotor
from pyganja import *


## Defining the Cl(3,1) signatures.
G3, blades_g2 = Cl(3)
G3c, blades_g3c, stuff = conformalize(G3)
# PUtting the symbolic variables in local namespace.
locals().update(blades_g3c)
locals().update(stuff)

'''
This script demonstrate the action of rotor and anti-rotor 
'''

R = generate_rotation_rotor(45,e1,e2) # Rotation along z-axis
R_anti = ~R # Anti-rotor

vec = 1*e1+1*e2+1*e3 #(1i,1j)
print("origin vector: ", vec)

vec_R = apply_rotor(vec,R)
print("\nVector with Rotor applied : ", vec_R)

vec_anti_R = apply_rotor(vec_R, R_anti)
print("\nVector with anti Rotor applied: ", vec_anti_R)

print("\nIs vector(without rotor) and vector(with anti-Rotor same?\n",vec == vec_anti_R)


sc = GanjaScene()
sc.add_objects([up(vec)], color=Color.BLACK)
sc.add_objects([up(vec_R)], color=Color.BLUE)
sc.add_objects([up(vec_anti_R)], color=Color.RED)
draw(sc, 
	static=False ,
	scale=0.1,
	grid= True,
	labels=True)