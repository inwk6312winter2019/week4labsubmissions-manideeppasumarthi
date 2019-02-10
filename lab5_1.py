import math
class point():
  def __init__(self,x=0.0,y=0.0):
    self.x=x
    self.y=y

  def distance_between_points(self,p):
    x1 = math.pow(self.x-p.x,2)
    y1 = math.pow(self.y-p.y,2)
    return (math.sqrt(x1+y1))

point1 = point(3,8)
point2 = point(10,3)
print(point1.distance_between_points(point2))
