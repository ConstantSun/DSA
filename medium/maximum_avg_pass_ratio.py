from typing import List
import heapq

class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        complementary = []
        maximum = 0
        for passed, total in classes:
            maximum += passed/total
            if passed != total:
                heapq.heappush(complementary, [-(passed+1)/(total+1)+passed/total, passed+1, total+1])
                
        if maximum == len(classes):
            return 1
        print("comp: ", complementary)
        while extraStudents:
            extraStudents -= 1
            sub, fir,sec = complementary[0]
            maximum += -sub
            heapq.heappop(complementary)
            heapq.heappush(complementary, [fir/sec - (fir+1)/(sec+1), fir+1, sec+1])
        
        return maximum/len(classes)


sol = Solution()
classes = [[1,2],[3,5],[2,2]]
extraStudents = 2

classes = [[2,4],[3,9],[4,5],[2,10]]
extraStudents = 4

print(sol.maxAverageRatio(classes, extraStudents))

