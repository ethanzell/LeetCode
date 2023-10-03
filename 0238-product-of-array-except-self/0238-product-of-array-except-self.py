class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        p = 1
        nz = []
        for k in range(n):
            if nums[k] == 0:
                nz.append(k)
            else:
                p*=nums[k]

        if len(nz) >= 2:
            return [0 for _ in range(n)]
        elif len(nz) == 1:
            answer = [0 for _ in range(n)]
            answer[nz[0]] = p
            return answer

        answer = [p for _ in range(n)]
        
        for k in range(n):
            answer[k] /= nums[k]

        return [int(k) for k in answer]