class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # STEP 1
        toswap = len(nums) - 2
        while toswap >= 0 and nums[toswap] >= nums[toswap + 1]:
            toswap -= 1
        pivot = toswap

        # STEP 2
        if pivot >= 0:
            test = len(nums) - 1
            while nums[test] <= nums[pivot]:
                test -= 1
            nums[pivot], nums[test] = nums[test], nums[pivot]

        # STEP 3
        nums[pivot + 1:] = nums[pivot + 1:][::-1]



        

                                
