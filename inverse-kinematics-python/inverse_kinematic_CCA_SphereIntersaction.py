## To ignore all the NumbaDeprecationWarnings. GOD! too many of them.
from numba.core.errors import NumbaDeprecationWarning, NumbaPendingDeprecationWarning
import warnings
warnings.simplefilter('ignore', category=NumbaDeprecationWarning)
warnings.simplefilter('ignore', category=NumbaPendingDeprecationWarning)

import numpy as np
from clifford import Cl, conformalize


## Defining the Cl(3,1) signatures.
G3, blades_g2 = Cl(3)
G3c, blades_g3c, stuff = conformalize(G3)
# PUtting the symbolic variables in local namespace.
locals().update(blades_g3c)
locals().update(stuff)


def main():
	
	l1 = 2 # units length
	l2 = 2 # units length
	theta0 = np.radians(45)
	theta1 = np.radians(30)
	theta2 = np.radians(-45)

	# Robotics Base
	Cbase = (up(0.2*e1)^up(0.2*e3)^up(-0.2*e1)).normal()

	## Giving the EE some position value.
	EE = up((2.59077^e1) + (0.48236^e2) + (2.59077^e3))
	# EE = up(3.6639^e1 + 0.48236^e3)
	## Storing Psuedoscalar in varible for simplicity
	I = G3c.pseudoScalar #e12345

	######## FIRST: Generate Contrains !!! ############
	# Defining a Sphere at the EE
	Sy = I*(EE-0.5*np.square(l2)*einf) # == (EE-0.5*np.square(l2)*einf).dual()
	# Construct a sphere at the base
	S_base = I*(up(0)-0.5*np.square(l1)*einf) #==(up(0)-0.5*np.square(l1)*einf).dual()
	# Intersection of Sphere, i.e. Sy ^ S_base
	C = S_base & Sy # basically here &-operator= Meet operation.

	## Generating a plane that passes through the EE and 
	plane = EE^up(0)^up(1*e2)^einf
	
	PP = -(plane & C)


	# The square of the point pair describes if the spheres intersect
	if float((PP*PP)(0)) > 0:
		print("inside")
		# If the spheres intersect then we can just choose one solution
		# print(1+PP*(np.sqrt(float(PP*PP)))*(PP|einf))
		# print((1 + PP.normal())*(PP|einf))
		elb = (1+PP*(np.sqrt(float((PP*PP)(0))))*(PP|einf))
		endpoint = EE
	else:
		# If the spheres do not intersect then we will just reach for the object.
		endpoint = up((l1+l2)*down(EE).normal())
		elb = up(l1*down(EE).normal())

	## Get the angles
	L1 = (elb^EE^einf).normal() #(elb.normal()^EE^einf).normal() 
	L2 = (elb^eo^einf).normal() 
	L1proj = ((L1|(Cbase^einf))|(Cbase^einf)).normal()
	downt = down(EE).normal()
	t0 = np.arctan2(float((downt|e3)(0)), float((downt|e1)(0)))
	print(L2|L1proj)
	t1 = np.arccos(float((L2|L1proj)(0)))
	t2 = np.arccos(float((L1|L2)(0)))

	print("Expected values of theta0:{}, theta1:{} & theta2:{}".format(np.rad2deg(theta0),np.rad2deg(theta1),np.rad2deg(theta2)))
	print("Obtained values of theta0:{}, theta1:{} & theta2:{}".format(np.rad2deg(t0),np.rad2deg(t1),np.rad2deg(t2)))



if __name__ == '__main__':
	main()