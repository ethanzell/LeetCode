from copy import copy
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone_dict = {'2':['a','b','c'], '3':['d','e','f'], '4': ['g','h','i'], '5': ['j','k','l'], 
                     '6': ['m','n','o'], '7': ['p','q','r','s'], '8': ['t','u','v'], '9': ['w','x','y','z']}
        
        output = []
           
        i = 0
        while i < len(digits):
            new_output = []
            if i == 0:
                for c in phone_dict[digits[i]]:
                    new_output.append(c)
            else: 
                for pre_out in output:
                    for c in phone_dict[digits[i]]:
                        new_output.append(pre_out + c)
            i+=1
            #print(output,new_output)
            output = copy(new_output)
            
        return output