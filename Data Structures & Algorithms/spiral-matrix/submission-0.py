class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        ans = []
        seen = set()
        def neighbor(i, j, d):
            r, c = i + d[0], j + d[1]
            if 0 <= r < m and 0 <= c < n and (r, c) not in seen:
                return r, c, d
            if d == (0, 1):
                d = (1, 0)
            elif d == (1, 0):
                d = (0, -1)
            elif d == (0, -1):
                d = (-1, 0)
            else:
                d = (0, 1)

            r, c = i + d[0], j + d[1]
            if 0 <= r < m and 0 <= c < n and (r, c) not in seen:
                return r, c, d
            return None

        i, j = 0, 0
        d = (0, 1)
        while True:
            ans.append(matrix[i][j])
            seen.add((i, j))
            nextCell = neighbor(i, j, d)
            if nextCell is None:
                return ans
            i, j, d = nextCell
        return ans