class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        mp = {} #letter -> frequency
        l = 0
        r = 0
        max_possible = 0
        for r,c  in enumerate(s):

            mp[c] = mp.get(c,0) + 1

            while (r-l+1) - max(mp.values()) > k and l<r:
                mp[s[l]] -= 1
                l += 1
            max_possible = max(max_possible,r-l+1)
        return max_possible

            






