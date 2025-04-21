class Solution:
    def mySqrt(self, x):
        """
        Compute the square root of x rounded down to the nearest integer without using built-in functions.
        """
        left, right = 0, x
        while left <= right:
            mid = (left + right) // 2
            if mid * mid <= x < (mid + 1) * (mid + 1):
                return mid
            elif mid * mid < x:
                left = mid + 1
            else:
                right = mid - 1