import matplotlib.pyplot as plt

class Plot:
    def __init__(self):
        pass

def AddScatterPlot(xArr, yArr, color):
    plt.scatter(xArr, yArr, color)

def FinalizePlot():
    plt.show()
