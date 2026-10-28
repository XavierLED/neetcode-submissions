class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        store = set()
        res = 0

        for i in nums:
            store.add(i)
        
        for i in store:
            w = 1
            j = 1
            if i - 1 in store:
                continue
            
            else:
                while i + w in store:
                    j += 1
                    w += 1
            res = max(res, j)
        return res 