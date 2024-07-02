from LogHelper import LogHelper


class NthTribonacciNumber:
    def __init__(self, n: int):
        LogHelper.PrintInput(n)
        LogHelper.PrintOutput(self.tribonacci(n))

    def tribonacci(self, n: int) -> int:
        fibQue = []

        fibQue.append(0)
        fibQue.append(0)
        fibQue.append(0)

        for i in range(n):
            if i == 0:
                fibQue.append(1)
            else:
                fibQue.append(fibQue[0] + fibQue[1] + fibQue[2])
            fibQue.pop(0)
            print(fibQue)
        return fibQue[-1]