class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:

        my_string = "".join(str(n) for n in digits)
        x = int(my_string) + 1

        new_list = [int(n) for n in str(x)]
        return new_list




solution = Solution()
print(solution.plusOne([0]))
