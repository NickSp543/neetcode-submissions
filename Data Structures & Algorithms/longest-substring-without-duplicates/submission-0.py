class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        seen = set()
        l = 0
        r = 0
        max_set = 0
        while r < len(s):
            while s[r] in seen and l<r:
                seen.remove(s[l])
                l += 1
            seen.add(s[r])
            max_set = max(max_set,len(seen))
            r += 1

        return max_set