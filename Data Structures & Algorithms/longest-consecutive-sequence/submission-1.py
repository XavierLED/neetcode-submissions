class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        store = set(nums)
        res = 0

        for i in store:
            w = 1
            if i - 1 in store:
                continue
            
            else:
                while i + w in store:
                    w += 1
            res = max(res, w)
        return res 