import math

class Solution:
    def maxGcdSum(self, nums, k):
        """
        Find the maximum gcd-sum of a subarray of nums with at least k elements.
        """
        def gcd_sum(arr):
            g = math.gcd(*arr)
            return g * sum(arr)
        
        max_sum = 0
        n = len(nums)
        for i in range(n):
            for j in range(i + k, n + 1):
                max_sum = max(max_sum, gcd_sum(nums[i:j]))
        return max_sum