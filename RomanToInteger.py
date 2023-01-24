class Solution:
    def romanToInt(self, s: str) -> int:
        converter = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
        N = len(s)
        i = N-1
        output = 0

        while i >= 0:
            if i < N-1 and converter[s[i]] < converter[s[i+1]]:
                output -= converter[s[i]]
            else:
                output += converter[s[i]]
            i -= 1
        return output
