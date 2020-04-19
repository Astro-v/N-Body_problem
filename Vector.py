class Vector:
    def __init__(self,x=0,y=0,z=0):
        self.x = x
        self.y = y
        self.z = z
        
    # Methods
    
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
    
    def mult(self,x):
        return Vector(self.x*x,self.y*x,self.z*x)
    
    # Operator overloading

    def __str__(self): # Allow to do "print(v)"
        return "("+str(self.x)+","+str(self.y)+","+str(self.z)+")"

    def __add__(self,other): # Allow to do "w=v+u"
        if not other.__class__ is Vector:
            print("Error: argument not a Vector")
            return NotImplemented
        return Vector(self.x+other.x,self.y+other.y,self.z+other.z)

    def __iadd__(self,other): # Allow to do "v+=u"
        if not other.__class__ is Vector:
            print("Error: argument not a Vector")
            return NotImplemented
        return self+other

    def __sub__(self,other): # Allow to do "w=v-u"
        if not other.__class__ is Vector:
            print("Error: argument not a Vector")
            return NotImplemented
        return Vector(self.x-other.x,self.y-other.y,self.z-other.z)

    def __isub__(self,other):
        if not other.__class__ is Vector: # Allow to do "v-=u"
            print("Error: argument not a Vector")
            return NotImplemented
        return self-other

    def __mul__(self,other): # Other way to make scalar product
        if not other.__class__ is Vector:
            print("Error: argument not a Vector")
            return NotImplemented
        return self.scalarProduct(other)

    def __neg__(self): # Allow to do "-v"
        return Vector()-self
    
    def __pos__(self): # Allow to do "+v"
        return self

    def __abs__(self): # Allow to do "abs(v)"
        return Vector(abs(self.x),abs(self.y),abs(self.z))

    def __eq__(self,other): # Allow to do "v==u"
        if not other.__class__ is Vector:
            print("Error: argument not a Vector")
            return NotImplemented
        if (self.x==other.x and self.y==other.y and self.z==other.z):
            return True
        return False

    def __ne__(self,other): # Allow to do "v!=u"
        if not other.__class__ is Vector:
            print("Error: argument not a Vector")
            return NotImplemented
        if (self.x!=other.x or self.y!=other.y or self.z!=other.z):
            return True
        return False

    def __lt__(self,other): # Allow to do "v<u"
        """
        Return True if and only if norm of v is lower than norm of u.
        """
        if not other.__class__ is Vector:
            print("Error: argument not a Vector")
            return NotImplemented
        if (self.norm()<other.norm()):
            return True
        return False

    def __le__(self,other): # Allow to do "v<=u"
        """
        Return True if and only if norm of v is lower than or equal to norm of u.
        """
        if not other.__class__ is Vector:
            print("Error: argument not a Vector")
            return NotImplemented
        if (self.norm()<=other.norm()):
            return True
        return False

    def __lt__(self,other): # Allow to do "v>u"
        """
        Return True if and only if norm of v is greater than norm of u.
        """
        if not other.__class__ is Vector:
            print("Error: argument not a Vector")
            return NotImplemented
        if (self.norm()>other.norm()):
            return True
        return False

    def __le__(self,other): # Allow to do "v>=u"
        """
        Return True if and only if norm of v is greater than or equal to norm of u.
        """
        if not other.__class__ is Vector:
            print("Error: argument not a Vector")
            return NotImplemented
        if (self.norm()>=other.norm()):
            return True
        return False

    def __len__(self): # Allow to do "len(v)" (not realy usefull)
        return 3

