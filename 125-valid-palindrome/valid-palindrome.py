class Solution(object):
    def isPalindrome(self, s):
        result=""
        for i in s:
            if i.isalnum():
                result+=i
        result=result.lower()
        return result==result[::-1]
        