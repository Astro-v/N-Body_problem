#### JEBRIL & VALENTIN ####
#### -- DISPLAY3D.PY --####

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


#-------- CONSTANT --------#
BLACK = [0, 0, 10]
WHITE = [255, 255, 255]
RED = [255, 0, 0]
YELLOW = [150,150,0]
GREEN = [0, 150, 0]
BLUE = [0, 0, 255]
ORANGE = [255, 150, 0]

def sphere(center: List[int],color: List[int],radius: float = 1): # Draw 3D sphere shape
	glBegin(GL_POLYGON)
	theta = -math.pi
	thetaList = np.linspace(-math.pi,+math.pi,20)
	phiList = np.linspace(0,2*math.pi,20)
	for theta in thetaList:
		for phi in phiList:
			glColor3f(color[0],color[1],color[2])
			glVertex3f(center[0]+radius*math.sin(theta)*math.cos(phi),center[1]+radius*math.sin(theta)*math.sin(phi),center[2]+radius*math.cos(theta))
	glEnd()

def grid(X): # Draw the several axes of the plan
	glBegin(GL_POINTS)
	x = np.linspace(-2*X,2*X,200)
	for i in range(len(x)):
		glColor3f(WHITE[0],WHITE[1],WHITE[2])
		glVertex3f(x[i],0,0)
		glVertex3f(0,x[i],0)
		glVertex3f(0,0,x[i])
	glEnd()

def point(pos: list,color: list): # Draw a point in the plan
	glBegin(GL_POINTS)
	glColor3f(color[0],color[1],color[2])
	glVertex3f(pos[0],pos[1],pos[2])
	glEnd()

def drawText(position: list, textString: str):     
    font = pygame.font.Font (None, 32)
    textSurface = font.render(textString, True, (255,255,255,255), (0,0,0,255))     
    textData = pygame.image.tostring(textSurface, "RGBA", True)     
    glRasterPos3d(*position)     
    glDrawPixels(textSurface.get_width(), textSurface.get_height(), GL_RGBA, GL_UNSIGNED_BYTE, textData)

def axes(theta: float,phi: float):
    eR = [-math.cos(phi)*math.sin(theta),+math.sin(phi),-math.cos(phi)*math.cos(theta)]
    eTheta = [-math.cos(theta),0,+math.sin(theta)]
    ePhi = [-math.sin(phi)*math.sin(theta),-math.cos(phi),-math.sin(phi)*math.cos(theta)]
    eZ = [math.cos(phi)*ePhi[0]+math.sin(phi)*eR[0],math.cos(phi)*ePhi[1]+math.sin(phi)*eR[1],math.cos(phi)*ePhi[2]+math.sin(phi)*eR[2]]
    return eR,eTheta,ePhi,eZ
				

def display(sys: System,method: str,xyzmax: float = 260000000.0,step: int = 200,ref: int = 0):
	"""
	sys: The system to display
	method: chose between two method "Euler" (default) or "RK4"
	"""

	#-------- INITIALIZATION --------#
	X = 800
	Y = 800
	Z = 800

	Xt=[[] for i in range(sys.N)]
	Yt=[[] for i in range(sys.N)]
	Zt=[[] for i in range(sys.N)]

	posText = [-X+10,Y-50,0]

	for j in range(sys.N):
	    Xt[j]=X*sys.body[j].p.x/xyzmax
	    Yt[j]=Y*sys.body[j].p.y/xyzmax
	    Zt[j]=Z*sys.body[j].p.z/xyzmax
	pygame.init()
	display = (X,Y)
	pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

	gluPerspective(90, (display[0]/display[1]), 0.1, 2*Z)
	eR = [0,0,1]
	eTheta = [1,0,0]
	ePhi = [0,1,0]
	phi = 0
	theta = 0
	eR,eTheta,ePhi,eZ = axes(theta,phi)
	posText = [eTheta[0]*(X-10)+ePhi[0]*(-Y+50),eTheta[1]*(X-10)+ePhi[1]*(-Y+50),eTheta[2]*(X-10)+ePhi[2]*(-Y+50)]
	
	angle = math.pi/500 # angle step for rotation
	glTranslatef(0.0,0.0,-Z) # initial position
	pygame.key.set_repeat(5, 5) # key repeat

	#-------- MAIN LOOP --------#
	while True:
	    #-------- EVENT --------#
		for event in pygame.event.get(): # There is some event 
			if event.type == pygame.QUIT: # Here the user clic on the quit button
				pygame.quit()
				quit()
			elif event.type == KEYDOWN: # Here the user push a key on the keyboard
				eR,eTheta,ePhi,eZ = axes(theta,phi)

				if  event.key == K_LEFT: # Here the user clic on the key left
					glRotatef(-angle*180/math.pi, eZ[0],eZ[1],eZ[2])
					glRotatef(angle*180/math.pi*2*math.sin(phi),eR[0],eR[1],eR[2])
					theta -= angle

				elif  event.key == K_RIGHT: # Here the user clic on the key right
					glRotatef(angle*180/math.pi, eZ[0],eZ[1],eZ[2])
					glRotatef(-angle*180/math.pi*2*math.sin(phi),eR[0],eR[1],eR[2])
					theta += angle

				elif  event.key == K_UP: # Here the user clic on the key up
					glRotatef(-angle*180/math.pi, eTheta[0],eTheta[1],eTheta[2])
					phi -= angle

				elif  event.key == K_DOWN: # Here the user clic on the key down
					glRotatef(angle*180/math.pi, eTheta[0],eTheta[1],eTheta[2])
					phi += angle
				elif event.key == K_0: # Here the user clic on the key 0
					ref = 0
				elif event.key == K_1:
					if sys.N > 1:
						ref = 1
				elif event.key == K_2:
					if sys.N > 2:
						ref = 2
				elif event.key == K_3:
					if sys.N > 3:
						ref = 3
				elif event.key == K_4:
					if sys.N > 4:
						ref = 4
				elif event.key == K_5:
					if sys.N > 5:
						ref = 5
				elif event.key == K_6:
					if sys.N > 6:
						ref = 6
				elif event.key == K_7:
					if sys.N > 7:
						ref = 7
				elif event.key == K_8:
					if sys.N > 8:
						ref = 8
				elif event.key == K_9:
					if sys.N > 9:
						ref = 9
				elif event.key == K_w:
					if xyzmax >= 20000000:
						xyzmax -=  1000000
				elif event.key == K_s:
					xyzmax += 1000000
			elif event.type == MOUSEBUTTONUP and event.button == 4: # Here the user roll the mouse wheel
				if xyzmax >= 20000000:
					xyzmax -=  3000000
			elif event.type == MOUSEBUTTONUP and event.button == 5:
				xyzmax += 3000000

		#-------- DISPLAY --------#
		glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
		grid(X)
		for j in range(sys.N):
			if sys.body[j].illuRadius == 1:
				point([Xt[j],Yt[j],Zt[j]],sys.body[j].color)
			else:
				sphere([Xt[j],Yt[j],Zt[j]],sys.body[j].color, sys.body[j].illuRadius) # display of the body
		if (method == "RK4"):
			sys.rk4(step) # we calculate the "step" next position
		else:
			sys.euler(step) # we calculate the "step" next position
		if ref != -1:
			for j in range(sys.N):
				Xt[j]=X*sys.body[j].p.x/xyzmax-X*sys.body[ref].p.x/xyzmax # we add the x,y and z position in the plan
				Yt[j]=Y*sys.body[j].p.y/xyzmax-Y*sys.body[ref].p.y/xyzmax
				Zt[j]=Z*sys.body[j].p.z/xyzmax-Z*sys.body[ref].p.z/xyzmax
		else:
			for j in range(sys.N):
				Xt[j]=X*sys.body[j].p.x/xyzmax
				Yt[j]=Y*sys.body[j].p.y/xyzmax
				Zt[j]=Z*sys.body[j].p.z/xyzmax

		eR,eTheta,ePhi,eZ = axes(theta,phi)
		posText = [eTheta[0]*(X-10)+ePhi[0]*(-Y+50),eTheta[1]*(X-10)+ePhi[1]*(-Y+50),eTheta[2]*(X-10)+ePhi[2]*(-Y+50)]
		drawText(posText,str(y(sys.t))+"y "+str(d(sys.t))+"d "+str(h(sys.t))+"h")
		pygame.display.flip()
	

def y(sec):
	return (sec//(3600*24*365))

def d(sec):
	return (sec//(3600*24))%365

def h(sec):
	return (sec//(3600))%24

