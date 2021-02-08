#!/usr/bin/env python3
# ********************************************************************************************************************************
# Author: TensorVince
# License: Peaceful Open Source License (https://raw.githubusercontent.com/TensorVince/PeacefulOpenSourceLicense/main/LICENSE)
# --------------------------------------------------------------------------------------------------------------------------------
# Description: class to calculate the N next neighbours of a point
# ********************************************************************************************************************************
from point import *
from sampleClass import *

# Test: Point
a = Point(2,4)
b = Point(3,9)
result = b - a
print(result)


# Test: SampleClass
testClass = SampleClass("red")
testClass.AddPoint(a)
testClass.AddPoint(b)

for point in testClass:
    print(point)




