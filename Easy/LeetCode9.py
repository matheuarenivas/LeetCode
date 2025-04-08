class Solution:
    def isPalindrome(self, x: int) -> bool:
        x1 = str(x)
        left_ptr = 0
        right_ptr = len(x1) - 1

        if x < 0:
            return False

        while left_ptr < right_ptr:
            if x1[left_ptr] == x1[right_ptr]:
                left_ptr+=1
                right_ptr-=1
                continue
            else:
                return False
        return True

s=Solution()
print(s.isPalindrome(123))