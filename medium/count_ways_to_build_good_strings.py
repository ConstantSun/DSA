from functools import cache
class Solution:
    modulo = 1e9 + 7
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        @cache
        def dp(length):
            # print(f"\ndp({length}) = ")
            if length == 0:
                return 1
            if length < min(zero, one):
                return -1
            temp, flag = 0, 0
            if dp(length - zero) != -1:
                temp = (dp(length-zero) + temp) % self.modulo
                flag = 1
            if dp(length - one) != -1:
                temp = (dp(length - one) + temp) % self.modulo
                flag = 1
            if flag:
                return temp
            else:
                return -1
        
        ans = 0
        for i in range(low, high+1):
            print(f"dp({i}) = {dp(i)}")
            if dp(i) != -1:
                ans = (ans + dp(i)) % self.modulo
        return ans
    
sol = Solution()

low = 3
high = 3
zero = 1
one = 1

low , high , zero, one  = 2,3,1,2
low , high , zero, one  = 5,5,2,4
print(sol.countGoodStrings(low, high, zero, one))

