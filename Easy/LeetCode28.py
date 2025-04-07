class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        if needle not in haystack: 
            return -1
        n=len(needle) 
        start=0
        end=n
        while end<=len(haystack):
            if haystack[start:end]==needle: 
                return start 
            start+=1
            end+=1
      
        

s=Solution()
print(s.strStr("hello","ll"))   