class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # we know that the words are sorted
        # so if given ["hrn", "hrf"], we know that n comes before f
        # we can think of this as a graph problem
        # since we know that n comes before f, we can make an edge n -> f.
        # similarly, we know that h comes before r, so h -> r, and so on
        # then we find the topological sort of this graph to get the lexicographical order

        # we make a hashmap for each character that maps to a set denoting the neighbors
        adj = {c: set() for w in words for c in w}
        indegree = {c: 0 for c in adj}

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]  # take two at a time

            # for it to be a valid dictionary, the first word has to be smaller or same in length than the second word IF they have a common prefix
            # for example, if we have [adjx, adj] it is not valid (self explanatory)

            minLen = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""

            # now we make the graph
            for j in range(minLen):
                if w1[j] != w2[j]:  # every character that is not common in the two,
                    if w2[j] not in adj[w1[j]]:  # if it is not present
                        adj[w1[j]].add(w2[j])
                        indegree[w2[j]] += 1
                    break  # break

        # BFS
        q = deque([c for c in indegree if indegree[c] == 0])
        res = []

        while q:
            c = q.popleft()
            res.append(c)

            for nei in adj[c]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)

        # we have to have visited all letters
        if len(res) != len(indegree):
            return ""

        return "".join(res)
