class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        one, two = 0, 0

        for i in range(len(cost)):
            cost[i] = cost[i] + min(one, two)
            tmp = one
            one = cost[i]
            two = tmp
        
        return min(one, two)