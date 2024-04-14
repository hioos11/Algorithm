'''
https://leetcode.com/problems/valid-parentheses/description/

1. 주어진 문자열을 하나씩 스택에 넣는다.

2. 현재 괄호가 닫는 괄호인 경우 현재까지 쌓인 스택의 top을 확인한다.

3. 현재 대상 괄호와 top의 괄호가 안 쌍이면 top을 pop해준다.

4. 만약 pop을 할 수 없는 괄호라면 invalid로 판단한다.

5. 모든 괄호를 다 사용했을 때 현재 남아있는 stack이 비어있어야 한다.
남아있지 않다면 invalid로 판단.
'''

# 내가 짠 코드
# 시간 복잡도는 O(n)
# 리트코드 결과
# https://leetcode.com/problems/valid-parentheses/submissions/1230859487
# 16초, 11.88메모리
class Solution(object):
    
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        open = ['(', '{', '[']
        close = [')', '}', ']']

        stack = []
        for p in s:
            if p in open:
                stack.append(p)
            else:
                # 닫는 괄호가 먼저 나온 경우를 고려하지 못함
                if len(stack) == 0:
                    return False
                popP = stack.pop()
                openIdx = open.index(popP)
                closeIdx = close.index(p)

                if closeIdx != openIdx:
                    return False
        # 스택에 남아있는 경우에는 false 
        if len(stack) != 0:
            return False        
        return True 


sol = Solution()

# print(sol.isValid("()"))
# print(sol.isValid("()[]{}"))
print(sol.isValid("(]"))


# 강의 코드
# 리트코드 결과 https://leetcode.com/problems/valid-parentheses/submissions/1230863892
# 14초, 11.84메모리
def isValid(s):
    stack = []
    for p in s:
        if p == '(':
            stack.append(')')
        elif p == '{':
            stack.append('}')
        elif p == '[':
            stack.append("]")
        elif not stack or stack.pop() != p:
            # not stack : 스택이 비어있지 않은지
            return False
    return not stack