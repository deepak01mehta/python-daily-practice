class fraction:

    def __init__(self,x,y):
        self.num = x
        self.dum = y


    def __str__(self):
        return '{}/{}'.format(self.num,self.dum)

    def __add__(self, other):
        new_num =self.num*other.dum + other.num*self.dum
        new_dum = self.dum*other.dum


        return '{}/{}'.format(new_num,new_dum)

    def __sub__(self, other):
        new_num =self.num*other.dum - other.num*self.dum
        new_dum = self.dum*other.dum
        
        
        return '{}/{}'.format(new_num,new_dum)

    def __mul__(self, other):
        new_num =self.num*other.num
        new_dum = self.dum*other.dum

        return '{}/{}'.format(new_num,new_dum)


    def __truediv__(self, other):
        new_num = self.num*other.dum
        new_dum = self.dum*other.num

        return '{}/{}'.format(new_num,new_dum)

fr1 = fraction(10,4)
fr2 = fraction(7,3)

print(fr1+fr2)
print(fr1 - fr2)
print(fr1*fr2)
print(fr1 / fr2)

        
        