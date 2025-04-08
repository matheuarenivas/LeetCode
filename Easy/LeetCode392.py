class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        if s == None or "":
            return True
        index = 0    
        for i in range(len(t)):
            if index < len(s) and s[index] == t[i]:
                index+=1

        if index == len(s):
            return True  
        return False

solution = Solution()
print(solution.isSubsequence("abc", "ahbgdc")) 