class Solution:
    def reverseBits(self, n: int) -> int:
        b = bin(n)[2:]
        return int(b[::-1] + '0' * (32 - len(b)), 2)