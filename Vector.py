class Vector:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
        
    def __str__(self):
        return "("+str(self.x)+","+str(self.y)+","+str(self.z)+")"
        
    def norm(self):
        return (self.x**2 + self.y**2 + self.z**2)**(1/2)
    
    def scalarProduct(self,v):
        return self.x*v.x + self.y*v.y + self.z*v.z
    
    def crossProduct(self,v):
        w = Vector(0,0,0)
        w.x = self.y*v.z - self.z*v.y
        w.y = self.z*v.x - self.x*v.z
        w.z = self.x*v.y - self.y*v.x
        return w

