class Solution:
    def leftmostBuildingQueries(self, heights, queries):
        """
        For each query, find the leftmost building where Alice and Bob can meet.
        Return -1 if Alice and Bob cannot meet in any building.
        """
        results = []
        for ai, bi in queries:
            leftmost = float('inf')
            for i in range(ai + 1, len(heights)):
                if heights[ai] < heights[i] and heights[bi] < heights[i]:
                    leftmost = min(leftmost, i)
            results.append(leftmost if leftmost != float('inf') else -1)
        return results