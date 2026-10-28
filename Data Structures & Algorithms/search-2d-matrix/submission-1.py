class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix[0]) - 1
        t, b = 0, len(matrix) - 1

        while t <= b:
            m = (t + b) // 2

            if matrix[m][l] > target:
                b = m - 1
            
            elif matrix[m][r] < target:
                t = m + 1
            
            else:
                while r >= l:
                    n = (r + l) // 2

                    if matrix[m][n] > target:
                        r = n - 1
                    
                    elif matrix[m][n] < target:
                        l = n + 1
                    
                    else:
                        return True
        
        return False
