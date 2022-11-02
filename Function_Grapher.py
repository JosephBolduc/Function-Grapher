#Constructs a graphical representation of a function inside of a 2D list and prints it
def plot(func):
    table = list(10)
    for i in range(10):
        for j in range(10):
            if isPoint(func, i, j):

    return 0


#Determines if a point (x,y) lies on the function "func"
def isPoint(func, x, y):
    if y == func(x):
        return True
    return False



def functionOfX(x):
    return 2 * x


plot(functionOfX)