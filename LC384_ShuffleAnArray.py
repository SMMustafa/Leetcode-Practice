from random import choice
class Solution:

    def __init__(self, nums: List[int]):
        self.arr = nums
        self.original = list(nums)


    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        self.arr=self.original
        self.original= list(self.original)

        return self.arr

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        for i in range(len(self.arr)):
            swap_index = random.randrange(i, len(self.arr))
            self.arr[i], self.arr[swap_index]= self.arr[swap_index], self.arr[i]
        return self.arr





# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
