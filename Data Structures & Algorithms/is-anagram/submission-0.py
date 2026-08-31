class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_chars = {}
        for c in s:
            s_chars[c] = s_chars.get(c, 0) + 1
        for c in t:
            if c not in s_chars: return False
            s_chars[c] -= 1
        for val in s_chars.values():
            if val != 0: return False
        return True