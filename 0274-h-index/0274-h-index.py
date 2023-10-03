class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n=len(citations)
        c = max(citations)

        c_list = [0 for _ in range(c+1)]

        for k in range(n):
            c_list[citations[k]]+=1

        for k in range(c,-1,-1):
            if sum(c_list[k:]) >= k:
                return k