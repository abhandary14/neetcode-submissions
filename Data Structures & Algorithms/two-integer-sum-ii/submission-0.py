class Solution:
    def tsHash(self, numbers, target):
        dic = {}
        for i in range(len(numbers)):
            dic[numbers[i]] = i

        for i in range(len(numbers)):
            d = target - numbers[i]
            if d in numbers:
                return [i + 1, dic[d] + 1]
        return []

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # return self.tsHash(numbers, target)
        left = 0
        right = len(numbers) - 1

        while left < right:
            current = numbers[left] + numbers[right]
            if current > target:
                right -= 1
            elif current < target:
                left += 1
            else:
                return [left + 1, right + 1]
        return []