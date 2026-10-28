class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hashMap = defaultdict(list)
        for word in strs:
            alphabet = [0] * 26 
            for char in word:
                alphabet[ord(char) - 97] += 1
            hashMap[tuple(alphabet)].append(word)
        return list(hashMap.values())