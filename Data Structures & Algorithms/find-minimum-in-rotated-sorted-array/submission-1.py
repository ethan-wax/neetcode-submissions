class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        first = nums[0]
        if n == 1:
            return first
        l, r = 0, n-1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] >= first:
                l = mid + 1
            else:
                r = mid - 1
        return nums[l % n]