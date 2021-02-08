#!/usr/bin/env python3
# ********************************************************************************************************************************
# Author: TensorVince
# License: Peaceful Open Source License (https://raw.githubusercontent.com/TensorVince/PeacefulOpenSourceLicense/main/LICENSE)
# --------------------------------------------------------------------------------------------------------------------------------
# Description: class to store a 2D-Point (x,y)
# ********************************************************************************************************************************
from math import sqrt

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # The subtraction operator will be used to determine the distance between two points.
    # We collect multiple distances to sort them later (to determine the KNNs). 
    # Since negative numbers would falsify the sorting results, the negative sign shall be removed.
    # This happens automatically by using the "squareroot"-function.
    # 
    # Formula to calculate the distance:
    # AB^2 = (xB - xA)^2 + (yB - yA)^2
    # AB = SQRT(AB^2)
    #
    # Source:
    # Pythagoras (https://en.wikipedia.org/wiki/Pythagoras)
    def __sub__(p1, p2): # p1 = self
        xSquared = (p2.x - p1.x)**2
        ySquared = (p2.y - p1.y)**2
        distance = sqrt(xSquared + ySquared)

        return distance
