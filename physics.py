'''(c) Roman Gundarin (NamorNiradnug)

This is library for working with physics measures.'''

import math

def isfloat(string):
    if string.count('.') == 1:
        if (string[:string.find('.')] + string[string.find('.') + 1:]).isnumeric():
            return True
        else:
            return False
    elif string.isnumeric():
        return True
    return False

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
            if len(args) != 0 and type(args[0]) == Measure:
                if len(args) + len(kwargs) == 1:
                    self.data = args[0].data
                    self.value = args[0].value
            elif len(args) != 0 and type(args[0]) == str:
                if len(args) + len(kwargs) == 1:
                    string = args[0].split()
                    if isfloat(string[0]):
                        num = float(string[0])
                    else:
                        num = 1
                    kg = m = s = 0
                    for i in range(1, len(string)):
                        string[i] = string[i].split()
                        if len(string[i]) == 2:
                            if isfloat(string[i][1]):
                                if string[i][0] == 'kg':
                                    kg += float(string[i][1])
                                elif string[i][0] == 'm':
                                    m += float(string[i][1])
                                elif string[i][0] == 's':
                                    s += float(string[i][1])
                                else:
                                    raise AttributeError('Indefinite argument ' + string[i][0])
                            else:
                                raise AttributeError('Degree of value must be int or float, not ' + str(type(string[i][1])))
                        elif len(string[i]) == 1:
                            if string[i][0] == 'kg':
                                kg += 1
                            elif string[i][0] == 'm':
                                m += 1
                            elif string[i][0] == 's':
                                s += 1
                            else:
                                raise AttributeError('Indefinite argument ' + string[i][0])
                        else:
                            raise AttributeError("inadmissible argument " + string[i])
                    self.data = [num, kg, m, s]
                else:
                    raise AttributeError('Too many arguments')
            else:
                if len(args) != 0:
                    if 'num' in kwargs.keys():
                        raise AttributeError('Double definition of num')
                    else:
                        num = args[0]
                else:
                    if 'num' in kwargs.keys():
                        num = kwargs['num']
                    else:
                        num = 1
                if len(args) > 1:
                    if 'kg' in kwargs.keys():
                        raise AttributeError('Double definition of kg')
                    else:
                        kg = args[1]
                else:
                    if 'kg' in kwargs.keys():
                        kg = kwargs['kg']
                    else:
                        kg = 0
                if len(args) > 2:
                    if 'm' in kwargs.keys():
                        raise AttributeError('Double definition of m')
                    else:
                        m = args[2]
                else:
                    if 'm' in kwargs.keys():
                        m = kwargs['m']
                    else:
                        m = 0
                if len(args) > 3:
                    if 's' in kwargs.keys():
                        raise AttributeError('Double definition of s')
                    else:
                        s = args[3]
                else:
                    if 's' in kwargs.keys():
                        s = kwargs['s']
                    else:
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
        output = ''
        output += str(float(self) / (10 ** (len(str(int(self))) - 1)) + ' * 10^' + str(len(str(int(self))) - 1) + ' '
        if self.data[1] != 0:
            output += 'kg^' + str(self.data[1]) + ' '
        if self.data[2] != 0:
            output += 'm^' + str(self.data[2]) + ' '
        if self.data[3] != 0:
            output += 's^' + str(self.data[3])
        return output
    
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

print(Measure(1, 2, m=2, s=3))