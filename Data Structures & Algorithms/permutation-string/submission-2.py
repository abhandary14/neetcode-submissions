class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        count1, count2 = [0]*26, [0]*26
        for i in range(len(s1)):
            count1[ord(s1[i]) - ord('a')] += 1
            count2[ord(s2[i]) - ord('a')] += 1
        
        matches = 0
        for i in range(26):
            matches += (1 if count1[i] == count2[i] else 0)

        l = 0
        for r in range(len(s1), len(s2)): # since we already initialized the count of both till the length of s1, we iterate the right pointer from the length of s1 till the length of s2
            if matches == 26:
                return True
            
            # adding a character to the window
            index = ord(s2[r]) - ord('a') # current index in the array
            count2[index] += 1
            if count1[index] == count2[index]:
                matches += 1
            elif count1[index] + 1 == count2[index]:
                matches -= 1
            
            # removing a character after adding to the window, we do the exact opposite of the above
            index = ord(s2[l]) - ord('a')
            count2[index] -= 1
            if count1[index] == count2[index]:
                matches += 1
            elif count1[index] - 1 == count2[index]:
                matches -= 1
            l += 1

        return matches == 26 