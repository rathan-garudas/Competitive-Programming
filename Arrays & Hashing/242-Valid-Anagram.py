class Solution:
    
    def wordCount(self, count_l, word):
        for i in word:
            if i in count_l:
                count_l[i]+=1
            else:
                count_l[i]=1
        return count_l

    def isAnagram(self, s: str, t: str) -> bool:
        freq1 = {}
        freq1 = self.wordCount(freq1, s)
        freq2 = {}
        freq2 = self.wordCount(freq2, t)
        
        if len(freq1) != len(freq2):
            return False
        
        for i in freq1:
            if i in freq2 and freq1[i] == freq2[i]:
                continue
            else:
                return False
        return True
    

    