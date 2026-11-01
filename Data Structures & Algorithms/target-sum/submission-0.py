class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}

        def dfs(i, a):
            if i == len(nums):
                if a == target:
                    return 1
                return 0
            if (i, a) in dp:
                return dp[(i, a)]
            paths = dfs(i + 1, a + nums[i])
            paths += dfs(i + 1, a - nums[i])
            dp[(i, a)] = paths
            return paths

        return dfs(0, 0)