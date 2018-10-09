class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        num = 0
        for i in range(len(digits)):
            num += digits[i] * pow(10, len(digits) - 1 - i)

        num += 1

        return [int(j) for j in str(num)]
        # for i in str(num):
            # print int(i)

plusing = Solution()

a = [1, 2, 3, 4]

print(plusing.plusOne(a))