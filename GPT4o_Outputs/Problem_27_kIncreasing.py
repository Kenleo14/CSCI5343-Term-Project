class Solution:
    def kIncreasing(self, arr, k):
        """
        Return the minimum number of operations required to make the array K-increasing.
        """
        from bisect import bisect_right
        
        def lis_length(subseq):
            lis = []
            for x in subseq:
                pos = bisect_right(lis, x)
                if pos == len(lis):
                    lis.append(x)
                else:
                    lis[pos] = x
            return len(lis)
        
        n = len(arr)
        result = 0
        for i in range(k):
            subseq = [arr[j] for j in range(i, n, k)]
            result += len(subseq) - lis_length(subseq)
        return result