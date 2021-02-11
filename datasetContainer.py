#!/usr/bin/env python3
class DataSetContainer:
    def __init__(self):
        self.datasets = []
        self.colorMappingDict = {}

    def AddDataSet(self, dataset):
        self.datasets.append(dataset)
        self.colorMappingDict[dataset.classid] = dataset.color

    def Data(self):
        retArr = []

        for dataset in self.datasets:
            retArr += dataset.GetClassPointMapping()

        return retArr

    def __len__(self):
        retLen = 0
        for dataset in self.datasets:
            retLen += len(dataset)

        return retLen
