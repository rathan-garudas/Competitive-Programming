class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        freq={}
        for i in range(len(nums)):
            if nums[i] in freq:
                return [freq[nums[i]], i]
            freq[target-nums[i]] = i
