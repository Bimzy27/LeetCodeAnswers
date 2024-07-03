import collections
from typing import List

from LogHelper import LogHelper

# solved using this tutorial https://www.youtube.com/watch?v=Uei1fwDoyKk&t=557s

class EvaluateDivision:
    def __init__(self, equations: List[List[str]], values: List[float], queries: List[List[str]]):
        LogHelper.PrintInput(equations)
        LogHelper.PrintInput(values)
        LogHelper.PrintInput(queries)
        LogHelper.PrintOutput(self.calcEquation(equations, values, queries))

    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = collections.defaultdict(list) # Map a -> list of [b, a/b]

        for i, eq in enumerate(equations):
            a, b = eq
            adj[a].append([b, values[i]])
            adj[b].append([a, 1 / values[i]])

        def bfs(src, target):
            if src not in adj or target not in adj:
                return -1
            q, visit = collections.deque(), set()
            q.append([src, 1])
            visit.add(src)
            while q:
                n, w = q.popleft()
                if n == target:
                    return w
                for nei, weight in adj[n]:
                    if nei not in visit:
                        q.append([nei, weight * w])
                        visit.add(nei)
            return -1


        return [bfs(q[0], q[1]) for q in queries]