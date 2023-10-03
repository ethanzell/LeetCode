class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n=len(nums)
        if n <= 1:
            return True
        if sum(nums)+1 < n:
            return False
        
        reach = [False for _ in range(n)]
        reach[0] = True

        for i in range(n):
            if reach[i]:
                for j in range(1, nums[i]+1):
                    if i+j < n:
                        reach[i+j] = True
                    if i+j==n-1:
                        return True
        return reach[n-1]