from collections import defaultdict
from typing import List

from LogHelper import LogHelper


class EvaluateDivision:
    def __init__(self, equations: List[List[str]], values: List[float], queries: List[List[str]]):
        LogHelper.PrintInput(equations)
        LogHelper.PrintInput(values)
        LogHelper.PrintInput(queries)
        LogHelper.PrintOutput(self.calcEquation(equations, values, queries))

    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        valueDict = defaultdict(dict)

        print(valueDict['c'])

        for i, equa in enumerate(equations):
            if not valueDict.__contains__(equa[0]):
                valueDict[equa[0]] = 1
            valueDict[equa[1]] = valueDict[equa[0]] / values[i]

        ans:List[float] = []
        for i, quer in enumerate(queries):
            if valueDict.__contains__(quer[0]) and valueDict.__contains__(quer[1]):
                ans.append(valueDict[quer[0]] / valueDict[quer[1]])
            else:
                ans.append(-1)

        return ans