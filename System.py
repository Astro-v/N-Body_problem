import Body


'''
the system class manages all the N-body system and manages the simulation
'''
class System:
    def __init__(self,p0,v0,m,radius):
        '''
        p0,v0,m,radius : array that contain:
        p0 : initial position
        v0 : initial velocity
        m : mass
        radius : radius of the several body
        '''
        self.N = len(p0)
        for i in range(1,self.N):
            
