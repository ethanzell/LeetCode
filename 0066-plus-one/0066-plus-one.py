class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = [str(k) for k in digits]
        num = ''.join(digits)
        num = int(num)
        num += 1
        digits = list(str(num))
        digits = [int(k) for k in digits]
        return digits
        