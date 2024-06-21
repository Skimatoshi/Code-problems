class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:

        # So we are creating a dictionary to store the values and index's
        prevMap = {} # val : index

        # We go through each number in the array
        for i, n in enumerate(nums):
            print(f"Index: {i} , Num: {n}")
            # To find the compliment we do this :
            diff = target - n

            # If diff is in the dictionary return a list
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
        return




solution = Solution()
print(solution.twoSum([2, 11, 7, 3, 5, 8], 12))

