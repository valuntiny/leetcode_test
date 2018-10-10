class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        for i in range(len(nums)):
            try:
                if nums.index(target - nums[i]) != i:
                    return (i, nums.index(target - nums[i]))
            except:
                ()


test = Solution()

print(test.twoSum([-1,-2,-3,-4,-5], -8))