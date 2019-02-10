import math
class Rectangle(point):
  def __init__(self,width=0.0,height=0.0,corner=point(0.0,0.0)):
    self.width=width
    self.height=height
    self.corner=corner

def find_center(Rectangle):
  x1 = (Rectangle.width)/2
  x2  = (Rectangle.height)/2
  return (x1,x2)

p = point()
rect=Rectangle(10,20,p)
centre= find_center(rect)
print(centre)

#Task2-b
def move_rectangle(Rectangle,dx,dy):
  Rectangle.corner.x=Rectangle.corner.x + dx
  Rectangle.corner.y = Rectangle.corner.y + dy

  return (Rectangle.corner.x,Rectangle.corner.y)
cor = point(4,5)
dx = 2
dy = 4
mv_ract = Rectangle(corner = cor)
moved_corner = move_rectangle(mv_ract,dx,dy)
print(moved_corner)
