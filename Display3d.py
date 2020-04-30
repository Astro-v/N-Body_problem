import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import math
import numpy as np
from typing import List

from System import *
from Body import *
from Vector import *


BLACK = [0, 0, 10]
WHITE = [255, 255, 255]
RED = [255, 0, 0]
YELLOW = [150,150,0]
GREEN = [0, 150, 0]
BLUE = [0, 0, 255]

def sphere(center: List[int],color: List[int],radius: float = 1):
	glBegin(GL_POLYGON)
	theta = -math.pi
	thetaList = np.linspace(-math.pi,+math.pi,10)
	phiList = np.linspace(0,2*math.pi,10)
	for theta in thetaList:
		for phi in phiList:
			glColor3f(color[0],color[1],color[2])
			glVertex3f(center[0]+radius*math.sin(theta)*math.cos(phi),center[1]+radius*math.sin(theta)*math.sin(phi),center[2]+radius*math.cos(theta))
	glEnd()

def grille():
	glBegin(GL_POINTS)
	x = np.linspace(-2*X,2*X,200)
	for i in range(len(x)):
		glColor3f(WHITE[0],WHITE[1],WHITE[2])
		glVertex3f(x[i],0,0)
		glVertex3f(0,x[i],0)
		glVertex3f(0,0,x[i])
	glEnd()

def display(sys: System,xyzmax: float = 260000000.0,step: int = 200,ref: int = 0):
	X = 800
	Y = 800
	Z = 800

	Xt=[[] for i in range(sys.N)]
	Yt=[[] for i in range(sys.N)]
	Zt=[[] for i in range(sys.N)]

	for j in range(sys.N):
	    Xt[j]=X*sys.body[j].p.x/xyzmax
	    Yt[j]=Y*sys.body[j].p.y/xyzmax
	    Zt[j]=Z*sys.body[j].p.z/xyzmax
	pygame.init()
	display = (X,Y)
	pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

	gluPerspective(90, (display[0]/display[1]), 0.1, 2*Z)

	glTranslatef(0.0,0.0,-Z) # initial position
	glRotatef(45, 45, 45, 0)
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
		grille()
		for j in range(sys.N):
			sphere([Xt[j],Yt[j],Zt[j]],sys.body[j].color, sys.body[j].illuRadius) # display of the body
		sys.euler(step) # we calculate the "step" next position
		for j in range(sys.N):
			Xt[j]=X*sys.body[j].p.x/xyzmax-X*sys.body[ref].p.x/xyzmax # we add the x,y and z position in the plan
			Yt[j]=Y*sys.body[j].p.y/xyzmax-Y*sys.body[ref].p.y/xyzmax
			Zt[j]=Z*sys.body[j].p.z/xyzmax-Z*sys.body[ref].p.z/xyzmax
		pygame.display.flip()
		#pygame.time.wait(10)

