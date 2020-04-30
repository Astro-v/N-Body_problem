from Body import *
import numpy as np
from typing import List

'''
the system class manages all the N-body system and manages the simulation
'''
class System:
    def __init__(self,dt: float = 10**(-3),name,p0: List[Vector] = [],v0: List[Vector] = [],m: list = [],radius: list = [],illuRadius: list = [],color: list = []):
        ''' 
        Initialize the N-Body system
        name : array of the names of the bodies
        p0,v0 are [3,N] (in 3D) and m,radius are [1,N] array that contain:
        p0 : initial position
        v0 : initial velocity
        m : mass
        radius : radius of the several bodies
        illuRadius : radius of the illustrations of the several bodies
        dt : infinitesimal time
        '''
        
        self.t = 0
        self.dt = dt
        self.N = len(p0)
        self.body = []
        for i in range(0,self.N,1):
            self.body.append(Body(name[i],p0[i],v0[i],m[i],radius[i]),illuRadius[i],color[i])
           
        
    def addBody(self,name,p0: Vector,v0: Vector,m: float,radius: float, illuRadius: float = 1,color: list[int] = [255,255,255]):
        ''' 
        Add a body to the system
        name : name of the body
        p0,v0 are Vectors and m,radius are floats that contain :
        p0 : initial position
        v0 : initial velocity
        m : mass
        radius : radius of the body
        illuRadius : radius of the illustration of the body
        '''
        
        self.N = self.N +1
        self.body.append(Body(name,p0,v0,m,radius,illuRadius,color))
       
    
    def __iadd__(self,other: Body): # Allow to do "system += body" in order to add a body to the system
        if not other.__class__ is Body:
            print("Error: argument not a Body")
            return NotImplemented
        self.N = self.N +1
        self.body.append(other)
        return self


    def euler(self,stepMax: float):
        ''' 
        resolve the N-Body problem until stepMax with the euler method
        '''

        G = 6.674*10**(-20)
        forces = [[0 for i in range(self.N)] for j in range(self.N)]
        for step in range(stepMax):
            for i in range(self.N):
                for j in range(self.N):
                    if j>i:
                        forces[i][j] = (self.body[j].p-self.body[i].p).mult(G*self.body[i].m*self.body[j].m/(self.body[i].p-self.body[j].p).norm()**3)
                    elif i==j:
                        forces[i][j] = Vector()
                    else:
                        forces[i][j] = -forces[j][i]
            for i in range(self.N):
                self.body[i].p = Vector(self.body[i].p.x+self.dt*(self.body[i].v.x),self.body[i].p.y+self.dt*(self.body[i].v.y),self.body[i].p.z+self.dt*(self.body[i].v.z))
                self.body[i].v = self.body[i].v+sumV(forces[i][:]).mult(self.dt/self.body[i].m)
            self.t+=self.dt


