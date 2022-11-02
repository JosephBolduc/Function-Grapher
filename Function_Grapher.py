import numbers
from Graph import Graph
import math

#Constructs a graphical representation of a function inside of a 2D list and prints it
def plot(func, length, width):
    plots = Graph(width, length)
    for i in range(length):
        for j in range(width):
            if isPoint(func, i, j):
                plots.plotPoint(i,j, i)

            dYdXAtAPoint= dYdXEstimator(func, j) * 5
            if (dYdXAtAPoint -.4) <= i <= (dYdXAtAPoint + .4):
                plots.plotPoint(j, dYdXAtAPoint, "D")
            print("dY/dY @", j, " is ", dYdXEstimator(func,j))
    plots.print()


#Determines if a point (x,y) lies on the function "func"
def isPoint(func, x, y):
    res = func(x)
    if (res-.4) <= y <= (res+.4):
        return True
    return False

#Determined the derivitive at a x
def dYdXEstimator(func, x):
    sum = func(x+.001) - func(x)
    return sum / .001


def functionOfX(x):
    numerator = 25
    denominator = 1 + math.pow(2.75, .1 *(-x+50))
    return numerator / denominator


plot(functionOfX, 100, 100)