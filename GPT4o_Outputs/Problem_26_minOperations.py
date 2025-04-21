class Solution:
    def minOperations(self, nums):
        """
        Return the minimum number of operations to make nums continuous.
        """
        nums = sorted(set(nums))
        n = len(nums)
        max_window = 0
        
        for start in range(n):
            end = start
            while end < n and nums[end] - nums[start] < len(nums):
                end += 1
            max_window = max(max_window, end - start)
        return len(nums) - max_window