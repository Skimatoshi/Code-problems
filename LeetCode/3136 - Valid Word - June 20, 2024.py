class Solution:
    def isValid(self, word: str) -> bool:

        if len(word) < 3:
            return False

        vowels = 'aeiou'
        consonants = 'bcdfghjklmnpqrstvwxyz'

        # Consonant and Vowel count
        c, v = 0, 0

        # isalnum() , checks if it contains both numbers and words
        # Condition : Will run only if True
        if word.isalnum():
            word = word.lower()  # To handle case-insensitive comparisons

            # For each character in word
            for char in word:
                if char in vowels:
                    c += 1
                elif char in consonants:
                    v += 1

                # By default, 0 is used to represent False
                if c and v:
                    return True

        return False

solution = Solution()
print(solution.isValid('123Adis'))