import Vector

class Body:
    def __init__(self,p0,v0,m,radius):
        self.p = [p0]
        self.v = v0
        self.m = m
        self.radius = radius
        
    def __str__(self):
        return "Its current position is "+print(self.p[-1])+" (en pc).\n""Its current speed is "+print(self.v)+" (en km.s-1).\n""Its mass is "+self.m+" kg.\n""Its radius is "+self.radius+" km."
