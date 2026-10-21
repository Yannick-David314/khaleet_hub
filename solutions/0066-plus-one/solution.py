class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        length = len(digits) - 1
        loop = length + 1
        number = 0
        for i in range(loop):
            number += digits[i] * pow(10, length - i)
        number += 1
        tbr = []
        while number:
            digit = number % 10
            tbr.append(digit)
            number = number // 10
        left = 0
        right = len(tbr) - 1
        while left < right:
            tbr[left], tbr[right] = tbr[right], tbr[left]
            left += 1
            right -= 1

        return tbr



        return digits

        