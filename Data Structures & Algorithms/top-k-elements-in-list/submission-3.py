class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        l = []
        mp = {} #element -> frequency
        for num in nums:
            mp[num] = mp.get(num,0) + 1
        
        sorted_mp = sorted(mp, key=mp.get, reverse=True)

        for j in range (k):
            l.append(sorted_mp[j])
        return l