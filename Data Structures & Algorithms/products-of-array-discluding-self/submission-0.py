class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        forward = []
        forward_prod = 1
        ptr = 0
        while ptr < len(nums):
            forward.append(forward_prod)
            forward_prod *= nums[ptr]
            ptr += 1
        forward.append(forward_prod)

        backward = []
        backward_prod = 1
        ptr = len(nums) - 1
        while ptr >= 0:
            backward.insert(0, backward_prod)
            backward_prod *= nums[ptr]
            ptr -= 1
        backward.append(backward_prod)

        res = []
        for i in range(len(nums)):
            res.append(forward[i] * backward[i])

        return res