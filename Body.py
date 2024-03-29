#### JEBRIL & VALENTIN ####
#### ---- BODY.PY ---- ####

from Vector import *
from typing import List

class Body:
    def __init__(self,name,p0: Vector,v0: Vector,m: float,radius : float,illuRadius : float = 1,color: List[int] = [0,0,0]):
        self.name = name
        self.p = p0
        self.v = v0
        self.m = m
        self.radius = radius
        self.illuRadius = illuRadius
        self.color = color
        
    def __str__(self):
        return "Its current position is "+self.p.__str__()+" (en km).\n""Its current speed is "+self.v.__str__()+" (en km.s-1).\n""Its mass is "+str(self.m)+" kg.\n""Its radius is "+str(self.radius)+" km."

