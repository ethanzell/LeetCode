class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        l = s.strip(' ').split(' ')
        for k in range(len(l)-1,-1,-1):
            if ' ' not in l[k]:
                return len(l[k])
        