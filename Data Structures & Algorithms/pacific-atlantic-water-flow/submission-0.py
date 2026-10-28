class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        pac, atl = set(), set()
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def dfs(r, c, ocean):
            ocean.add((r, c))
            height = heights[r][c]

            for dr, dc in directions:
                row, col = r + dr, c + dc
                if (row in range(rows) and col in range(cols)
                and heights[row][col] >= height and (row, col) not in ocean):
                    dfs(row, col, ocean)

        
        for c in range(cols):
            dfs(0, c, pac)
            dfs(rows - 1, c, atl)
        
        for r in range(rows):
            dfs(r, 0, pac)
            dfs(r, cols - 1, atl)
        
        res = []
        for r in range(rows):
            for c in range(cols):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])
        
        return res
