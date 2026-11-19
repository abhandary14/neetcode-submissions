class CountSquares:
    def __init__(self):
        self.pointsCnt = defaultdict(int)
        self.points = []

    def add(self, point: List[int]) -> None:
        self.pointsCnt[tuple(point)] += 1 # typecast to tuple to make it hashable
        self.points.append(point)

    def count(self, point: List[int]) -> int:
        res = 0
        px, py = point

        for x, y in self.points:
            if (abs(py - y) != abs(px - x)) or x == px or y == py:
                continue
            res += self.pointsCnt.get((x, py), 0) * self.pointsCnt.get((px, y), 0)
        
        return res
