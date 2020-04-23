import pygame
from System import *
from Body import *
from Vector import *

"""
BLACK = [0, 0, 10]
WHITE = [255, 255, 255]
RED = [255, 0, 0]
YELLOW = [150,150,0]
GREEN = [0, 150, 0]
BLUE = [0, 0, 255]
"""


def display(sys: System,xymax: int = 300000000,nbr: int = 300,step: int = 100):
  """
  sys: system
  nbr : number of saved value
  step : number of step between 2 display
  """
	pygame.init()
	taillex = 500
	tailley = 500
	taille = [2*taillex, 2*tailley]

	Xt=[[] for i in range(sys.N)]
	Yt=[[] for i in range(sys.N)]

	for j in range(sys.N):
	    Xt[j].append(int(taillex*sys.body[j].p.x/xymax))
	    Yt[j].append(int(tailley*sys.body[j].p.y/xymax))

	screen = pygame.display.set_mode(taille)

	clock = pygame.time.Clock()

	ref = 0 # reference body
	end = 0
	i = 0 
	while end == 0: # while we don't wanna stop
	    for event in pygame.event.get(): # if we want to shut the program (red cross)
	        if event.type == pygame.QUIT:
	            end = 1
	    
	    screen.fill(BLACK)
	    for j in range(sys.N):
	        if i<nbr: # display of the following line
	            pygame.draw.circle(screen, sys.body[j].color, [taillex + Xt[j][i],tailley + Yt[j][i]], sys.body[j].radius) # display of the body
	            for k in range(i-1):
	                pygame.draw.line(screen,sys.body[j].color, [taillex + Xt[j][i-k], tailley + Yt[j][i-k]],[taillex + Xt[j][i-k-1], tailley + Yt[j][i-k-1]])
	        else:
	            pygame.draw.circle(screen, sys.body[j].color, [taillex + Xt[j][nbr-1],tailley + Yt[j][nbr-1]], sys.body[j].radius) # display of the body
	            for k in range(nbr-1):
	                pygame.draw.line(screen,sys.body[j].color, [taillex + Xt[j][k], tailley + Yt[j][k]],[taillex + Xt[j][k+1], tailley + Yt[j][k+1]])
	    i+=1
	    sys.eulerStep(step) # we calculate the "step" next position
	    for j in range(sys.N):
	        if ref >=0:
		        if len(Xt[j])<nbr:
		            Xt[j].append(int(taillex*sys.body[j].p.x/xymax)-int(taillex*sys.body[ref].p.x/xymax)) # we add the x and y position in the plan
		            Yt[j].append(int(tailley*sys.body[j].p.y/xymax)-int(tailley*sys.body[ref].p.y/xymax))
		        else:
		            for k in range(len(Xt[j])-1):
		                Xt[j][k] = Xt[j][k+1]
		                Yt[j][k] = Yt[j][k+1]
		            Xt[j][-1] = int(taillex*sys.body[j].p.x/xymax)-int(taillex*sys.body[ref].p.x/xymax)
		            Yt[j][-1] = int(tailley*sys.body[j].p.y/xymax)-int(tailley*sys.body[ref].p.y/xymax)
	        else:
		        if len(Xt[j])<nbr:
		            Xt[j].append(int(taillex*sys.body[j].p.x/xymax)) # we add the x and y position in the plan
		            Yt[j].append(int(tailley*sys.body[j].p.y/xymax))
		        else:
		            for k in range(len(Xt[j])-1):
		                Xt[j][k] = Xt[j][k+1]
		                Yt[j][k] = Yt[j][k+1]
		            Xt[j][-1] = int(taillex*sys.body[j].p.x/xymax)
		            Yt[j][-1] = int(tailley*sys.body[j].p.y/xymax)
	    pygame.display.flip() # 
	   
	    
	pygame.quit()
