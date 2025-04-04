class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        string = s.lower()
        string_new = ""

        for c in string:
            if c.isalnum():
                string_new += c
        i = 0
        j = len(string_new) - 1

        while i < j:
            if string_new[i] == string_new[j]:
                i += 1
                j -= 1
            else:
                return False
        return True
    
solution = Solution()
print(solution.isPalindrome("A man, a plan, a canal: Panama"))
