class Solution:
    def isMajorityElement(self, nums, target):
        """
        Return true if target is a majority element in nums, otherwise return false.
        A majority element in nums is an element that appears more than nums.length / 2 times.
        """
        n = len(nums)
        left = 0
        right = n - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                # Check if target is a majority element
                count = nums.count(target)
                return count > n // 2
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False