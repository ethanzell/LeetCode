class Solution:
    def reverseWords(self, s: str) -> str:
        l = s.strip(' ').split(' ')
        l = l[::-1]
        l = [m.strip(' ') for m in l]
        l = list(filter(lambda a: a != '', l))
        return ' '.join(l)
        