from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        steps = [0]*len(nums)
        for i in range(len(nums)):
            for j in range( min(len(nums)-1, i+nums[i]),0,-1):
                if steps[j] == 0:
                    steps[j] = steps[i] + 1
                else:
                    break
        return steps[-1]
    
sol = Solution()
nums = [2,3,1,1,4]
nums = [2,3,0,1,4]
nums = [1,2,2,6,0]
print(sol.jump(nums))
