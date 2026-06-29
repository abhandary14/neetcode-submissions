# The children of a state:
# The children would be the states we get after turning each wheel clockwise and anti-clockwise:
# 6769 -> 7769, 5769, 6869, 6669, 6779, 6759, 6760, 6768

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        # apparently "0000" can be in the deadends
        if "0000" in deadends:
            return -1
        
        def children(lock): # get all 8 children of a state.
            res = []
            for i in range(4):
                digit = str((int(lock[i]) + 1) % 10)
                res.append(lock[:i] + digit + lock[i+1:]) # we can't modify strings in place in python so we need to rebuild it before appending
                
                digit = str((int(lock[i]) - 1 + 10) % 10)
                res.append(lock[:i] + digit + lock[i+1:])

            return res

        q = deque()
        q.append(["0000", 0]) # [the state, the number of moves it took us to reach here]
        
        visit = set(deadends) 
        # for the deadends, we can either declare a separate set. but the smart thing would be to initilaize the visit set with the deadends so they're not visited again

        while q:
            lock, turns = q.popleft()
            if lock == target:
                return turns
            
            for child in children(lock):
                if child not in visit:
                    visit.add(child)
                    q.append([child, turns + 1])
        
        return -1
            