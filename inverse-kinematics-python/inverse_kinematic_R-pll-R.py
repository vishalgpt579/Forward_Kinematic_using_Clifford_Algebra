## To ignore all the NumbaDeprecationWarnings. GOD! too many of them.
from numba.core.errors import NumbaDeprecationWarning, NumbaPendingDeprecationWarning
import warnings
warnings.simplefilter('ignore', category=NumbaDeprecationWarning)
warnings.simplefilter('ignore', category=NumbaPendingDeprecationWarning)

import numpy as np
from clifford import Cl, conformalize
from clifford.tools.g3 import generate_rotation_rotor
from clifford.tools.g3c import generate_translation_rotor, apply_rotor


## Defining the Cl(3,1) signatures.
G3, blades_g2 = Cl(3)
G3c, blades_g3c, stuff = conformalize(G3)
# PUtting the symbolic variables in local namespace.
locals().update(blades_g3c)
locals().update(stuff)


## R || R configuration robot

l1 = 2
l2 = 2
theta0 = np.radians(0)
theta1 = np.radians(0)
# Forward kinematics
R0 = generate_rotation_rotor(theta0,e1,e2)
# T0 = generate_translation_rotor(l1*e1) ## NOT WORKING!!!
T0 = 1 - 0.5*l1*(e1^einf)
R1 = generate_rotation_rotor(theta1,e1,e2)
# T1 = generate_translation_rotor(l2*e1) ## NOT WORKING !!!
T1 =1 - 0.5*l2*(e1^einf)
R_elb = R0*T1
R = R_elb*R1*T1
elb = down(apply_rotor(up(0), R_elb))
EE = down(apply_rotor(up(0),R))

print("\nR||R configuration...")
print("\nElbow: ",elb)
print("EE: ", EE)

# Inverse Kinematics
print("\nPerforming Inverse Kinematics")
S_ee = (up(EE)-0.5*np.square(l2)*einf).dual()
S_base = (up(0)-0.5*np.square(l1)*einf).dual()
C = S_base & S_ee
# Generating a plane that passes through the EE and 
plane = up(0)^up(1*e2)^up(EE)^einf
PP = -(plane & C)

#computing the elb pose using the constrains...
elb_test = (1 + PP*(1/np.sqrt(float(PP*PP))))*(PP|einf)
print("For {} EE values, computed Elbow pose are: {}".format(EE,down(elb_test)))

L1 = (elb_test^up(EE)^einf).dual().normal()
# print("L1: ",L1)
L2 = (up(0)^elb_test^einf).dual().normal()
ly = (e2*E0).dual().normal()
lx = (e1*E0).dual().normal()
 
t0 = np.radians(90) - np.arccos((L2|ly).value[0])
t1 = np.radians(180) - np.arccos((L1|L2).value[0]) #angle between L1 and L2

print("\nExpected values of theta0:{},&  theta1:{} ".format(np.rad2deg(theta0),np.rad2deg(theta1)))
print("Obtained values of theta0:{},&  theta1:{} ".format(np.rad2deg(t0),np.rad2deg(t1)))
