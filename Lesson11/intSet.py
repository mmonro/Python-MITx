class intSet(object):
    """An intSet is a set of integers
    The value is represented by a list of ints, self.vals.
    Each int in the set occurs in self.vals exactly once."""

    def __init__(self):
        """Create an empty set of integers"""
        self.vals = []

    def insert(self, e):
        """Assumes e is an integer and inserts e into self""" 
        if not e in self.vals:
            self.vals.append(e)

    def member(self, e):
        """Assumes e is an integer
           Returns True if e is in self, and False otherwise"""
        return e in self.vals

    def remove(self, e):
        """Assumes e is an integer and removes e from self
           Raises ValueError if e is not in self"""
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + ' not found')

    def __str__(self):
        """Returns a string representation of self"""
        self.vals.sort()
        return '{' + ','.join([str(e) for e in self.vals]) + '}'

    def intersect(self, other):
        commonVals = intSet()

        for x in self.vals:
            if other.member(x):
                commonVals.insert(x)
        return commonVals

    def __len__(self):
        return len(self.vals)
       
        
        
x = intSet()
x.insert(1)
x.insert(10)
x.insert(12)
x.insert(17)
x.insert(18)

y = intSet()
y.insert(1)
y.insert(2)
y.insert(4)

z = x.intersect(y)
print z 

z.insert(5)
print z  

print x.__len__()
