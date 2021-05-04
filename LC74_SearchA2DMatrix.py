class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        m = len(matrix)
        n = len(matrix[0])


        left = 0
        right = m * n - 1

        #binary search
        while left <= right:
            pivot_idx = (left + right) // 2
            pivot_ele = matrix[pivot_idx // n][pivot_idx % n]
            if target == pivot_ele:
                return True
            elif pivot_ele < target:
                left = pivot_idx + 1
            else:
                right = pivot_idx - 1
        return False
