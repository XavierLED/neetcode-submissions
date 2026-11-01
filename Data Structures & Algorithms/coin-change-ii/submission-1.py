class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = {}

        def dfs(i, attempt):
            if attempt == amount:
                return 1
            if i >= len(coins) or attempt > amount:
                return 0
            if (i, attempt) in dp:
                return dp[(i, attempt)]

            path1 = dfs(i + 1, attempt)
            attempt += coins[i]
            path2 = dfs(i, attempt)

            dp[(i, attempt - coins[i])] = path2 + path1
            return path1 + path2
        
        return dfs(0, 0)
