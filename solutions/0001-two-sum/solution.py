class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        my_dict = {}
        for i in range(len(nums)):
            if target - nums[i] in my_dict:
                return [i, my_dict[target - nums[i]]]
            my_dict[nums[i]] = i
        return None
        