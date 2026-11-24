class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # all of them start from JFK
        # start from JFK. The only thing we're worry about is the lexicographically order.
        # we need to build the graph in a way that it always uses the lexicographically smaller one

        adj = defaultdict(list)

        # sort it in reverse order so when we pop, it gives the lexicographically smallest one every time
        for u, v in sorted(tickets, reverse=True):
            adj[u].append(v)

        st = ["JFK"] # dfs
        itinerary = []

        while st:
            while adj[st[-1]]: # while there is somewhere to go from here,  
                curr = adj[st[-1]].pop() # will give the lexicographically smallest destination we can visit from this index
                st.append(curr)

            itinerary.append(st.pop()) # this will be reversed

        return itinerary[::-1]

        

        
