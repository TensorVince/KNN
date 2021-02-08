#!/usr/bin/env python3
# ********************************************************************************************************************************
# Author: TensorVince
# License: Peaceful Open Source License (https://raw.githubusercontent.com/TensorVince/PeacefulOpenSourceLicense/main/LICENSE)
# --------------------------------------------------------------------------------------------------------------------------------
# Description: class to map samples
# ********************************************************************************************************************************
from point import *

class SampleClass:
    def __init__(self, color, pointArr = []):
        self.color = color
        self.pointArr = pointArr

    def AddPoint(self, p):
        self.pointArr.append(p)

    # Methods to iterate over all Points
    def __iter__(self):
        return self.pointArr.__iter__()
