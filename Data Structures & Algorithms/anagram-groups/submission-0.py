class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}

        for word in strs:
            temp = [0] * 26
            for char in word:
                temp[ord(char) - 97] += 1

            temp = tuple(temp)
            if temp in hashmap:
                hashmap[temp].append(word)
            else:
                hashmap[temp] = [word]

        anagrams = []
        for key in hashmap:
            anagrams.append(hashmap[key])
        
        return anagrams
        