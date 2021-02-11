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
classes = ["dogs", "cats"]
dsTest = DataSet(0, "red")
dsTest.AddPoint(Point(2, 4))
dsTest.AddPoint(Point(3, 8))

for point in dsTest:
    print(point)

# Test: Dataset Container
dsTest2 = DataSet(1, "blue")
dsTest2.AddPoint(Point(2, 8))
dsTest2.AddPoint(Point(3, 27))

dsc = DataSetContainer()
dsc.AddDataSet(dsTest)
dsc.AddDataSet(dsTest2)


# Test: KNN
print("TEST:KNN")
knnCalc = KNN_Calculator(3)
testPoint = Point(1,1)
result = knnCalc.GetKNNs(testPoint, dsc)

print(result)
