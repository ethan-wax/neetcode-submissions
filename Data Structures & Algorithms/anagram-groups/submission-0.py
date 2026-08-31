class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        for s in strs:
            pat = [0] * 26
            for c in s:
                pat[ord(c) - ord('a')] += 1
            pat = tuple(pat)
            if pat not in seen:
                seen[pat] = []
            seen[pat].append(s)
        return list(seen.values())