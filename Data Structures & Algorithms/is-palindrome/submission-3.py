class Solution:
    def isPalindrome(self, s: str) -> bool:
        s2 = ''
        for i in range(len(s)):
            if s[i].isalnum():
                s2 += s[i]

        print(s2)

        i = 0
        while i != (len(s2)-i-1) and (len(s2)-i-1) != -1:
            if s2[i].lower() != s2[len(s2)-i-1].lower():
                return False
            i += 1
        return True

            
        