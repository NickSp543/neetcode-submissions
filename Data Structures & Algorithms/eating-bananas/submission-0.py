class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if not piles:
            return 0
        
        l = math.ceil(sum(piles) / h)
        r = max(piles)

        while l <= r:
            mid = (l + r) // 2
            iterations = h

            for pile in piles:
                iterations -= math.ceil(pile / mid)
                    
            if iterations >= 0:
                r = mid - 1
            else:
                l = mid + 1
            
        return l