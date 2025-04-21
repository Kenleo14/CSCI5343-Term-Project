class Solution:
    def findKthNumber(self, m, n, k):
        """
        Return the kth smallest number in the m x n multiplication table.
        """
        def enough(x):
            count = 0
            for i in range(1, m + 1):
                count += min(x // i, n)
            return count >= k
        
        left, right = 1, m * n
        while left < right:
            mid = (left + right) // 2
            if enough(mid):
                right = mid
            else:
                left = mid + 1
        return left