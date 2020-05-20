from System import *
from Body import *
from Vector import *

from Display3d import *

xyzmax = 300000000
ref = 0
step = 100
dt = 100
sys = System(dt)
earth = Body("Earth",Vector(149597887.5,0,0),Vector(0,29.783,0),5.972*(10**24),6371,6,BLUE)
sun = Body("Sun",Vector(0,0,0),Vector(0,0,0),1.9891*(10**30),696340,10,YELLOW)
mars = Body("Mars",Vector(206655000,0,0),Vector(0,26.50,0),6.4185*(10**23),3389.5,3,RED)
moon = Body("Moon",Vector(149597887.5+384400,0,0),Vector(0,29.783+1,0),7.36*(10**22),1737.1,1,WHITE)
sat = Body("Sat",Vector(149597887.5/2,149597887.5/2,-149597887.5/2),Vector(0,20,0),7.36*(10**22),2000,3,GREEN)
sat2 = Body("Sat2",Vector(49597887.5,0,0),Vector(0,0,0),1.9891*(10**23),696340,10,WHITE)
sys+=sun
sys+=earth
sys += sat
sys += mars
sys += sat2

# method = "RK4"
method = "Euler"

display(sys,method,xyzmax,step,ref)
