class Solution:
    def arraysIntersection(self, arr1, arr2, arr3):
        """
        Given three integer arrays arr1, arr2, and arr3 sorted in strictly increasing order,
        return a sorted array of only the integers that appeared in all three arrays.
        """
        p1, p2, p3 = 0, 0, 0
        result = []
        while p1 < len(arr1) and p2 < len(arr2) and p3 < len(arr3):
            if arr1[p1] == arr2[p2] == arr3[p3]:
                result.append(arr1[p1])
                p1 += 1
                p2 += 1
                p3 += 1
            else:
                if arr1[p1] < arr2[p2]:
                    p1 += 1
                elif arr2[p2] < arr3[p3]:
                    p2 += 1
                else:
                    p3 += 1
        return result