#!/usr/bin/env python3
# ********************************************************************************************************************************
# Author: TensorVince
# License: Peaceful Open Source License (https://raw.githubusercontent.com/TensorVince/PeacefulOpenSourceLicense/main/LICENSE)
# --------------------------------------------------------------------------------------------------------------------------------
# Description: Acts as single proxy for multiple datasets. Purpose is to make it easier to iterate over all datasets
# ********************************************************************************************************************************
class DataSetContainer:
    def __init__(self):
        self.datasets = []
        self.datasetRanges = []
        self.length = 0

    def AddDataSet(self, dataset):
        self.datasets.append(dataset)

        if len(self.datasetRanges) > 0:
            self.datasetRanges.append(range(self.length - 1, self.length + len(dataset) -1))
        else:
          self.datasetRanges.append(range(0, len(dataset) -1))

        self.length += len(dataset)

    def DetermineRightDatasetFromIndex(self, index):
        for i in range(len(self.datasetRanges)):
            print("Index in Range?", index, self.datasetRanges[i])
            if index in self.datasetRanges[i]:
              return i

    def DetermineLabelAndColorFromIndex(self, index):
        dataSetIndex = self.DetermineRightDatasetFromIndex(index)
        return self.datasets[dataSetIndex].label, self.datasets[dataSetIndex].color

    # Methods to iterate over all Points in all sampleClasses    
    def __len__(self):
        return self.length # alternatively: return sum(self.datasetLengths)

    def __getitem__(self, index):
        if len(self) > index:
            #return self.datasets[index]
            dataSetIndex = self.DetermineRightDatasetFromIndex(index)
            newIndex = index
            for i in range(0, len(self.datasetRanges)):
                if newIndex > len(self.datasetRanges[i]):
                  newIndex -= len(self.datasetRanges[i])
                else:
                  break

            try:
                 print(dataSetIndex, newIndex)
                 return self.datasets[dataSetIndex][newIndex]
            except:
                raise
        else:
            return None
