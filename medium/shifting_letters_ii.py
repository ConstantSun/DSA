from typing import List
import heapq

class Solution:
    def shiftingLetters(self, s: str, origin_shifts: List[List[int]]) -> str:
        def scan(shifts):
            shifts.sort()
            final_shifts = [0]*len(s)
            hq = []
            j = 0
            for i in range(len(s)):
                while j < len(shifts) and shifts[j][0] <= i:
                    heapq.heappush(hq, [shifts[j][1],shifts[j][2]])
                    j += 1
                while hq and hq[0][0] < i:
                    heapq.heappop(hq)
                final_shifts[i] = len(hq)
            
            return final_shifts
        
        shifts_1 = [ele for ele in origin_shifts if ele[2] == 1]
        shifts_0 = [ele for ele in origin_shifts if ele[2] == 0]

        fw = scan(shifts_1)
        bw = scan(shifts_0)

        print("shifts fw: ", fw)
        print("shifts bw: ", bw)

        final = [0]*len(s)
        res = []
        for i in range(len(fw)):
            final[i] = fw[i] - bw[i]
            res.append(chr( (ord(s[i]) + fw[i] - bw[i] - ord('a'))%26 + ord('a') ))
        print("final shifts:")
        for i in range(len(final)):
            print(i, final[i])
        return ''.join(res)

sol = Solution()
s = "abc"
shifts = [[0,1,0],[1,2,1],[0,2,1]]

# s = "dztz"
# shifts = [[0,0,0],[1,1,1]]

print(sol.shiftingLetters(s, shifts))