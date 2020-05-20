from System import *
from Body import *
from Vector import *

from Display3d import *

xyzmax = 300000000
ref = 0
step = 100
dt = 100
sys = System(dt)
earth = Body("Earth",Vector(149597887.5,0,0),Vector(0,29.783,0),5.972*(10**24),1,6,BLUE)
sun = Body("Sun",Vector(0,0,0),Vector(0,0,0),1.9891*(10**30),1,10,YELLOW)
mars = Body("Mars",Vector(206655000,0,0),Vector(0,26.50,0),6.4185*(10**23),1,3,RED)
moon = Body("Moon",Vector(149597887.5+384400,0,0),Vector(0,29.783+1,0),7.36*(10**22),1,1,WHITE)
sat = Body("Sat",Vector(149597887.5/2,149597887.5/2,-149597887.5/2),Vector(0,20,0),7.36*(10**22),1,3,GREEN)
sys+=sun
sys+=earth
sys += sat

display(sys,xyzmax,step,ref)
