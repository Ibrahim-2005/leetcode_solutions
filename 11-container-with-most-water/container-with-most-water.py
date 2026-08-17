class Solution(object):
    def maxArea(self, height):
        left, right= 0, len(height)-1
        maxwater=0
        while left<right:
            current=min(height[left],height[right])
            maxwater=max(current*(right-left),maxwater)
            if current==height[left]:
                left+=1
            else:
                right-=1
        return maxwater
            