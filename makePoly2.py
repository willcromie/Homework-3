Python 3.10.8 (tags/v3.10.8:aaaf517, Oct 11 2022, 16:50:30) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
from graphics import*
def isBetween(x, end1, end2):
    return end1 <= x <= end2 or end2 <= x <= end1
... 
>>> def isInside(point, rect):
...     pt1 = rect.getP1()
...     pt2 = rect.getP2()
...     return isBetween(point.getX(), pt1.getX(), pt2.getX()) and \
...            isBetween(point.getY(), pt1.getY(), pt2.getY())
... 
>>> def polyHere(rect, win):
...     rect.setOutline("red")
...     rect.draw(win)
...     vertices = list()
...     pt = win.getMouse()
...     poly = None
...     while isInside(pt, rect):
...         if poly is not None:
...             poly.undraw()
...         vertices.append(pt)
...         poly = Polygon(vertices)
...         poly.draw(win)
...         pt = win.getMouse()
...     return poly
... 
>>> def main():
...     win = GraphWin('Drawing Polygons', 400, 400)
...     win.yUp()
... 
...     instructions = Text(Point(win.getWidth() / 2, 30),
...                         "Click vertices inside the red rectangle." +
...                         "\nClick outside the rectangle to stop.")
...     instructions.draw(win)
...     rect1 = Rectangle(Point(5, 55), Point(200, 120))
...     poly1 = polyHere(rect1, win)
...     poly1.setFill('green')
...     rect2 = Rectangle(Point(210, 50), Point(350, 350))
...     poly2 = polyHere(rect2, win)
...     poly2.setOutline('orange')
...     win.promptClose(instructions)
... 
...     
