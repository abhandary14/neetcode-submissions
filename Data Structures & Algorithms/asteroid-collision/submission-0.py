class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # stack = []
        # for a in asteroids:
        #     if stack and ((stack[-1] > 0 and a > 0) or (stack[-1] < 0 and a < 0)):
        #         stack.append(a)
        #     elif stack and (a > 0 and stack[-1] < 0) or (a < 0 and stack[-1] > 0):
        #         if abs(a) > abs(stack[-1]):
        #             stack.append(a)
        #     elif stack and a == stack[-1]:
        #         stack.pop()
        #     else:
        #         stack.append(a)
        # return stack

        # asteroid collision only happens when a positive one is followed by a negative. 
        # when the one on the left moves right and the one on the right moves left

        stack = []
        for a in asteroids:
            destroyed = False
            while stack and stack[-1] > 0 and a < 0:
                if stack[-1] < abs(a):
                    stack.pop()
                elif stack[-1] == abs(a):
                    stack.pop()
                    destroyed = True
                    break
                else:
                    destroyed = True
                    break

            if not destroyed:
                stack.append(a)
        
        return stack