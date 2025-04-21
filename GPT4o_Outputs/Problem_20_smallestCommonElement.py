class Solution:
    def smallestCommonElement(self, mat):
        """
        Return the smallest common element in all rows of the given matrix, or -1 if none exist.
        """
        from collections import Counter
        counter = Counter()
        
        for row in mat:
            for num in row:
                counter[num] += 1
                if counter[num] == len(mat):
                    return num
        return -1