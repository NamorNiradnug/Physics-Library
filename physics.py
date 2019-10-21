'''(c) Roman Gundarin (NamorNiradnug)

This is library for working with physics measures.'''

import math

class PhysicsError(Exception):
    def __init__(self, text):
        self.txt = text
        print(self)

class DimensionError(Exception):
    def __init__(self, text):
        self.txt = text
        print(self)

class Measure:

    '''Measure object is number with three dimensions: 
    mass in kilograms, length in meters, time in seconds.'''

    def __init__(self, *args, **kwargs):
        if len(args) + len(kwargs) <= 4:
            # TODO str var
            if type(args[0]) == str:
                if len(args) + len(kwargs) == 1:
                    pass
                else:
                    raise AttributeError('To many arguments')
            else:
                try:
                    num = kwargs['num']
                except KeyError:
                    num = args[0]
                except IndexError:
                    num = 1
                try:
                    kg = kwargs['kg']
                except KeyError:
                    kg = args[1]
                except IndexError:
                    kg = 0
                try:
                    m = kwargs['m']
                except KeyError:
                    m = args[2]
                except IndexError:
                    m = 0
                try:
                    s = kwargs['s']
                except KeyError:
                    s = args[3]
                except IndexError:
                    s = 0
                if sum([(type(i) == int or type(i) == float) for i in [num, kg, m, s]]) == 4:
                    self.data = [num, kg, m, s]
                    self.value = 'basic'
                else:
                    raise PhysicsError('Arguments of physics measure must be float or int')
        else:
            raise AttributeError('Too many arguments')
            

    def get_basic_value(self):
        return self.data[1:]

    def get_num(self):
        return self.data[0]

    def __cmp__(self, other): 
        other = Measure(other)
        if self.get_basic_value() == other.get_basic_value():
            return self.get_num() - other.get_num()
        raise DimensionError('Sum of different dimension')

    def __neg__(self): 
        return Measure(num=-self.data[0], kg=self.data[1],  
                            m=self.data[2], s=self.data[3])

    def __abs__(self):
        return abs(self.data[0])

    def __floor__(self):
        return Measure(num=math.floor(self.data[0]), kg=self.data[1], 
                                    m=self.data[2], s=self.data[3])

    def __ceil__(self):
        return  Measure(num=math.ceil(self.data[0]), kg=self.data[1], 
                                    m=self.data[2], s=self.data[3])
                                    
    def __round__(self, n):
        return  Measure(num=round(self.data[0], n), kg=self.data[1], 
                                    m=self.data[2], s=self.data[3])

    def __add__(self, other):
        other = Measure(other)
        if self.get_basic_value() == other.get_basic_value():
            return Measure(num=self.data[0] + other.data[0], kg=self.data[1],
                            m=self.data[2], s=self.data[3])
        raise DimensionError('Sum of different dimension numbers')

    def __sub__(self, other):
        return self + (-other)

    def __mul__(self, other):
        other = Measure(other)
        return Measure(num=self.data[0] * other.data[0], 
                        kg=self.data[1] + other.data[1],
                        m=self.data[2] + other.data[2], 
                        s=self.data[3] + other.data[3])

    def __floordiv__(self, other):
        other = Measure(other)
        return Measure(num=self.data[0] // other.data[0], 
                        kg=self.data[1] - other.data[1],
                        m=self.data[2] - other.data[2], 
                        s=self.data[3] - other.data[3])

    def __div__(self, other):
        other = Measure(other)
        return Measure(num=self.data[0] / other.data[0], 
                        kg=self.data[1] - other.data[1],
                        m=self.data[2] - other.data[2], 
                        s=self.data[3] - other.data[3])

    def __mod__(self, other):
        other = Measure(other)
        if other.get_basic_value() == self.get_basic_value():
            return Measure(num=self.data[0] % other.data[0], kg=self.data[1],
                            m=self.data[2], s=self.data[3])
        raise DimensionError('Mod of different dimension physics measures')

    def __pow__(self, other):
        return Measure(num=self.data[0] ** other, 
                        kg=self.data[1] * other,
                        m=self.data[2] * other,
                        s=self.data[3] * other)

    def __radd__(self, other):
        return self + other

    def __rsub__(self, other):
        return other + (-self)

    def __rmul__(self, other):
        return self * other

    def __rfloordiv__(self, other):
        return Measure(other) // self

    def __rdiv__(self, other):
        return Measure(other) / self

    def __rmod__(self, other):
        return Measure(other) % self
    
    def __rpow__(self, other):
        raise DimensionError('Exsponentiation of physics measure')
    
    def __iadd__(self, other):
        self.data = (self + other).data
    
    def __isub__(self, other):
        self.data = (self - other).data
    
    def __imul__(self, other):
        self.data = (self * other).data
    
    def __ifloordiv__(self, other):
        self.data = (self // other).data
    
    def __idiv__(self, other):
        self.data = (self / other).data
    
    def __imod__(self, other):
        self.data = (self % other).data
    
    def __ipow__(self, other):
        self.data = (self ** other).data
    
    def __int__(self):
        return int(self.data[0])
    
    def __float__(self):
        return float(self.data[0])
    
    def __str__(self):
        return (str(float(self) / (len(int(self)) ** 10)) +
                ' * ' + str(len(int(self)) ** 10) +
                ' kg^' + str(self.data[1]) +
                ' m^' + str(self.data[2]) +
                ' s^' + str(self.data[3]))
    
    def __repr__(self):
        return ('Measure(num=' + str(float(self)) +
                ', kg=' + str(self.data[1]) +
                ', m=' + str(self.data[2]) +
                ', s=' + str(self.data[3]) + ')')
    
    def __nonzero__(self):
        if float(self):
            return True
        return False
    
    def __iter__(self):
        for obj in self.data:
            yield obj

print(Measure(1, 2, m=2, s=3)