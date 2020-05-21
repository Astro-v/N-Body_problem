#### JEBRIL & VALENTIN ####
#### ---- MAIN.PY ---- ####

from System import *
from Body import *
from Vector import *
import math
import random
from Display3d import *
"""
SIMU : different kind of simulation
0:  Simple 2 body system with euler
1:  2 body system with a satelite
2:	Colision between 2 body
3:	Solar System
4:  Moon around the earth
5:	Solar system with an astroid
6:  Fun : 100 asteroid around sun
"""
SIMU = 0


#-------- 0 --------#
if SIMU == 0:
	xyzmax = 300000000 # Scale
	ref = -1 # Body ref
	step = 100 # number of step between 2 display
	dt = 100 # time step
	sys = System(dt)
	sys+=Body("1",Vector(150000000,0,0),Vector(0,2,0),1*(10**30),100000,10,BLUE)
	sys+=Body("2",Vector(-150000000,0,0),Vector(0,-2,0),1*(10**30),100000,10,RED)
	#method = "RK4"
	method = "Euler"
	display(sys,method,xyzmax,step,ref)

#-------- 1 --------#
if SIMU == 1:
	xyzmax = 300000000 # Scale
	ref = -1 # Body ref
	step = 100 # number of step between 2 display
	dt = 100 # time step
	sys = System(dt)
	sys+=Body("1",Vector(150000000,0,0),Vector(0,2,0),1*(10**30),100000,10,YELLOW)
	sys+=Body("2",Vector(-150000000,0,0),Vector(0,-2,0),1*(10**30),100000,10,YELLOW)
	sys+=Body("3",Vector(100000000,100000000,100000000),Vector(-10,2,0),1*(10**20),10000,4,WHITE)
	#method = "RK4"
	method = "Euler"
	display(sys,method,xyzmax,step,ref)


#-------- 2 --------#
if SIMU == 2:
	xyzmax = 300000000 # Scale
	ref = -1 # Body ref
	step = 100 # number of step between 2 display
	dt = 100 # time step
	sys = System(dt)
	sys+=Body("1",Vector(0,0,0),Vector(-0,0,0),1*(10**30),100000,10,WHITE)
	sys+=Body("2",Vector(-150000000,0,0),Vector(+60,0,0),1*(10**29),100000,8,WHITE)
	method = "RK4"
	#method = "Euler"
	display(sys,method,xyzmax,step,ref)


#-------- 3 --------#
if SIMU == 3:
	xyzmax = 1400000000 # Scale
	ref = 0 # Sun in the middle
	step = 100 # number of step between 2 display
	dt = 100 # time step
	sys = System(dt)
	sys+=Body("Sun",Vector(0,0,0),Vector(0,0,0),1.9891*(10**30),696340,10,YELLOW)
	sys+=Body("Earth",Vector(149597887.5,0,0),Vector(0,29.783,0),5.972*(10**24),6371,4,BLUE)
	sys+=Body("Mars",Vector(206655000,0,0),Vector(0,26.50,0),6.4185*(10**23),3389.5,3,RED)
	sys+=Body("Moon",Vector(149597887.5+384400,0,0),Vector(0,29.783+1,0),7.36*(10**22),1737.1,2,WHITE)
	sys+=Body("Jupiter",Vector(-816000000,0,0),Vector(0,-12.448,0),7.36*(10**27),71492,7,ORANGE)
	sys+=Body("Mercury",Vector(46001000,0,0),Vector(0,58.9859,0),3.3011*(10**23),71492,3,WHITE)
	sys+=Body("Saturn",Vector(1503500000,0,0),Vector(0,9.141,0),5.6846*(10**26),71492,6,RED)
	# method = "RK4"
	method = "Euler"
	display(sys,method,xyzmax,step,ref)

#-------- 4 --------#
if SIMU == 4:
	xyzmax = 1000000 # Scale
	ref = 1 # Earth in the middle
	step = 100 # number of step between 2 display
	dt = 50 # time step
	sys = System(dt)
	sys+=Body("Sun",Vector(0,0,0),Vector(0,0,0),1.9891*(10**30),696340,10,YELLOW)
	sys+=Body("Earth",Vector(149597887.5,0,0),Vector(0,29.783,0),5.972*(10**24),6371,6,BLUE)
	sys+=Body("Moon",Vector(149597887.5+384400,0,0),Vector(0,29.783+1,0),7.36*(10**22),1737.1,3,WHITE)
	method = "RK4"
	# method = "Euler"
	display(sys,method,xyzmax,step,ref)

#-------- 5 --------#
if SIMU == 5:
	xyzmax = 300000000 # Scale
	ref = 0 # Sun in the middle
	step = 100 # number of step between 2 display
	dt = 100 # time step
	sys = System(dt)
	sys+=Body("Sun",Vector(0,0,0),Vector(0,0,0),1.9891*(10**30),696340,10,YELLOW)
	sys+=Body("Earth",Vector(149597887.5,0,0),Vector(0,29.783,0),5.972*(10**24),6371,4,BLUE)
	sys+=Body("Mars",Vector(206655000,0,0),Vector(0,26.50,0),6.4185*(10**23),3389.5,3,RED)
	sys+=Body("Mercury",Vector(46001000,0,0),Vector(0,58.9859,0),3.3011*(10**23),71492,3,WHITE)
	sys+=Body("Asteroid",Vector(149597887.5/2,149597887.5/2,-149597887.5/2),Vector(0,20,0),10*(10**22),2000,3,GREEN)
	# method = "RK4"
	method = "Euler"
	display(sys,method,xyzmax,step,ref)


#-------- 6 --------#
if SIMU == 6:
	xyzmax = 300000000
	ref = 0
	step = 1
	dt = 10000
	sys = System(dt)
	sys += Body("Sun",Vector(0,0,0),Vector(0,0,0),1.9891*(10**30),696340,10,YELLOW)
	for i in range(0,100):
		d = (149597887.5+(random.random()-0.5)*2*70000000)
		v = (random.random()-0.5)*2*30
		theta = random.random()*math.pi*2
		sys+=Body(str(i),Vector(math.cos(theta)*d,math.sin(theta)*d,(random.random()-0.5)*2*7000000),Vector(-math.sin(theta)*(30+v),math.cos(theta)*(30+v),0),5.0*(10**18),100,1,WHITE)
	method = "RK4"
	# method = "Euler"

	display(sys,method,xyzmax,step,ref)
