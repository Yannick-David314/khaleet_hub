class Solution:
    def findArray(self, pref: list[int]) -> list[int]:
        right = len(pref) - 1
        while right > 0:
            pref[right] = (pref[right] ^ pref[right - 1])
            right -= 1
        return pref


        