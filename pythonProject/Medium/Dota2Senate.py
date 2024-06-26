from collections import deque

from LogHelper import LogHelper


class Dota2Senate:
    def __init__(self, senate: str):
        LogHelper.PrintInput(senate)
        LogHelper.PrintOutput(self.predictPartyVictory(senate))

    def predictPartyVictory(self, senate: str) -> str:
        senArr = list(senate)
        rQueue = deque()
        dQueue = deque()

        for i, c in enumerate(senArr):
            if c == 'R':
                rQueue.append(i)
            else:
                dQueue.append(i)

        while dQueue and rQueue:
            dTurn = dQueue.popleft()
            rTurn = rQueue.popleft()

            if rTurn < dTurn:
                rQueue.append(dTurn + len(senArr))
            else:
                dQueue.append(rTurn + len(senArr))

        return "Radiant" if rQueue else "Dire"
