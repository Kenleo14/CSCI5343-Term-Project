class Solution:
    def kthSmallest(self, mat, k):
        """
        Return the kth smallest array sum among all possible arrays formed by choosing one element per row.
        """
        import heapq
        rows = len(mat)
        pq = [(sum(row[0] for row in mat), [0] * rows)]
        visited = set(tuple([0] * rows))
        
        for _ in range(k):
            val, indices = heapq.heappop(pq)
            for i in range(rows):
                new_indices = indices[:]
                if new_indices[i] + 1 < len(mat[i]):
                    new_indices[i] += 1
                    new_val = val + mat[i][new_indices[i]] - mat[i][new_indices[i] - 1]
                    if tuple(new_indices) not in visited:
                        heapq.heappush(pq, (new_val, new_indices))
                        visited.add(tuple(new_indices))
        return val