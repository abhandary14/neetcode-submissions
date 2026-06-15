class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        # so every word has to be a prefix of the next word till the characters are same.
        # dag and disk -> d is the common character, and a comes before i in the language in example 1.
        # we just need to verify this condition for every pair of words.
        # we can use a hashmap to store the indices of characters in the language order.

        hashmap = {c : i for i, c in enumerate(order)} # {h:0, l:1, a:2...}

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i+1]

            for j in range(len(w1)): # we only need word 1. if all characters in word1 are in the same order in word2, then word1 is a prefix of word2 and the condition holds true.
                if j == len(w2):
                    return False
                
                if w1[j] != w2[j]:
                    if hashmap[w2[j]] < hashmap[w1[j]]: # if the characters are not same and the one in the w1 comes after the one in w2, then the order is broken
                        return False
                    break
                
        return True