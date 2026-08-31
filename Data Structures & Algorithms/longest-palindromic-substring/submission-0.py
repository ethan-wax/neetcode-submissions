class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        best = ''
        for i in range(n):
            l, r = i, i
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
            if (r - l - 1) > len(best):
                best = s[l+1:r]
            
            l, r = i, i+1
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
            if (r - l - 1) > len(best):
                best = s[l+1:r]
        return best