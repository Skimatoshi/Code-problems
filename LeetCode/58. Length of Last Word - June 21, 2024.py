class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        x = []

        for str in s.split():
            x.append(str)

        return len(x[-1])


    # or
    '''
    x = s.split()
        return len(x[-1])
    
    第二個想到的 solution
    '''