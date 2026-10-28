class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums[0] = [nums[0]]
        for i in nums:
            if i in nums[0]:
                return i
            else:
                nums[0].append(i)