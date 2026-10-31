class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        cache = [1] * n
        for i in range(m - 1):
            row = [1] * n
            for j in range(n-2, -1, -1):
                row[j] = row[j + 1] + cache[j]
            cache = row
                
            
        return cache[0]
