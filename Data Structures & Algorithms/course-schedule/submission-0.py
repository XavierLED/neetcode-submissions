class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courseTable = {i:[] for i in range(numCourses)}
        visit = set()

        for crs, pre in prerequisites:
            courseTable[crs].append(pre)
        
        def dfs(crs):
            if courseTable[crs] == []:
                return True
            if crs in visit:
                return False
            
            visit.add(crs)
            for pre in courseTable[crs]:
                if not dfs(pre): return False
            
            courseTable[crs] = []
            return True
            

        for crs in range(numCourses):
            if not dfs(crs): return False
        
        return True