def gcd(a,b):
    while a % b != 0 :
         olda = a
         oldb = b
         a = oldb
         b = olda % oldb
    return b 
#print (gcd(4,14))
class Fraction:
    def __init__(self,top,bottom):
        self.num = top
        self.den = bottom
    def __str__(self):
        return str(self.num) + "/" + str(self.den)
    def __add__(self,other):
        newnum = self.num * other.den + self.den * other.num
        newden = self.den * other.den
        common = gcd(newnum,newden)
        return Fraction(newnum//common,newden//common) 
    def __sub__(self,other):
        newnum = self.num * other.den - self.den * other.num
        newden = self.den * other.den
        common = gcd(newnum,newden)
        return Fraction(newnum//common,newden//common)
    def __mul__(self,other):
        newnum = self.num * other.num
        newden = self.den * other.den
        common = gcd(newnum,newden)
        return Fraction(newnum//common,newden//common)
    def __truediv__(self,other):
        newnum = self.num * other.den
        newden = self.den * other.num
        common = gcd(newnum,newden)
        return Fraction(newnum//common,newden//common)
    def __eq__(self,other):
        firstnum = self.num * other.den
        secondnum = self.den * other.num
        return firstnum == secondnum 
    def __lt__(self,other):
        firstnum = self.num * other.den
        secondnum = self.den * other.num
        return firstnum < secondnum 
x = Fraction(3,2)
y = Fraction(3,4)
print("Sum of numbers is:",x+y)
print("Difference is:",x-y)
print("Multiplication of numbers is:",x*y)
print("Division of numbers is:",x/y)
print("x is equal to y:",x==y)
print("x is less than y:",x<y)
print("x is greater than y:",x>y)
