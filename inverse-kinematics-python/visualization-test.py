from numba.core.errors import NumbaDeprecationWarning, NumbaPendingDeprecationWarning
import warnings
warnings.simplefilter('ignore', category=NumbaDeprecationWarning)
warnings.simplefilter('ignore', category=NumbaPendingDeprecationWarning)

from clifford.g3c import *
from clifford.tools.g3c import *
from pyganja import *

P1 = up(random_euc_mv()*0.1)
P2 = up(random_euc_mv()*0.1)
P3 = up(random_euc_mv()*0.1)
P4 = up(random_euc_mv()*0.1)

# The sphere is the outer product of all 4
S = (P1^P2^P3^P4).normal()

# A line is the outer product of 2 with ninf
L = P1^P2^einf

# The inversion of a line in a sphere is a circle
C = S*L*S

# The tangent to the circle at the intersection point is the reflected line
Ldash = (P1|C)^einf

# The tangent plane to the sphere at the intersection point can be easily found
Ppi = (P1|S)^einf

sc = GanjaScene()
sc.add_objects([P1,P2,P3,P4], color=Color.BLACK)
sc.add_objects([L], color=Color.BLUE)
sc.add_objects([Ldash], color=Color.RED)
sc.add_objects([C], color=Color.RED)
sc.add_objects([S*einf*S], color=Color.BLACK)
sc.add_objects([S])
sc.add_objects([Ppi], color=rgb2hex((0,100,0))+int('70000000',16))
# draw(sc,scale=0.5)
draw(sc, 
	static=False ,
	scale=0.1,
	grid= True,
	labels=True)