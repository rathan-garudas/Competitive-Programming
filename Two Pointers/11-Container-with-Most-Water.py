class Solution:
    def maxArea(self, height: List[int]) -> int:
        if len(height)==0: return 0

        l,r=0,len(height)-1

        maxarea = 0

        while l<r:
            mini = min(height[l], height[r])
            area=(r-l)*mini

            maxarea = max(maxarea, area)

            if mini==height[l]:
                l+=1
            else:
                r-=1

        return maxarea