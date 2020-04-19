from Body import *
import numpy as np
from typing import List

'''
the system class manages all the N-body system and manages the simulation
'''
class System:
    def __init__(self,dt: float = 10**(-3),p0: List[Vector] = [],v0: List[Vector] = [],m: list = [],radius: list = []):
        ''' 
        Initialize the N-Body system
        p0,v0,m,radius are array that contain:
        p0 : initial position
        v0 : initial velocity
        m : mass
        radius : radius of the several body
        dt : infinitesimal time
        '''
        
        self.t = 0
        self.dt = dt
        self.N = len(p0)
        self.body = []
        for i in range(0,self.N,1):
            self.body.append(Body(p0[i],v0[i],m[i],radius[i]))
           
        
    def addBodyI(self,p0: Vector,v0: Vector,m: float,radius: float):
        ''' 
        Add a body to the system
        p0,v0,m,radius are integer that contain :
        p0 : initial position
        v0 : initial velocity
        m : mass
        radius : radius of the body
        '''
        
        self.N = self.N +1
        self.body.append(Body(p0,v0,m,radius))

    def addBodyII(self,body: Body):
        ''' 
        Add a body to the system
        p0,v0,m,radius are integer that contain :
        p0 : initial position
        v0 : initial velocity
        m : mass
        radius : radius of the body
        '''
        
        self.N = self.N +1
        self.body.append(body)
       
    def __iadd__(self,other: Body): # Allow to do "system += body" in order to add a body to the system
        if not other.__class__ is Body:
            print("Error: argument not a Body")
            return NotImplemented
        self.N = self.N +1
        self.body.append(other)
        return self

    def euler(self,tmax: float):
        ''' 
        Resolve the N-Body problem until tmax with the euler method
        It resolve the problem but with a self.N**2 complexity
        '''

        G = 6.674*10**(-20)
        forces = [[0 for i in range(self.N)] for j in range(self.N)]
        while self.t < tmax:
            for i in range(self.N):
                for j in range(self.N):
                    if j>i:
                        forces[i][j] = (self.body[j].p[-1]-self.body[i].p[-1]).mult(G*self.body[i].m*self.body[j].m/(self.body[i].p[-1]-self.body[j].p[-1]).norm()**3)
                    elif i==j:
                        forces[i][j] = Vector()
                    else:
                        forces[i][j] = -forces[j][i]
            for i in range(self.N):
                (self.body[i].p).append(Vector(self.body[i].p[-1].x+self.dt*(self.body[i].v[-1].x),self.body[i].p[-1].y+self.dt*(self.body[i].v[-1].y),self.body[i].p[-1].z+self.dt*(self.body[i].v[-1].z)))
                (self.body[i].v).append(self.body[i].v[-1]+sum(forces[i][:]).mult(self.dt/self.body[i].m))
            self.t+=self.dt


def sum(T: List[Vector]):
    s = Vector()
    for i in range(len(T)):
        s += T[i]
    return s


     
