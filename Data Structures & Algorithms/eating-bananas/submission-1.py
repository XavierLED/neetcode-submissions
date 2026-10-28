class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r

        while r >= l:
            m = (l + r) // 2
            tempTime = 0
            
            for i in piles:
                tempTime += math.ceil(i / m)

            if tempTime > h:
                l = m + 1
            
            else:
                r = m - 1
                res = m
        return res


         

