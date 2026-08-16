class Solution:
    def isPalindrome(self, s:int) -> bool:
        lowercase_s = "".join(char.lower() for char in s if char.isalnum())
        left = 0
        right = len(lowercase_s) - 1

        while left < right:
            if lowercase_s[left] != lowercase_s[right]:
                return False
            left += 1
            right -= 1
        
        return True




