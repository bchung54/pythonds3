class Fraction:
    
    # Fraction class from PythonDS 1.13
    # Originally negative fractions are represented with a negative numerator
    # No changes needed for 1.17.6
    
    def __init__(self, top, bottom):
        
        #Integer check added due to Programming Exercises 1.17.5
        if isinstance(top, int) and isinstance(bottom, int):

            #Moved from __add__ function due to Programming Exercies 1.17.2
            common = gcd(top, bottom)
            
            self.num = top // common
            self.den = bottom // common
        else:
            raise ValueError("numerator and denominator must be integers")

    def show(self):
        print(self.num, "/", self.den)
    
    def __str__(self):
        return str(self.num) + "/" + str(self.den)
    
    def __add__(self, otherfraction):
        
        newnum = self.num * otherfraction.den + self.den * otherfraction.num
        newden = self.den * otherfraction.den
        return Fraction(newnum, newden)
        
        #Moved gcd to constructor due to Programming Exercisee 1.17.2
        #common = gcd(newnum, newden)
        #return Fraction(newnum // common, newden // common)
    
    def __eq__(self, other):
        
        firstnum = self.num * other.den
        secondnum = other.num * self.den
        return firstnum == secondnum

    #Programming Exercises 1.17.1
    def getNum(self):
        return self.num
    
    #Programming Exercises 1.17.1
    def getDen(self):
        return self.den

    #Programming Exercises 1.17.3
    def __sub__(self, otherfraction):
        
        newnum = self.num * otherfraction.den - self.den * otherfraction.num
        newden = self.den * otherfraction.den
        return Fraction(newnum, newden)
    
    #Programming Exercises 1.17.3
    def __mul__(self, otherfraction):

        newnum = self.num * otherfraction.num
        newden = self.den * otherfraction.den
        return Fraction(newnum, newden)
    
    #Programming Exercises 1.17.3
    def __truediv__(self, otherfraction):

        newnum = self.num * otherfraction.den
        newden = self.den * otherfraction.num
        return Fraction(newnum, newden)
    
    #Programming Exercises 1.17.4
    def __gt__(self, otherfraction):
        
        selfnum = self.num * otherfraction.den
        othernum = self.den * otherfraction.num
        return selfnum > othernum
    
    #Programming Exercises 1.17.4
    def __ge__(self, otherfraction):
        return self.__gt__(otherfraction) or self.__eq__(otherfraction)

    #Programming Exercises 1.17.4
    def __lt__(self, otherfraction):
        
        selfnum = self.num * otherfraction.den
        othernum = self.den * otherfraction.num
        return selfnum < othernum
    
    #Programming Exercises 1.17.4
    def __le__(self, otherfraction):
        return self.__lt__(otherfraction) or self.__eq__(otherfraction)
    
    #Programming Exercises 1.17.4
    def __ne__(self, otherfraction):
        return not self.__eq__(otherfraction)

    #Programming Exercises 1.17.7
    #__radd__ allows addition to commutative with numbers that are not fractions
    #the function defined here works with other integers
    def __radd__(self, other):
        return self.__add__(Fraction(other, 1))

    #Programming Exercises 1.17.8
    #__iadd__ is addition assignment or '+='
    def __iadd__(self, other):
        
        if isinstance(other, int):
            other = Fraction(other, 1)
        self = self.__add__(other)
        return self
    
    #Programming Exercises 1.17.9
    #__repr__ provides a printable representation of the object itself
    def __repr__(self):
        return "Fraction({}, {})".format(self.num, self.den)

def gcd(m, n):
    while m % n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm % oldn
    return n


x = Fraction(1,-2)
y = Fraction(2,3)
print(x+y)
print(x == y)
print(x / y)
print(x * y)

