class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        i = 0  # counting the loop
        zero_num = 0  # counting the number of zeros
        while (i + zero_num) < len(nums):
            nums[i] = nums[i + zero_num]
            if nums[i] == 0:
                zero_num += 1
                i -= 1

            i += 1

        nums[-zero_num:] = [0] * zero_num

    def optimalMove(self, nums):
        """

        :param nums: List[int]
        :return:
        """
        lastnonzero = 0
        for cur in range(len(nums)):
            if nums[cur] != 0:
                nums[cur], nums[lastnonzero] = nums[lastnonzero], nums[cur]
                lastnonzero += 1




test = Solution()

x = [1, 0, 4, 0, 4, 0, 23, 0, 34, 0, 23]
print(x)

test.optimalMove(x)
print(x)