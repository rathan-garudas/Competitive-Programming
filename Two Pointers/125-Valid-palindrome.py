class Solution:
    def isPalindrome(self, s: str) -> bool:
        l,r=0,len(s)-1

        alphanum = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"

        while l<r:
            if s[l] in alphanum and s[r] in alphanum:
                if s[l].lower()!=s[r].lower():
                    return False
                l+=1
                r-=1
            elif s[l] in alphanum:
                r-=1
            else:
                l+=1
        
        return True
