class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1)>len(s2):
            return False
            
        count=[0]*26
        count2=[0]*26
        ans=0
        for i in range(len(s1)):
            count[ord(s1[i])-ord('a')]+=1
            count2[ord(s2[i])-ord('a')]+=1

        l=0
        matches=0
        for i in range(len(s1), len(s2)):
            matches=0

            for j in range(26):
                if count[j]==count2[j]:
                    matches+=1

            if matches==26:
                return True

            count2[ord(s2[i])-ord('a')]+=1

            count2[ord(s2[l])-ord('a')]-=1

            l+=1

        
        matches=0
        for j in range(26):
            if count[j]==count2[j]:
                matches+=1

        if matches==26:
            return True
        return False
