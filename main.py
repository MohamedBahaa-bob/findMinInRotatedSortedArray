# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def recursiveMin(start, end, nums):
    if start == end:
        return nums[start]
    if end - start == 1:
        return min(nums[start], nums[end])
    median = int((start + end)/2)
    if nums[median] < nums[median - 1]:
        return nums[median]
    if nums[median] > nums[median + 1]:
        return nums[median + 1]
    if nums[median] > nums[end]:
        return recursiveMin(median + 1, end, nums)
    else:
        return recursiveMin(start, median - 1, nums)


class Solution:
    def findMin(self, nums) -> int:
        return recursiveMin(0, len(nums) - 1, nums)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    obj = Solution()
    print(obj.findMin([18, 13, 15, 17]))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
