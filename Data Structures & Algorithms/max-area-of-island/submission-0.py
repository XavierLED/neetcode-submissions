class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visit = set()
        maxArea = 0
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        rows, cols = len(grid), len(grid[0])

        def bfs(r, c):
            size = 1
            q = collections.deque()
            q.append((r, c))
            visit.add((r, c))
            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    r, c = dr + row, dc + col
                    if (r in range(rows) and c in range(cols)
                    and (r, c) not in visit and grid[r][c] == 1):
                        q.append((r, c))
                        visit.add((r, c))
                        size += 1

            return size


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visit:
                    attempt = bfs(r, c)
                    maxArea = max(maxArea, attempt)
        
        return maxArea
