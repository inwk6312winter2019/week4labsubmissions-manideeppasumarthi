class Point():
	def __init__(self,a,b):
		self.a=a
		self.b=b

	def __add__(self,other):
		return (self.a+other.a,self.b+other.b)
	def add(self,other):
		if isinstance(other,tuple):
			return (self.a+other[0],self.b+other[1])
		else:
			return self+other
point1=Point(0.5,1.2)
point2=Point(1.2,1.8)
print('Points addition: ',point1.add(point2))
print('Tuple and Points Addtion: ',point1.add((2.5,4.8)))
