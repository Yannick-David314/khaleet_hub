class Solution:
    def convert(self, s: str, numRows: int) -> str:

        if numRows == 1:
            return s

        constant_sum = 2 * (numRows - 1)
        current = 0
        length = len(s) - 1
        result = []
        for i in range(numRows):
            current = i
            if i == 0 or i == numRows - 1:
                gap = constant_sum
            else:
                gap = 2 * (numRows - (i + 1)) 
            while current <= length:
                result.append(s[current])
                current += gap
                if i > 0 and numRows - 1 > i:
                    gap = constant_sum - gap
                else:
                    gap = constant_sum
        return (''.join(result))

        