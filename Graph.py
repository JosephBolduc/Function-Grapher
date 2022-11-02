class Graph(object):
    def __init__(self, cols, rows):
        self.cols = cols
        self.rows = rows
        self.plot = [[" " for i in range(rows)] for j in range(cols)]

    def plotPoint(self, x, y, txt):
        self.plot[int(y)][int(x)] = str(txt)[0]

    def print(self):
        for x in range(self.rows):
            for y in range(self.cols):
                print(self.plot[self.cols-1-x][y-1], end="")
            print("")





