class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = s.replace(" ", "").casefold()
        i, j = 0, len(string) - 1

        while i < j:
            while i < j and not string[i].isalnum():
                i += 1
            while i < j and not string[j].isalnum():
                j -= 1
            if string[i] != string[j]:
                return False
            i, j = i + 1, j - 1
        
        return True