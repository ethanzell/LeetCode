class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if len(nums) < 2:
            if (sum(nums) > target):
                return 1
            else:
                return 0
        else:
            ws = nums[0]
        i=0
        j=0
        min_w_len = 999999
        while j < len(nums):
            if ws >= target:
                if j == i:
                    return 1
                elif min_w_len > j-i+1:
                    min_w_len = j-i+1
                ws -= nums[i]
                i += 1
            else:
                j+=1
                if j < len(nums):
                    ws += nums[j]
        if (j == len(nums)) and (i==0):
            return 0
        else:
            return min_w_len