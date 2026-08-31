from bisect import bisect_left
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        for num in nums:
            seen[num] = seen.get(num, 0) + 1
        res = []
        counts = []
        for key, val in seen.items():
            pos = bisect_left(counts, val)
            res.insert(pos, key)
            counts.insert(pos, val)
        return res[-k:]