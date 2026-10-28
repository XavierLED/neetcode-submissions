class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0
        if len(nums) == 1:
            return nums[0]
        
        for n in nums[1:]:
            tmp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = tmp
    
        wealth1 = max(rob1, rob2)

        rob1, rob2 = 0, 0
        for n in nums[:len(nums) - 1]:
            tmp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = tmp

        wealth2 = max(rob1, rob2)

        
        return max(wealth1, wealth2)