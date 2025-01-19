"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters if it is non-empty.
"""

class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""

        min_length = min(len(s) for s in strs)

        i = 0
        while i < min_length:
            for s in strs:
                if s[i] != strs[0][i]:
                    return strs[0][:i]
            i += 1

        return strs[0][:i]

