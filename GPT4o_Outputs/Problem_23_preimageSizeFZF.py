class Solution:
    def preimageSizeFZF(self, k):
        """
        Return the number of non-negative integers x such that f(x) = k.
        """
        def zeta(x):
            return 0 if x == 0 else x // 5 + zeta(x // 5)
        
        def x_has_k(k):
            left, right = 0, 5 * k
            while left <= right:
                mid = (left + right) // 2
                if zeta(mid) < k:
                    left = mid + 1
                else:
                    right = mid - 1
            return left
        
        return x_has_k(k + 1) - x_has_k(k)