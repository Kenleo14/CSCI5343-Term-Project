class Solution:
    def nextGreatestLetter(self, letters, target):
        """
        Return the smallest character in letters that is lexicographically greater than target.
        If no such character exists, return the first character in letters.
        """
        left, right = 0, len(letters) - 1
        while left <= right:
            mid = (left + right) // 2
            if letters[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1
        return letters[left % len(letters)]