#!/usr/bin/env python3
# ********************************************************************************************************************************
# Author: TensorVince
# License: Peaceful Open Source License (https://raw.githubusercontent.com/TensorVince/PeacefulOpenSourceLicense/main/LICENSE)
# --------------------------------------------------------------------------------------------------------------------------------
# Description: returns the K next neighbors
# ********************************************************************************************************************************
from point import *
from dataset import *
from datasetContainer import *

class KNN_Calculator():

    def __init__(self, K = 5):
        self.K = K

    # Summary:
    # - Calculates all distances
    # - Sorts the distances ascending (shortest first)
    # - returns their respective indeces in the SampleClassContainer
    def GetKNNs(self, p : Point, dsc : DataSetContainer):
        distances = [] # contains pairs like [classId, distance]
        
        # Determine all distances
        #for i in range(len(dsc)):
        for classId, newPoint in dsc.Data():
            #currentDistance = p - dsc[i]
            currentDistance = p - newPoint
            distances.append([classId, currentDistance])

        # Sort distances ascending (next neighbours)
        distances.sort(key = lambda x : x[1])

        # extract indeces from next neighbours
        indeces = [indexDistancePair[0] for indexDistancePair in distances]

        # return only indeces of K next neighbours
        return indeces[:self.K]
