import random


class DatasetContainerDict(dict):
    def __init__(self):
        pass

    def LoadDataFromArray(inputData):
        pass

    def LoadDataSetsFromCsv(csvPath, colSeperator = ';', classifierColumnIndex = 0, *coordinateColumnIndeces):

        with open(csvPath, 'r') as fHandleCsv:
            csvLine = f.readline()

            while csvLine:
                csvLineSplit = csvLine.split(colSeperator)
                classifier = csvLineSplit[classifierColumn]
                
                if classifier not in self:
                    self[classifier] = []

                currentCoordinateArr = []

                for coordinateColumnIndex in coordinateColumnIndeces:
                    currentCoordinateArr.append(csvLineSplit[coordinateColumnIndex])
                self[classifier].append(currentCoordinateArr)

    # percentTestData    = What percentage of the trainingdataset should be used as test data?
    # randomizeDataOrder = Should the test data be random or always the same?
    # -------------------------------------------------------------------------------------
    # Returns 2 DatasetContainers 
    # [0] = training data
    # [1] = test data
    def CreateDatasetContainersForSupervisedLearning(percentTestData = 33, randomizeDataOrder = False):
        allData = []
        for className in self:
            allData.append(className, self.[className])

        # set shuffle-seed
        randomSeed = 666 # as long as the seed stays the same, the shuffle algorithm returns on shuffle always the same result
        if randomizeDataOrder:
            randomSeed = random.randint(0, 100000000000)

        # shuffle inputData
        random.seed(randomSeed)
        random.shuffle(allData)

        # seperate training-data from test-data
        












                    



