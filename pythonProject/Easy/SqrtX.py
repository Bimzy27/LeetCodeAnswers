from pythonProject.LogHelper import LogHelper


class SqrtX:
    def __init__(self, x: int):
        LogHelper.PrintInput(x)
        LogHelper.PrintOutput(self.mySqrt(x))

    def mySqrt(self, x: int) -> int:

        last2 = int(x)
        last1 = int(x * 0.5)

        while True:
            pow = last1^2
            if pow == x:
                return last1
            elif pow < x:
                last2 = last1
                last1 = int(last1 * 0.5)
            else:
                last2 = last1
                last1 = int(last2 + (last1 * 0.5))

            if last1 == last2:
                return last1
