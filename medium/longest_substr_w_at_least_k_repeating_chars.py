from collections import defaultdict
import bisect 
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        seq = defaultdict(list)
        for i in range(26):
            seq[chr(i+ord('a'))] = [0]
        for k in range(len(s)):
            for i in range(26):
                seq[chr(i+ord('a'))].append(seq[chr(i+ord('a'))][-1])
            seq[s[k]][-1] += 1
        
        for i in range(26):
            print(seq[chr(i+ord('a'))])

        def get_optimal_idx(i: int, char: str):
            cur_no =  seq[char][i+1]
            if cur_no >= k:
                return i+1
            if cur_no == 0:
                return 0
            first_idx = bisect.bisect_left(seq[char], cur_no)

            return i+1-first_idx+1
        
        longest_sub_len = 0
        for i in range(len(s)):
            print("\n\n", s[i])
            cur_longest_len = 0
            for c in range(26):
                t = get_optimal_idx(i, chr(c+ord('a')))
                print(f"{ chr(c+ord('a')) }, opt: {t}")
                cur_longest_len = max(cur_longest_len, t )
            longest_sub_len = max(longest_sub_len, cur_longest_len)
        return longest_sub_len
        

sol= Solution()
s = "aaabb"
k = 3

s = "ababbc"
k = 2

print(sol.longestSubstring(s, k))
