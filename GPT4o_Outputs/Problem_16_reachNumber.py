class Solution:
    def reachNumber(self, target):
        """
        Find the minimum number of moves to reach the target.
        """
        target = abs(target)
        step = 0
        total = 0
        while total < target or (total - target) % 2 != 0:
            step += 1
            total += step
        return step