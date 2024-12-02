class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        dic={')': '(', '}':'{',']': '['}
        
        for ele in s:
            if ele in dic:
                if stack and stack[-1] == dic[ele]:
                    stack.pop()
                else:
                    return False    
            else:
                stack.append(ele)
                        
        return not stack
                
                