class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        workspace = []
        while x:
            workspace.append(x % 10)
            x //= 10
        left = 0
        right = len(workspace) - 1
        while left < right:
            if workspace[left] != workspace[right]:
                return False
            left += 1
            right -= 1
        return True
        