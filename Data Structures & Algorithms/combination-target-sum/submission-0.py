class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        numsLen = len(nums)

        def helper(index, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            if not numsLen > index or total > target:
                return 
            
            cur.append(nums[index])
            helper(index, cur, total + nums[index])
            cur.pop()
            helper(index + 1, cur, total)

        helper(0, [], 0)
        return res