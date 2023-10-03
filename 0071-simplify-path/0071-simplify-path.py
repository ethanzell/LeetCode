class Solution:
    def simplifyPath(self, path: str) -> str:
        path_list = path.split('/')
        stack = []
        
        for string in path_list:
            if string == '':
                pass
            elif string == '.':
                pass
            elif string == '..':
                if len(stack) > 0:
                    stack.pop()
                else:
                    pass
            else:
                stack.append(string)
        
        
        if len(stack) > 0:
            result = ''
            for k in range(len(stack)):
                result = result + '/' + stack[k]
        else:
            result = '/'
        
        return result     