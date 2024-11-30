class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for ele in s:
            if ele == '(' or ele == '{' or ele =='[':
                stack.append(ele)
            else:
                if not stack:
                    return False
                top = stack.pop()
                if (
                    (top == '(' and ele != ')') or
                    (top == '{' and ele != '}') or
                    (top == '[' and ele != ']')
                ):
                    return False
        return not stack

                