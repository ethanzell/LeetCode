class Solution:
    def trailingZeroes(self, n: int) -> int:    
        if n == 0:
            return 0
        twos=0
        fives=0
        for k in range(1,n+1,1):
            temp2 = k
            temp5 = k
            while temp2 % 2 == 0:
                twos += 1
                temp2 /= 2
            while temp5 % 5 == 0:
                fives += 1
                temp5 /= 5 
        return min(twos, fives)


        