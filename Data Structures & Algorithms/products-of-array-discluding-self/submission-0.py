class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        pre = []
        suf = []
        
        for i in range(len(nums)):
            if i > 1:
                pre.append(pre[i - 1] * nums[i - 1])
            
            elif i == 0:
                pre.append(1)
            
            else:
                pre.append(nums[0])


        for i in range(len(nums) - 1, -1, -1):
            if i < len(nums) - 2:
                suf.insert(0, (suf[0] * nums[i + 1]))
            
            elif i == len(nums) - 1:
                suf.insert(0, 1)
            
            else:
                suf.insert(0, nums[i + 1])
        
        for i in range(len(pre)):
            res.append(pre[i] * suf[i])
        
        return res
