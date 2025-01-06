from typing import List
from sortedcontainers import SortedList

class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        i,j = 0,0
        sl = SortedList()
        count = 0
        while j < len(nums):
            sl.add(nums[j])
            while nums[j] > sl[-1] or nums[j] < sl[0]:
                sl.remove(nums[i])
                i += 1
            count += j - i + 1
            j += 1
        return count

sol = Solution()
nums = [5,4,2,4]
# nums = [1,2,3]
# nums = [1,2,3,2,2,1]
# nums = [1,10]
# nums = [4,5,6,7,8,9,10,10]
print(sol.continuousSubarrays(nums))

1+2+3+4+5+6


