import Vector as Vec

class Body:
    def __init__(self,p0,v0,m,radius):
        self.p = [p0]
        self.v = v0
        self.m = m
        self.radius = radius
        
    def __str__(self):
        return "Its current position is "+self.p[-1].__str__()+" (en km).\n""Its current speed is "+self.v.__str__()+" (en km.s-1).\n""Its mass is "+str(self.m)+" kg.\n""Its radius is "+str(self.radius)+" km."
