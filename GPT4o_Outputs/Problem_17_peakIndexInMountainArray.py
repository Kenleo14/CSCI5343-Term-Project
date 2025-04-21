class Solution:
    def peakIndexInMountainArray(self, arr):
        """
        Find the peak index in a mountain array.
        """
        left, right = 0, len(arr) - 1
        while left < right:
            mid = (left + right) // 2
            if arr[mid] > arr[mid + 1]:
                right = mid
            else:
                left = mid + 1
        return left