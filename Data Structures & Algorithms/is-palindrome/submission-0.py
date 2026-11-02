class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = "".join(char for char in s if char.isalnum())

        for i in range(len(s) // 2):
            first_char = s[len(s) - i - 1]
            last_char = s[i]

            if first_char != last_char:
                return False

        return True