from System import *
from Body import *
from Vector import *

for Display3d import *

step = 100
dt = 100
nbr = 500
sys = System(dt)
earth = Body(Vector(149597887.5,0,0),Vector(0,29.783,0),5.972*(10**24),6,BLUE)
sun = Body(Vector(0,0,0),Vector(0,0,0),1.9891*(10**30),10,YELLOW)
mars = Body(Vector(206655000,0,0),Vector(0,26.50,0),6.4185*(10**23),3,RED)
moon = Body(Vector(149597887.5+384400,0,0),Vector(0,29.783+1,0),7.36*(10**22),1,WHITE)
sat = Body(Vector(149597887.5/2,149597887.5/2,-149597887.5/2),Vector(0,20,0),7.36*(10**22),3,GREEN)
sys+=sun
sys+=earth
sys += sat

display(sys)
