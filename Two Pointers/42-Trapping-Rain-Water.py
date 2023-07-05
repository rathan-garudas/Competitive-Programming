class Solution:
    def trap(self, height: List[int]) -> int:
        
        max_height = 0
        result=0
        for i in range(len(height)):
            if height[i]>height[max_height]:
                max_height = i

        max_left = height[0]
        for i in range(max_height):
            if height[i]<max_left:
                result+=(max_left-height[i])
            else:
                max_left = height[i]

        max_right = height[-1]

        for i in range(len(height)-1, max_height, -1):
            if height[i]<max_right:
                result+=(max_right-height[i])

            else:
                max_right=height[i]

        
        return result
