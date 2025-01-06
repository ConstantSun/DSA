from typing import List 
import math 
 
class Solution: 
    ans = 0 
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int: 
        if sum(quantities) <= n:
            return 1 

        def seek(x1:int, n1:int, x2:int, n2:int): 
            if x1 + 1 == x2: 
                self.ans = x1 if n1 == n else x2 
                return  
            x = (x1+x2)//2 
            min_stores = 0 
            for num in quantities: 
                min_stores += math.ceil(num/x) 
            if min_stores <= n : 
                seek(x1, n1, x, min_stores) 
            else: 
                seek(x, min_stores, x2, n2) 
         
        seek(1, sum(quantities), max(quantities), len(quantities)) 
        return self.ans
        # TC: O(m * log k), where m: len(quantities), k: max value of quantities.
        # SC: O(log m) -> can reduce to O(1) using while loop instead of recursion.
 
sol = Solution() 
n = 6 
quantities = [11,6] 

n = 7
quantities = [15,10,10]

n = 1
quantities = [100000]

# n = 3
# quantities = [2]

n = 1
quantities = [1]

print(sol.minimizedMaximum(n, quantities))

