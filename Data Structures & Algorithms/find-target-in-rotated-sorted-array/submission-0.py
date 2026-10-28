class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        cut = 0
        
        while r >= l:
            m = (l + r) // 2

            if nums[r] < nums[m]:
                l = m + 1
            
            elif nums[l] < nums[m]:
                r = m - 1
            
            else:
                cut = m
                r -= 1
                l += 1
        
        l, r = cut, len(nums) - 1
        while r >= l:
            m = (l + r) // 2

            if nums[m] > target:
                r = m - 1
            
            elif nums[m] < target:
                l = m + 1
            
            else:
                return m

        l, r = 0, cut - 1
        while r >= l:
            m = (l + r) // 2

            if nums[m] > target:
                r = m - 1
            
            elif nums[m] < target:
                l = m + 1
            
            else:
                return m
        
        return -1
