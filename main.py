class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:

        my_map = {}

        for i, n in enumerate(nums):
            diff = target - n

            if diff in my_map:
                return [my_map[diff], i]
            my_map[n] = i



solution = Solution()
print(solution.twoSum([1, 2, 3, 4], 8))
