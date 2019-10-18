import math

class PhisicsError(Exception):
    def __init__(self, text):
        self.txt = text

class SizeError(Exception):
    def __init__(self, text):
        self.txt = text

class Measure:
    def __init__(self, num=1, kg=0, m=0, s=0):
        try:
            if type(num) == int or type(num) == float:
                self.data = (num, kg, m, s)
            elif type(num) == Measure:
                self.data = num.data
            else:
                raise PhisicsError('\'' + num + '\' can\'t be physics measure')
        except PhisicsError as phys_err:
            print(phys_err)

    def get_value(self):
        return self.data[1:]

    def get_num(self):
        return self.data[0]

    def __cmp__(self, other): 
        other = Measure(other)
        try:
            if self.get_value() == other.get_value():
                return self.get_num() - other.get_num()
            else:
                raise SizeError('Sum of different sizes')
        except SizeError as size_error:
            print(size_error)

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
        return  Measure(num=math.round(self.data[0], n), kg=self.data[1], 
                                    m=self.data[2], s=self.data[3])
    def __add__(self, other):
        other = Measure(other)
        try:
            if self.data[1:] == other.data[1:]:
                return Measure(num=self.data[0] + other.data[0], kg=self.data[1],
                                m=self.data[2], s=self.data[3])
            else:
                raise SizeError('Sum of different sizes numbers')
        except SizeError as size_error:
            print(size_error)
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
        try: 
        return Measure(num=self.data[0] % other.data[0], 
                        kg=self.data[1] - other.data[1],
                        m=self.data[2] - other.data[2], 
                        s=self.data[3] - other.data[3])
    def __pow__(self, other):
        return Measure(num=self.data[0] ** other, 
                        kg=self.data[1] * other,
                        m=self.data[2] * other 
                        s=self.data[3] * other)
    def __radd__(self, other): pass
    def __rsub__(self, other): pass
    def __rmul__(self, other): pass
    def __rfloordiv__(self, other): pass
    def __rdiv__(self, other): pass
    def __rmod__(self, other): pass
    def __rpow__(self, other): pass
    def __iadd__(self, other): pass
    def __isub__(self, other): pass
    def __imul__(self, other): pass
    def __ifloordiv__(self, other): pass
    def __idiv__(self, other): pass
    def __imod__(self, other): pass
    def __ipow__(self, other): pass
    def __int__(self): pass
    def __float__(self):pass
    def __str__(self):pass
    def __repr__(self):pass
    def __nonzero__(self):pass
    def __iter__(self):pass

Measure(com)