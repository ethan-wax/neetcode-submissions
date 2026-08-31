from collections import Counter
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0: return False
        numHands = len(hand) // groupSize
        c = Counter(hand)
        for _ in range(numHands):
            start = min(c.keys())
            for i in range(groupSize):
                if start + i not in c:
                    return False
                c[start+i] -= 1
                if c[start+i] == 0:
                    del c[start+i]
        return True