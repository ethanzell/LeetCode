class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i=2
        end = len(nums)-1
        while i<=end:
            if (nums[i] == nums[i-1]) and (nums[i-1] == nums[i-2]):
                nums.pop(i)
                end-=1
            else:
                i+=1
        k=len(nums)
        