class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        res = 1000

        while r >= l:
            m = (l + r) // 2

            if(nums[m] > nums[l] and nums[l] < nums[r]):
                r = m - 1
            
            elif(nums[m] > nums[r] and nums[r] < nums[l]):
                l = m + 1
            
            else:
                if nums[m] < res:
                    res = nums[m]
                r -= 1
                l += 1
        
        return res

         