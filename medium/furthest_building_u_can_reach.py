from typing import List
import heapq

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        # hq = []
        
        # for i in range(len(heights)-1) :
        #     sub = heights[i+1] - heights[i]
        #     if sub > 0:
        #         if ladders > 0:
        #             ladders -= 1
        #             heapq.heappush(hq, sub)
        #         else:
        #             if hq and hq[0] >= sub:
        #                 if bricks >= sub:
        #                     bricks -= sub
        #                 else:
        #                     return i
        #             else:
        #                 last_min = sub
        #                 if hq:
        #                     last_min = hq[0]
        #                     heapq.heappop(hq)
        #                     heapq.heappush(hq, heights[i+1])
        #                 if bricks >= last_min:
        #                     bricks -= last_min
        #                 else:
        #                     return i
        
        # return len(heights)-1


        hq = []
        for i in range(len(heights)-1):
            climb = heights[i+1] - heights[i]
            if climb <= 0:
                continue
            heapq.heappush(hq, climb)
            if ladders > 0:
                ladders -= 1
                continue
            bricks = bricks - heapq.heappop(hq)
            if bricks < 0:
                return i
        return len(heights) - 1

    
sol= Solution()
heights = [4,2,7,6,9,14,12]
bricks = 5
ladders = 1

heights = [4,12,2,7,3,18,20,3,19]
bricks = 10
ladders = 2

heights = [14,3,19,3]
bricks = 17
ladders = 0

print(sol.furthestBuilding(heights, bricks, ladders))


