class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return []

        seen = {} # number -> index
        for i, num in enumerate(nums):
            dif = target - num
            if dif in seen:
                return [seen[dif] , i]
            seen[num] = i
        return []
