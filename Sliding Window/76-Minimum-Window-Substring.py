class Solution:

    def isValid(self, count, count2):

        for i in count:
            if count[i]>count2[i]:
                return False
        return True
    
    def validSubstring(self, s, t):

        freq={}
        freq2={}

        for i in t:
            freq[i]=1+freq.get(i,0)
        for i in s:
            if i in freq:
                freq2[i]=1+freq2.get(i,0)

        for i in freq:
            if i not in freq2:
                return False
            if i in freq2 and freq[i]>freq2[i]:
                return False
        return True

    def minWindow(self, s: str, t: str) -> str:

        if len(s)<len(t):
            return ""
        res = [0,len(s)]

        if self.validSubstring(s,t)==False:
            return ""

        count={}
        count2={}

        for i in range(len(t)):
            count[t[i]]=1+count.get(t[i],0)
            count2[t[i]]=0

        l,r=0,0

        while r<len(s) and l<=r:
            
            if self.isValid(count, count2):
                if s[l] in count2:
                    count2[s[l]]-=1
                if r-l<res[1]-res[0]:
                    res=[l,r]
                l+=1
            else:
                if s[r] in count:
                    count2[s[r]]+=1
                r+=1
        
        while self.isValid(count, count2):
            if s[l] in count2:
                count2[s[l]]-=1
            if r-l<res[1]-res[0]:
                res=[l,r]
            l+=1
        return s[res[0]:res[1]]