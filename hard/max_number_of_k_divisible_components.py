from typing import List
from collections import defaultdict
from functools import cache

class Solution:
    count = 1
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        neighbors = defaultdict(set)
        for e1, e2 in edges:
            neighbors[e1].add(e2)
            neighbors[e2].add(e1)
        visited = set([0])
        @cache
        def get_sum(root):
            total = values[root]
            for node in neighbors[root]:
                if node not in visited:
                    visited.add(node)
                    total += get_sum(node)
            return total
        get_sum(0)

        visited = set([0])
        def bfs(root):
            for node in neighbors[root]:
                if node not in visited:
                    if get_sum(node) % k == 0:
                        self.count += 1
                    visited.add(node)
                    bfs(node)
        bfs(0)
        return self.count


sol = Solution()

n = 5
edges = [[0,2],[1,2],[1,3],[2,4]]
values = [1,8,1,4,4]
k = 6


# n = 7
# edges = [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6]]
# values = [3,0,6,1,5,2,1]
# k = 3

# n = 2
# edges = [[0,1]]
# values = [4,4]
# k = 2
print(sol.maxKDivisibleComponents(n, edges, values, k))

