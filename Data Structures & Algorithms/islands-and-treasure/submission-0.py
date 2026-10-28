class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        visit = set()
        q = collections.deque()

        def spaceVisit(r, c):
            if (r < 0 or r == rows or c < 0 or c == cols or (r, c) in visit
            or grid[r][c] == -1):
                return
            q.append((r, c))
            visit.add((r, c))
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r, c))
                    visit.add((r, c))
        
        dist = 0
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist

                spaceVisit(r + 1, c)
                spaceVisit(r - 1, c)
                spaceVisit(r, c - 1)
                spaceVisit(r, c + 1)
            dist += 1