class Solution:
    def maxArea(self, height: List[int]) -> int:
        n=len(height)
        i=0
        j=n-1
        mm = 0
        while i<=j:
            minh = min(height[i],height[j])
            ca = minh*(j-i)
            if ca >= mm:
                mm = ca
            if height[i]<height[j]:
                i+=1
            else:
                j-=1 
        return mm    