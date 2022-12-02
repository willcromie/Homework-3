Python 3.10.8 (tags/v3.10.8:aaaf517, Oct 11 2022, 16:50:30) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
from graphics import*
def isBetween(x, end1, end2):
    return end1 <= x <= end2 or end2 <= x <= end1

def isInside(point, rect):
    pt1 = rect.getP1()
    pt2 = rect.getP2()
    return isBetween(point.getX(), pt1.getX(), pt2.getX()) and isBetween(point.getY(), pt1.getY(), pt2.getY())

def makeColoredRect(corner, width, height, color, win):
    corner2 = corner.clone()
    corner2.move(width, -height)
    rect = Rectangle(corner, corner2)
    rect.setFill(color)
    rect.draw(win)
    return rect

def getChoice(choicePairs, default, win):
    point = win.getMouse()
    for (rectangle, choice) in choicePairs:
...         if isInside(point, rectangle):
...             return choice
...     return default
... 
>>> def main():
...     win = GraphWin('pick Colors', 400, 400)
...     win.yUp()
...     choicePairs = list()
...     buttonSetup = [(310, 350, 'red'), (310, 310, 'yellow'), (310, 270, 'blue'), (310, 320, 'purple')]
...     for (x, y, color) in buttonSetup:
...         button = makeColoredRect(Point(x, y), 80, 30, color, win)
...         choicePairs.append((button, color))
...         house = makeColoredRect(Point(60, 200), 180, 150, 'grey', win)
...         door = makeColoredRect(Point(90, 150), 40, 100, 'white', win)
...         roof = Polygon(Point(50, 200), Point(250, 200), Point(150, 300))
...         chimne = makeColoredRect(Point(90, 335), 40, 60, 'red', win)
...         line = makeColoredRect(Point(105, 360), 5, 25, 'black', win)
...         roof.draw(win)
...     shapePairs = [(house, 'house'), (door, 'door'), (roof, 'roof'), (chiimne, 'chimne')]
...     msg = Text(Point(win.getWidth()/2, 375), '')
...     msg.draw(win)
...     for (shape, description) in shapePairs:
...         propmt = 'Click to choose a ' + description + ' color.'
...         msg.setText(prompt)
...         color = getChoice(choicePairs, 'white', win)
...         shape.setFill(color)
...     win.promptClose(msg)
... 
...     
>>> main()
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    main()
  File "<pyshell#10>", line 15, in main
    shapePairs = [(house, 'house'), (door, 'door'), (roof, 'roof'), (chiimne, 'chimne')]
NameError: name 'chiimne' is not defined. Did you mean: 'chimne'?
