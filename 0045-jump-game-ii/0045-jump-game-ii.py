class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        jumps = [n for _ in range(n)]
        jumps[0] = 0

        for i in range(n):
            for j in range(nums[i]+1):
                if i+j < n:
                    jumps[i+j] = min(jumps[i+j], jumps[i]+1)
        return jumps[-1]