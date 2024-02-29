## To ignore all the NumbaDeprecationWarnings. GOD! too many of them.
from numba.core.errors import NumbaDeprecationWarning, NumbaPendingDeprecationWarning
import warnings
warnings.simplefilter('ignore', category=NumbaDeprecationWarning)
warnings.simplefilter('ignore', category=NumbaPendingDeprecationWarning)

import numpy as np
from clifford import Cl, conformalize
from clifford.tools.g3 import generate_rotation_rotor
from clifford.tools.g3c import apply_rotor


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
	## Assuming our base of the robot is at origin
	#Cbase = up(0*e1+0*e2+0*e3) 

	### This Cbase is chose from GAME2020 presentation
	## from visualizing the Cbase using pyganja
	## gs = GanjaScene()
	## gs.add_object(Cbase, color=Color.BLUE)

	### Render the scene using the GanjaScene renderer
	## draw(gs, 
	##      static=False , 
	##      scale=0.1)
	Cbase = (up(0.2*e1)^up(0.2*e3)^up(-0.2*e1)).normal()
	## Turns out a circle. 

	## Giving the EE some position value.
	EE = (2.59077^e1) + (0.48236^e2) + (2.59077^e3)
	## Storing Psuedoscalar in varible for simplicity
	I = G3c.pseudoScalar #e12345

	######## FIRST: Generate Contrains !!! ############
	# Defining a Sphere at the EE
	Sy = I*(EE-0.5*np.square(l2)*einf)
	# Construct a sphere at the base
	S_base = I*(up(0)-0.5*np.square(l1)*einf) #here the center is the origin & not Cbase (still figuring out)
	# Intersection of Sphere, i.e. Sy ^ S_base
	C = Sy & S_base # basically here &-operator= Meet operation.

	## To understand how this circle looks like, lets break it down
	## Reference: https://clifford.readthedocs.io/en/latest/_modules/clifford/tools/g3c.html?highlight=get_circle_in_euc#
	## get_circle_in_euc(circle) --> Extracts all the normal stuff for a circle

	'''
	In [85]: from clifford.tools.g3c import get_circle_in_euc
	In [86]: get_circle_in_euc(C)
	Out[86]: 
	[-(0.37941^e1) - (0.07064^e2) - (0.37941^e3),
	 -(0.70106^e1) - (0.13053^e2) - (0.70106^e3),
	 1.9253848136188636]

	'''

	## Generating a plane that passes through the eo, e3 & EE  
	plane = eo^up(e3)^EE^einf

	## Generating the constrains
	if plane == 0:
		constrain = C 
		## the generated plane = 0 iff EE = constant x e3
		## E.g)
		'''
		In [218]: eo^up(e3)^up(2*e3)^einf == 0
		Out[218]: True
		'''
	else:
		constrain = C & plane # the intersaction betw two sphere and the plane(passing throug eo and elbow(aka X)) 


	######## Second: Computing the angles #######
	
	print("Highest Grades within the generated plane",plane.grades())

	if plane.grades() == {3}:
		print("the end effector lies on the Z axis.")
		t0 = np.radians(0)

		## Elbow's pose aka X(can be 2 points, since circle & plane = 2 solutions)
		X = constrain &  (eo^up(e3)^up(e1)^einf) # remove the rotation from x, intersect it with the plane of the links

	else:
		t0 = np.arctan2(EE[(3,)],EE[(1,)]) 
		## Creating a anti-rotor ??
		R0 = generate_rotation_rotor(t0,e1,e3) ## Base --> Shoulder
		# X = R0 * (constrain * ~R) ## Or same as below
		X = apply_rotor(constrain,~R0)

	# project out one end of the point-pair
	x = (1 - X.normal()) * (X | einf)

	x_down = down(x)
	t1 = np.arctan2(x_down[(2,)], x_down[(1,)])
	#Update the rotors
	R1 = generate_rotation_rotor(t1,e1,e2) ## Shoulder--> Upper

	R01 = R0*R1
	Rl1 = 1 - 0.5*l1*(e1^einf) ## Upper --> Elbow(X)
	R_X = R01*Rl1

	# remove the second rotor
	Y = apply_rotor(EE, ~R_X) #generating an anti-rotor
	y_down = down(Y)

	t2 = np.arctan2(-y_down[(2,)], -y_down[(1,)])
	R2 = generate_rotation_rotor(t1, e1, e2)
	R02 = R_X * R2
	#Updating the rotor from Forearm --> EE
	Rl2 = 1 - 0.5*l2*(e1^einf)
	R = R02 * Rl2


	print("Expected values of theta0:{}, theta1:{} & theta2:{}".format(np.rad2deg(theta0),np.rad2deg(theta1),np.rad2deg(theta2)))
	print("Obtained values of theta0:{}, theta1:{} & theta2:{}".format(np.rad2deg(t0),np.rad2deg(t1),np.rad2deg(t2)))

	# print("Generated Rotor: ", R)



if __name__ == '__main__':
	main()