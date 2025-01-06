from typing import List


class Solution:
    dif_exp = 0
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        def next_number(current: int, idx: int):
            if idx == len(nums):
                if current == target:
                    self.dif_exp += 1
                return
            next_number(current+nums[idx], idx+1)
            next_number(current-nums[idx], idx+1)
        
        next_number(0,0)
        return self.dif_exp



class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        self.total_sum = sum(nums)
        memo = [
            [float("-inf")] * (2 * self.total_sum + 1) for _ in range(len(nums))
        ]
        return self.calculate_ways(nums, 0, 0, target, memo)

    def calculate_ways(
        self,
        nums: List[int],
        current_index: int,
        current_sum: int,
        target: int,
        memo: List[List[int]],
    ) -> int:
        if current_index == len(nums):
            # Check if the current sum matches the target
            return 1 if current_sum == target else 0
        else:
            # Check if the result is already computed
            if memo[current_index][current_sum + self.total_sum] != float(
                "-inf"
            ):
                return memo[current_index][current_sum + self.total_sum]

            # Calculate ways by adding the current number
            add = self.calculate_ways(
                nums,
                current_index + 1,
                current_sum + nums[current_index],
                target,
                memo,
            )

            # Calculate ways by subtracting the current number
            subtract = self.calculate_ways(
                nums,
                current_index + 1,
                current_sum - nums[current_index],
                target,
                memo,
            )

            # Store the result in memoization table
            memo[current_index][current_sum + self.total_sum] = add + subtract

            return memo[current_index][current_sum + self.total_sum]

            

sol = Solution()
nums = [1,1,1,1,1]
target = 3

nums = [0]
target = 1

print(sol.findTargetSumWays(nums, target))

