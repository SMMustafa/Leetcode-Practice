class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        count = 0
        total = {0: 1}
        running_sum = 0

        for i in nums:
            running_sum += i

            if running_sum-k in total:
                count+=total[running_sum-k]

            if running_sum in total:
                total[running_sum]+=1
            else:
                total[running_sum]=1

        return count
