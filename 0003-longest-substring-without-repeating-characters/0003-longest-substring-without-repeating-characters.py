class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        stack = []
        l = len(stack)
        for c in s:
            while (c in stack):
                stack.pop(0)
            stack.append(c)
            l = max(l, len(stack))
        return l      