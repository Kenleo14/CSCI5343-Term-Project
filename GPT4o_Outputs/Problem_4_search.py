class Solution:
    def search(self, nums, target):
        """
        Given an array of integers nums sorted in ascending order, and an integer target,
        return the index of target if it exists in nums, otherwise return -1.
        The algorithm must have O(log n) runtime complexity.
        """
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1