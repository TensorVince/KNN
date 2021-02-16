from sklearn import datasets
from os import linesep

iris = datasets.load_iris()
classes = iris.target
coordinates = iris.data[:, :2] # take only 2 dimension out of 4
csvSeperator = ';'


with open('irisDataSet_2D.csv', 'w') as outputCsv:
    for irisClass, irisCoordinate in zip(classes, coordinates):
        csvFields = [str(irisClass), str(irisCoordinate[0]), str(irisCoordinate[1])]
        csvLine = csvSeperator.join(csvFields)
        outputCsv.write(csvLine)
        outputCsv.write(linesep)
        
