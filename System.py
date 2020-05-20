from Body import *
import numpy as np
from typing import List


G = 6.674*10**(-20)

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

        self.N = self.N +1
        self.body.append(Body(name,p0,v0,m,radius,illuRadius,color))
       
    
    def __iadd__(self,other: Body): # Allow to do "system += body" in order to add a body to the system
        if not other.__class__ is Body:
            print("Error: argument not a Body")
            return NotImplemented

        self.N = self.N +1
        self.body.append(other)
        return self
    
    
    def removeBody(self,i: int):
        """
        Remove the body indexed by i
        """
        
        if i >= self.N or i < 0:
            print("Error: index out of range")
        else:
            self.body = [self.body[j] for j in range(0,self.N,1) if j!=i]
            self.N = self.N-1


    
    def collision(self):
        """
        Takes into consideration collisions
        return the number of colision
        """
        for i in range(0,self.N-1,1):
                for j in range(i+1,self.N,1):
                    if (self.body[i].p-self.body[j].p).norm() < self.body[i].radius+self.body[j].radius:
                        name = self.body[i].name + "+" + self.body[j].name
                        m = self.body[i].m + self.body[j].m
                        p0 = self.body[i].p.mult(self.body[i].m/m) + self.body[j].p.mult(self.body[j].m/m)
                        v0 = self.body[i].v.mult(self.body[i].m/m) + self.body[j].v.mult(self.body[j].m/m)
                        radius = (self.body[i].radius**3 + self.body[j].radius**3)**(1/3)
                        if self.body[i].m > self.body[j].m : 
                            illuRadius = self.body[i].illuRadius
                            color = self.body[i].color
                            self.body[i] = Body(name,p0,v0,m,radius,illuRadius,color)
                            self.removeBody(j)
                        else:
                            illuRadius = self.body[j].illuRadius
                            color = self.body[j].color
                            self.body[j] = Body(name,p0,v0,m,radius,illuRadius,color)
                            self.removeBody(i)
                        return self.collision()+1
        return 0
        

    def euler(self,stepMax: float):
        ''' 
        Resolve the N-Body problem until stepMax with the euler method
        stepMax: number of steps to perform
        '''

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
            self.collision()


    def f(self,p: list,v: list):
        F = []
        for i in range(self.N):
            force = Vector()
            for j in range(self.N):
                if j != i:
                    force += (self.body[j].p-p[i]).mult(G*self.body[i].m*self.body[j].m/(self.body[j].p-p[i]).norm()**3)
            F.append(force.mult(1/(self.body[i].m)))
        return (v,F)

    def RK4(self,stepMax: float):
        for step in range(stepMax):
            p = [self.body[i].p for i in range(self.N)]
            v = [self.body[i].v for i in range(self.N)]
            (vk1,ak1) = self.f(p,v)
            (vk2,ak2) = self.f([p[k] + vk1[k].mult(self.dt/2) for k in range(self.N)],[v[k] + ak1[k].mult(self.dt/2) for k in range(self.N)])
            (vk3,ak3) = self.f([p[k] + vk2[k].mult(self.dt/2) for k in range(self.N)],[v[k] + ak2[k].mult(self.dt/2) for k in range(self.N)])
            (vk4,ak4) = self.f([p[k] + vk3[k].mult(self.dt/2) for k in range(self.N)],[v[k] + ak3[k].mult(self.dt/2) for k in range(self.N)])
            for k in range(0,self.N,1):
                self.body[k].p = self.body[k].p + vk1[k].mult(self.dt/6) + vk2[k].mult(self.dt/3) + vk3[k].mult(self.dt/3) + vk4[k].mult(self.dt/6) 
                self.body[k].v = self.body[k].v + ak1[k].mult(self.dt/6) + ak2[k].mult(self.dt/3) + ak3[k].mult(self.dt/3) + ak4[k].mult(self.dt/6)
            self.t+=self.dt
            self.collision()


