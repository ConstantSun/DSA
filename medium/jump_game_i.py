from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reachable = [0]*len(nums)
        reachable[0] = 1
        for i in range(len(nums)):
            if reachable[i]:
                for j in range( min(len(nums)-1, nums[i]+i) ,-1,-1):
                    if reachable[j]:
                        break
                    else:
                        reachable[j] = 1
        return bool(reachable[-1])
    
sol = Solution()
nums = [2,3,1,1,4]
nums = [3,2,1,0,4]
nums = [0]
print(sol.canJump(nums))
