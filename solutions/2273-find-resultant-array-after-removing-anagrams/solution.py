class Solution:
    def removeAnagrams(self, words: list[str]) -> list[str]:
        lst = []
        left = 0
        right = 1
        length = len(words)
        sort_left = sorted(words[left])
        while right < length:
            sort_right = sorted(words[right])
            isAnag = sort_left == sort_right
            if not isAnag:
                lst.append(words[left])
                left = right
                sort_left = sort_right
            right += 1
        return lst + [words[left]]


        