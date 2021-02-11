class DataSet:
   
    def __init__(self, classid, color):
        self.classid = classid
        self.color = color
        self.dataPoints = []

    def AddPoint(self, p):
        self.dataPoints.append(p)

    def AddData(self, dataPoints):
        self.dataPoints += dataPoints # merge data arrays

    def GetClassPointMapping(self):
        return [[self.classid, point] for point in self.dataPoints]

    # Methods to iterate over all points
    def __iter__(self):
        return self.GetClassPointMapping().__iter__()

    def __len__(self):
        return self.dataPoints.__len__()

    def __getitem__(self, index):
        return self.dataPoints[index]


