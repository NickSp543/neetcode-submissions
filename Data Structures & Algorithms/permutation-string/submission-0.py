class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        mp_s1 = {}
        mp_s2 = {}

        for c in s1:
            mp_s1[c] = mp_s1.get(c, 0) + 1

        size = len(s1)
        l = 0
        r = size - 1

        for i in range(size):
            mp_s2[s2[i]] = mp_s2.get(s2[i], 0) + 1

        while r < len(s2):
            if mp_s1 == mp_s2:
                return True

            mp_s2[s2[l]] -= 1

            if mp_s2[s2[l]] == 0:
                del mp_s2[s2[l]]

            l += 1
            r += 1

            if r < len(s2):
                mp_s2[s2[r]] = mp_s2.get(s2[r], 0) + 1

        return False