class point():
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def __str__(self):
        return "Points is: ({},{})".format(self.a,self.b)
    def add(self,other):
        print("Addition is: ({} , {})".format(self.a+other.a, self.b+other.b))


p1 = point(1.2,2.3)
p2= point(0.6,0.8)
p1.add(p2)
print(p1)
print(p2)
