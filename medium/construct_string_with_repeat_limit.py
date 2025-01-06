from collections import Counter
import heapq 
class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        ans = []
        count = Counter(s)
        hq = []
        for k, v in count.items():
            heapq.heappush(hq, [-ord(k), v])
        while hq:
            last_char, last_count = chr(-hq[0][0]), hq[0][1]
            heapq.heappop(hq)

            use = min(repeatLimit, last_count)
            ans.append(last_char*use)
            if last_count > use and hq:
                sec_char, sec_count =  chr(-hq[0][0]), hq[0][1]
                heapq.heappop(hq)
                sec_count -= 1
                ans.append(sec_char)

                if sec_count:
                    heapq.heappush(hq, [-ord(sec_char), sec_count])
                heapq.heappush(hq, [-ord(last_char), last_count-use])

        return ''.join(ans)
    
sol = Solution()
s = "cczaccczccc"
repeatLimit = 3

# s = "aababab"
# repeatLimit = 2
print(sol.repeatLimitedString(s, repeatLimit))
                



        