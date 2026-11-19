class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = [str(d) for d in digits]
        
        s = "".join(digits)
        
        num = int(s)
        num += 1
        
        res = [int(c) for c in str(num)]
        
        return res