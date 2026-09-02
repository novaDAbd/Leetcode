class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        result = ""
        
        for char in s:
            if char.isalnum():
                result += char

        s_ = result[::-1]

        if s_ == result:
            return True
        else:
            return False