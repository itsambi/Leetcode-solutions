class Solution(object):
    def romanToInt(self, s):
        
        roman = {
            'I': 1, 'V': 5, 'X': 10,
            'L': 50, 'C': 100,
            'D': 500, 'M': 1000
        }

        total = 0
        i = 0
        n = len(s)

        while i < n:
            curr = roman[s[i]]
            if i + 1 < n and curr < roman[s[i + 1]]:
                total += roman[s[i + 1]] - curr
                i += 2
            else:
                total += curr
                i += 1

        return total