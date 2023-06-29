class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]: 
        freq={}
        for i in strs:
            if "".join(sorted(i)) in freq:
                freq["".join(sorted(i))].append(i)
            else:
                freq["".join(sorted(i))]=[]
                freq["".join(sorted(i))].append(i)
        return list(freq.values())
