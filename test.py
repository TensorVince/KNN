#!/usr/bin/env python3
# --------------------------------------------------------------------------------------------------------------------------------
# Author: TensorVince
# License: Peaceful Open Source Proxy License (POSPL)
# License Url: https://raw.githubusercontent.com/TensorVince/PeacefulOpenSourceLicense/master/POSPL.txt
# --------------------------------------------------------------------------------------------------------------------------------
# Description: class to calculate the N next neighbours of a point
# --------------------------------------------------------------------------------------------------------------------------------
from point import *
from dataset import *
from knn import *

# Test: Point
a = Point(2,4)
b = Point(3,9)
result = b - a
print(f"a - b = {result}")

# Test: Dataset
classes = ["dogs", "cats"]
dsTest = DataSet(0, "red")
dsTest.AddPoint(Point(2, 4))
dsTest.AddPoint(Point(3, 8))

dsTest2 = DataSet(1, "blue")
dsTest2.AddPoint(Point(2, 8))
dsTest2.AddPoint(Point(3, 27))

for dsClass, point in dsTest:
    print(f"Class: {dsClass}, Point: {point}")

for dsClass, point in dsTest2:
    print(f"Class: {dsClass}, Point: {point}")

# Test: Dataset Container
dsc = DataSetContainer()
dsc.AddDataSet(dsTest)
dsc.AddDataSet(dsTest2)

# Test: KNN
print("TEST:KNN")
knnCalc = KNN_Calculator(3)
testPoint = Point(1,1)
result = knnCalc.GetKNNs(testPoint, dsc)

print(result)
