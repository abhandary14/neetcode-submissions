# bruteforce solution is to sort the stream every 
# sorting m operations takes (m * n log n) time for a stream of size n
# addNum takes O(n)

class MedianFinder:

    def __init__(self):
        self.stream = []

    def addNum(self, num: int) -> None:
        self.stream.append(num)

    def findMedian(self) -> float: # m * (n log n)
        self.stream.sort()

        n = len(self.stream)
        if n % 2 == 1:
            return self.stream[n // 2]
        else:
            return (self.stream[n // 2] + self.stream[n // 2 - 1]) / 2
        