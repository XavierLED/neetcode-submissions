class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.casefold()
        replace = [' ','.','?','!','"',"'",'(', ')',',',':',';']
        for i in replace:
            s = s.replace(i,'')
        leng = len(s)

        for i in range(leng):
            if not(s[i] == s[leng - i - 1]):
                return False
        return True
        