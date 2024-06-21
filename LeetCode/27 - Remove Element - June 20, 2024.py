class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:

        list_count = []

        for i in nums:
            if i != val:
                list_count.append(i)

        return len(list_count)




solution = Solution()
print(solution.removeElement([0,1,2,2,3,0,4,2], 2))



