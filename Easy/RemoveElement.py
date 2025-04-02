# https://leetcode.com/problems/remove-element/
# Two pointer technique
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        i = 0
        j = len(nums)
        k = 0

        while i < j:
            if nums[i] == val:
                nums[i] = nums[j-1]
                j-=1 
            else:
                i +=1
        return j

# Example usage:
solution = Solution()
nums = [3, 2, 2, 3]
val = 3
result = solution.removeElement(nums, val)
print(result)  # Output: 2

# Example usage:
solution = Solution()
nums = [0,1,2,2,3,0,4,2]
val = 2
result = solution.removeElement(nums, val)
print(result)  # Output: 5

