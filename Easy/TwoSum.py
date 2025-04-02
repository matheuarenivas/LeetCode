class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):               # Outer loop: Use indexes
            for j in range(i + 1, len(nums)):    # Inner loop: Avoid duplicates
                if nums[i] + nums[j] == target:  # Check if the sum matches
                 return [i, j]                # Return the indexes
        

# Test cases
solution = Solution()

# Test case 1: Basic case
nums = [2, 7, 11, 15]
target = 9
print(solution.twoSum(nums, target))  # Output: [0, 1]

# Test case 2: Negative numbers
nums = [-3, 4, 3, 90]
target = 0
print(solution.twoSum(nums, target))  # Output: [0, 2]