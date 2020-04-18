from Body import *


'''
the system class manages all the N-body system and manages the simulation
'''
class System:
    def __init__(self,p0,v0,m,radius,dt):
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
            self.body.append(Bd.Body(p0[i],v0[i],m[i],radius[i]))
           
        
    def addBody(self,p0,v0,m,radius):
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
       
     
     
