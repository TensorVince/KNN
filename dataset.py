#!/usr/bin/env python3
# ********************************************************************************************************************************
# Author: TensorVince
# License: Peaceful Open Source License (https://raw.githubusercontent.com/TensorVince/PeacefulOpenSourceLicense/main/LICENSE)
# --------------------------------------------------------------------------------------------------------------------------------
# Description: class to map samples / datasets
# ********************************************************************************************************************************
from point import *

class DataSet:
    def __init__(self, label, color, pointArr = []):
        self.label = label # should be unique (e.g. cats, dogs, ...)
        self.color = color
        self.pointArr = pointArr

    def AddPoint(self, p):
        self.pointArr.append(p)

    # Methods to iterate over all Points
    def __iter__(self):
        return self.pointArr.__iter__()

    def __len__(self):
        return len(self.pointArr)

    def __getitem__(self, index):
        try:
          return self.pointArr[index]
        except:
            print("Fehler: IndexOutOfRange im PointArr")
            print(f"Index: {index}")
            raise
