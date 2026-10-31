class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        row = [[0 for i in range(len(text2) + 1)] for j in range(len(text1) + 1)]

        for i in range(len(text1) - 1, -1, -1):
            for j in range(len(text2) - 1, -1, -1):
               if text1[i] == text2[j]:
                    row[i][j] = row[i + 1][j + 1] + 1
               else:
                    row[i][j] = max(row[i][j + 1], row[i+1][j])
        
        return row[0][0]
                

