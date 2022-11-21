# Problem Description:
# A valid parentheses string is either empty "", "(" + A + ")", or A + B, 
# where A and B are valid parentheses strings, and + represents string concatenation.

# For example, "", "()", "(())()", and "(()(()))" are all valid parentheses strings.
# A valid parentheses string s is primitive if it is nonempty, and there does not 
# exist a way to split it into s = A + B, with A and B nonempty valid parentheses strings.

# Given a valid parentheses string s, consider its primitive decomposition: 
# s = P1 + P2 + ... + Pk, where Pi are primitive valid parentheses strings.

# Return s after removing the outermost parentheses of every primitive 
# string in the primitive decomposition of s.

# EXAMPLE:
# Input: s = "(()())(())"
# Output: "()()()"
# Explanation: 
# The input string is "(()())(())", with primitive decomposition "(()())" + "(())".
# After removing outer parentheses of each part, this is "()()" + "()" = "()()()".

def removebrackets(s):
    stack = []
    
    for bracket in s:
        if not stack:
            stack.append(bracket)
            
        elif stack[-1] == bracket:
            stack.pop(-1)
            stack.append(bracket)
            
        else:
            stack.append(bracket)
        
    return "".join(stack)
        
print(removebrackets("(()())(())(()(()))"))