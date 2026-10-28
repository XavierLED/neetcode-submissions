class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap1 = {}
        hashmap2 = {}

        if len(t) == len(s):
            for i in range(len(s)):
                hashmap1[s[i]] = 1 + hashmap1.get(s[i], 0)
                hashmap2[t[i]] = 1 + hashmap2.get(t[i], 0)

            return hashmap1 == hashmap2
        
        return False

        