class Solution:
    def maximizeSweetness(self, sweetness, k):
        """
        Return the maximum total sweetness of the piece you can get by cutting the chocolate bar optimally.
        """
        left, right = 1, sum(sweetness) // (k + 1)
        
        def can_divide(mid):
            pieces, total = 0, 0
            for s in sweetness:
                total += s
                if total >= mid:
                    pieces += 1
                    total = 0
            return pieces >= k + 1
        
        while left < right:
            mid = (left + right + 1) // 2
            if can_divide(mid):
                left = mid
            else:
                right = mid - 1
        return left