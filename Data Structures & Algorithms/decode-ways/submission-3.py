class Solution:
    def numDecodings(self, s: str) -> int:
        dic = {len(s): 1}
        for i in range(len(s) - 1, -1, -1):
            if s[i] == "0":
                dic[i] = 0
            else:
                dic[i] = dic[i + 1]

            if i + 1 < len(s) and (s[i] == "1" or s[i] == "2" and s[i + 1] in "0123456"):
                dic[i] += dic[i + 2]
        
        return dic[0]
