"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"

Output: true

Example 2:

Input: s = "()[]{}"

Output: true

Example 3:

Input: s = "(]"

Output: false

Example 4:

Input: s = "([])"

Output: true

 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""

class Solution(object):      
      def isValid(self, s):                          #time complexity = O(n) because you iterate through the string once, n number of times
        """
        :type s: str
        :rtype: bool
        """
        stack = []                                   #space complexity = should be O(n/2) because you only stack the open brackets, 
        close = {")": "(",                           #but worst case scenario would be O(n) for strings with only close brackets
                 "}": "{",
                 "]": "["}
        for bracket in s:                            #for each bracket in the string
            if bracket not in close:                 #if it's an open bracket
                stack.append(bracket)                #push open bracket in stack
            else:                                    #otherwise since it is a close bracket
                if len(stack) == 0:                  #if there is nothing in the stack
                    return False                     #first bracket is a close bracket, so it automatically fails
                if close[bracket] != stack.pop():    #if the open bracket that is mapped to that closing bracket is the same as 
                    return False                     # the open bracket at the top of your stack it should fail
        return len(stack) == 0                       #since it hasnt failed yet, it must be true

        
