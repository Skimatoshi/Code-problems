class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:

        # if target not in nums:
        #     nums.append(target)
        #     nums.sort()
        #
        # for i, n in enumerate(nums):
        #     if target == n:
        #         return i

        # binary search solution

        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2

            if target == nums[mid]:
                return mid
            if target > nums[mid]:
                l = mid + 1
            else:
                r = mid - 1

        return l


solution = Solution()
print(solution.searchInsert([13, 14, 17, 19], 15))
