#!/usr/bin/env python3
# ********************************************************************************************************************************
# Author: TensorVince
# License: Peaceful Open Source License (https://raw.githubusercontent.com/TensorVince/PeacefulOpenSourceLicense/main/LICENSE)
# --------------------------------------------------------------------------------------------------------------------------------
# Description: class to calculate the N next neighbours of a point
# ********************************************************************************************************************************
from point import *
from dataset import *
from knn import *

# Test: Point
a = Point(2,4)
b = Point(3,9)
result = b - a
print(result)

# Test: Dataset
dsTest = DataSet("dogs", "red")
dsTest.AddPoint(a)
dsTest.AddPoint(b)

for point in dsTest:
    print(point)

# Test: Dataset Container
dsTest2 = DataSet("cats", "blue")
dsTest2.AddPoint(Point(2, 8))
dsTest2.AddPoint(Point(3, 27))

dsc = DataSetContainer()
dsc.AddDataSet(dsTest)
dsc.AddDataSet(dsTest2)


# Test: KNN
knnCalc = KNN_Calculator(3)
testPoint = Point(0,0)
knnCalc.GetKNNs(testPoint, dsc)
