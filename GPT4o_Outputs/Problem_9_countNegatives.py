class Solution:
    def countNegatives(self, grid):
        """
        Given a m x n matrix grid which is sorted in non-increasing order both row-wise and column-wise,
        return the number of negative numbers in grid.
        """
        count = 0
        for row in grid:
            left, right = 0, len(row) - 1
            while left <= right:
                mid = (left + right) // 2
                if row[mid] < 0:
                    right = mid - 1
                else:
                    left = mid + 1
            count += len(row) - left
        return count