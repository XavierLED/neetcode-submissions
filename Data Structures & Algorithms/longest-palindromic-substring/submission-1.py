class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = 0
        resLen = 0

        for i in range(len(s)):
            r, l = i, i
            while(l >= 0 and r < len(s) and s[l] == s[r]):
                if r - l + 1 > resLen:
                    res = l
                    resLen = r - l + 1
                r, l = r + 1, l - 1

            r, l = i + 1, i
            while(l >= 0 and r < len(s) and s[l] == s[r]):
                if r - l + 1 > resLen:
                    res = l
                    resLen = r - l + 1
                r, l = r + 1, l - 1
        
        return s[res: res + resLen]