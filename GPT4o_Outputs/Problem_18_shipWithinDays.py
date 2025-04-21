class Solution:
    def shipWithinDays(self, weights, days):
        """
        Find the minimum capacity of a ship to deliver packages within days.
        """
        left, right = max(weights), sum(weights)
        while left < right:
            mid = (left + right) // 2
            current, required_days = 0, 1
            for weight in weights:
                if current + weight > mid:
                    required_days += 1
                    current = 0
                current += weight
            if required_days > days:
                left = mid + 1
            else:
                right = mid
        return left