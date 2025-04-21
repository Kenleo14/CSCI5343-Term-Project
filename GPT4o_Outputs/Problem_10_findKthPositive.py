class Solution:
    def findKthPositive(self, arr, k):
        """
        Find the kth missing positive integer from a sorted array.
        """
        missing = 0
        for i in range(1, arr[-1] + k + 1):
            if i not in arr:
                missing += 1
                if missing == k:
                    return i