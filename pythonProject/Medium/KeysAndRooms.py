from typing import List

from LogHelper import LogHelper


class KeysAndRooms:
    def __init__(self, rooms: List[List[int]]):
        LogHelper.PrintInput(rooms)
        LogHelper.PrintOutput(self.canVisitAllRooms(rooms))

    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        self.keys = set()
        self.visited = set()
        self.roomCount = len(rooms)

        def addKeys(keys: List[int]):
            for i, num in enumerate(keys):
                self.keys.add(num)

        def visitRoom(room: int):
            self.visited.add(room)
            addKeys(rooms[room])
            for i, num in enumerate(rooms[room]):
                if self.keys.__contains__(num) and not self.visited.__contains__(num):
                    visitRoom(num)

        visitRoom(0)

        print(self.keys)
        print(self.visited)
        return len(self.visited) == self.roomCount