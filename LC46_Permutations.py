class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        output = []

        def backtrack(first=0):
            if first == n:
                output.append(nums[:])

            for i in range(first, n):
                nums[i], nums[first] = nums[first], nums[i]
                backtrack(first+1)
                nums[i], nums[first] = nums[first], nums[i]



        n = len(nums)
        backtrack()
        return output
