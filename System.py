from Body import *
import numpy as np
from typing import List


'''
the system class manages all the N-body system and manages the simulation
'''
class System:
    def __init__(self,dt: float = 10**(-3),name: List[str] = [],p0: List[Vector] = [],v0: List[Vector] = [],m: list = [],radius: list = [],illuRadius: list = [],color: list = []):
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
           
        
    def addBody(self,name,p0: Vector,v0: Vector,m: float,radius: float, illuRadius: float = 1,color: list = [255,255,255]):
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
        
        self.name.append(name)
        self.p0.append(p0)
        self.v0.append(v0)
        self.m.append(m)
        self.radius.append(radius)
        self.illuRadius.append(illuRadius)
        self.color.append(color)
        self.N = self.N +1
        self.body.append(Body(name,p0,v0,m,radius,illuRadius,color))
       
    
    def __iadd__(self,other: Body): # Allow to do "system += body" in order to add a body to the system
        if not other.__class__ is Body:
            print("Error: argument not a Body")
            return NotImplemented
        self.name.append(other.name)
        self.p0.append(other.p)
        self.v0.append(other.v)
        self.m.append(pther.m)
        self.radius.append(other.radius)
        self.illuRadius.append(other.illuRadius)
        self.color.append(other.color)
        self.N = self.N +1
        self.body.append(other)
        return self
    
    
    def removeBody(self,name):
        k = 0
        while self.name[k] != name or k < self.N:
            k += 1
        if k = self.N:
            print(name,"is not part of the system")
        if k = self.N-1:
            self.body = self.body[:k]
            self.N = self.N - 1
        else:
            self.body = self.body[:,k] + self.body[k+1:]
            self.N = self.N - 1
    
    
    def collision(self, nameA, nameB):
        i = 0
        j = 0
        for k in range(self.N):
            if self.name[k] == nameA:
                i = k
            if self.name[k] == nameB:
                j = k
        A = self.body[i]
        B = self.body[j]
        name = nameA + "+" + nameB
        m = A.m + B.m
        p0 = (A.m*A.p + B.m*B.p)/(A.m + B.m)
        v0 = (A.m*A.v + B.m*B.v)/(A.m + B.m)
        radius = (A.radius**3 + B.radius**3)**(1/3)
        if A.m > B.m : 
            illuRadius = A.illuRadius
            color = A.color
        else:
            illuRadius = B.illuRadius
            color = B.color
        removeBody(self,nameA)
        removeBody(self,nameB)
        addBody(self,name,p0,v0,m,radius, illuRadius,color)
        
        
    def f(self,p0,v0):
        F = 0
        for i in range(self.N):
            force = 0
            for j in range(self.N):
                if j != i:
                    force += (self.body[j].p-p0[i]).mult(G*self.body[i].m*self.body[j].m/(self.body[i].p-p0[i]).norm()**3)
            F.append(force/(self.body[i].m))
        return (v0,F)


    def euler(self,stepMax: float):
        ''' 
        resolve the N-Body problem until stepMax with the euler method
        '''

        G = 6.674*10**(-20)
        forces = [[0 for i in range(self.N)] for j in range(self.N)]
        for step in range(stepMax):
            if EULER = 1:
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
            elif RK4 = 1:
                p0 = []
                v0 = []
                for j in range(self.N):
                    p0.append(self.body[j].p)
                    v0.append(self.body[j].v)
                k1 = f(self,p0,v0)
                k2 = f(self,[[p0[k][l] + dt/2*k1[0][k][l] for l in range(3)] for k in range(self.N)],[[v0[k][l] + dt/2*k1[1][k][l] for l in range(3)] for k in range(self.N)])
                k3 = f(self,[[p0[k][l] + dt/2*k2[0][k][l] for l in range(3)] for k in range(self.N)],[[v0[k][l] + dt/2*k2[1][k][l] for l in range(3)] for k in range(self.N)])
                k4 = f(self,[[p0[k][l] + dt*k3[0][k][l] for l in range(3)] for k in range(self.N)],[[v0[k][l] + dt*k3[1][k][l] for l in range(3)] for k in range(self.N)])
                p = [[self.body[k].p[l] + dt/6*(k1[0][k][l] + 2*k2[0][k][l] + 2*k3[0][k][l] + k4[0][k][l]) for l in range(3)] for k in range(self.N)]
                v = [[self.body[k].v[l] + dt/6*(k1[1][k][l] + 2*k2[1][k][l] + 2*k3[1][k][l] + k4[1][k][l]) for l in range(3)] for k in range(self.N)]
                for i in range(self.N):
                    self.body[i].p = p[i]
                    self.body[i].v = v[i]
            self.t+=self.dt


