class Solution:
    def countSubstrings(self, s: str) -> int:
        palCount = 0

        for i in range(len(s)):
            r, l = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                palCount += 1
                r, l = r + 1, l - 1
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                palCount += 1
                l -= 1
                r += 1
        return palCount