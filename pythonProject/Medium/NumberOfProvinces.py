from typing import List

from LogHelper import LogHelper


class NumberOfProvinces:
    def __init__(self, isConnected: List[List[int]]):
        LogHelper.PrintInput(isConnected)
        LogHelper.PrintOutput(self.findCircleNum(isConnected))

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        self.provinces = 0

        def validCities(cities:List[int])->bool:
            for i, num in enumerate(cities):
                if num == 1:
                    return True
            return False

        def checkProvinces(i):
            for j, num in enumerate(isConnected[i]):
                if num == 1:
                    isConnected[i][j] = -1
                    checkProvinces(j)

        for i in range(len(isConnected)):
            if validCities(isConnected[i]):
                self.provinces += 1
                checkProvinces(i)

        return self.provinces