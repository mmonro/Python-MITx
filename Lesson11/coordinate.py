class Coordinate(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def getX(self):
        # Getter method for a Coordinate object's x coordinate.
        # Getter methods are better practice than just accessing an attribute directly
        return self.x

    def getY(self):
        # Getter method for a Coordinate object's y coordinate
        return self.y

    def __str__(self):
        return '<' + str(self.getX()) + ',' + str(self.getY()) + '>'
        
    def __eq__(self, other):
        # check to see if 'other' is same type
        assert type(other) == type(self)
        if self.getX() == other.getX():
            if self.getY() == other.getY():
                return True
        return False


    def __repr__(self):
        return 'Coordinate(' + str(self.getX()) + ', ' + str(self.getY()) + ')'


c1=Coordinate(1,-8)
c2=Coordinate(-1,8)

print c1
print c2
print c1 == c2

print c1.__repr__
