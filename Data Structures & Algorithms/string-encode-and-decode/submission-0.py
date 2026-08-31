class Solution:

    def encode(self, strs: List[str]) -> str:
        res = str(len(strs)) + '_'
        for s in strs:
            res += str(len(s)) + '_'
        for s in strs:
            res += s
        return res

    def decode(self, s: str) -> List[str]:
        ptr1 = s.find('_')
        num_strs = int(s[:ptr1])
        lens = []
        for _ in range(num_strs):
            ptr2 = s.find('_', ptr1 + 1)
            l = s[ptr1+1:ptr2]
            lens.append(int(l))
            ptr1 = ptr2
        res = []
        ptr1 += 1
        for l in lens:
            res.append(s[ptr1:ptr1+l])
            ptr1 = ptr1 + l
        return res
