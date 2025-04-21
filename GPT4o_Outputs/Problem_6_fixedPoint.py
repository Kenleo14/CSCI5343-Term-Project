class Solution:
    def fixedPoint(self, arr):
        """
        Given an array of distinct integers arr sorted in ascending order,
        return the smallest index i that satisfies arr[i] == i. If no such index exists, return -1.
        """
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == mid:
                return mid
            elif arr[mid] < mid:
                left = mid + 1
            else:
                right = mid - 1
        return -1