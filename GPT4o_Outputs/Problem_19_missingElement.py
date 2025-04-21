class Solution:
    def missingElement(self, nums, k):
        """
        Given a sorted array nums and an integer k, return the kth missing number starting from the leftmost number.
        """
        missing = lambda idx: nums[idx] - nums[0] - idx
        n = len(nums)
        
        if k > missing(n - 1):
            return nums[-1] + k - missing(n - 1)

        left, right = 0, n - 1
        while left < right:
            mid = (left + right) // 2
            if missing(mid) < k:
                left = mid + 1
            else:
                right = mid
        return nums[left - 1] + k - missing(left - 1)