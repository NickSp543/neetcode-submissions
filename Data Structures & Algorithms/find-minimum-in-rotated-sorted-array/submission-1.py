class Solution:
    def findMin(self, nums: List[int]) -> int:
        if not nums:
            return -1

        l = 0
        r = len(nums) - 1

        while l < r:
            mid = (l + r) // 2

            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid

        return nums[l]