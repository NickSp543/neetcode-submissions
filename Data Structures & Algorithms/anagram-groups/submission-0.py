class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs:
            return []

        stringMap = {}

        for s in strs:
            mp = {}

            for char in s:
                mp[char] = mp.get(char, 0) + 1

            key = tuple(sorted(mp.items()))

            if key in stringMap:
                stringMap[key].append(s)
            else:
                stringMap[key] = [s]

        res = []

        for l in stringMap.values():
            res.append(l)

        return res