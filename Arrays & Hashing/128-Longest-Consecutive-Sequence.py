class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        ans = 0
        for i in range(len(nums)):
            c = 1
            if nums[i]-1 not in nums_set:
                for j in range (1,len(nums)):
                    if nums[i]+j in nums_set:
                        c+=1
                    else:
                        break
            ans = max(ans, c)
        return ans