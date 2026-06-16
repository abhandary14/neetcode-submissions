class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # if there's no outgoing edge to a node, that guy is the judge
        # judge will have incoming edges to all nodes except him0
        # think of it as an adjacency list.
        # let's make a hashmap of incoming edges and a hashmap of outgoing edges

        incoming, outgoing = defaultdict(set), defaultdict(set)
        for i, j in trust:
            incoming[j].add(i)
            outgoing[i].add(j)
        
        judge = -1
        for i in incoming:
            if len(incoming[i]) == n-1 and i not in outgoing:
                judge = i
        
        return judge
        
