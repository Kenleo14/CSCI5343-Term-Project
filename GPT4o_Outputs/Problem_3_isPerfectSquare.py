class Solution:
    def isPerfectSquare(self, num):
        """
        Check if a given number is a perfect square.
        Do not use built-in square root functions.
        """
        left, right = 1, num
        while left <= right:
            mid = (left + right) // 2
            if mid * mid == num:
                return True
            elif mid * mid < num:
                left = mid + 1
            else:
                right = mid - 1
        return False