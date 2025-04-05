class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        index = 0
        count = 0

        hash_count = {}
        for char in magazine:
            if char in hash_count:
                hash_count[char] += 1
            else:
                hash_count[char] = 1


        for char in ransomNote:
            if char in hash_count and hash_count[char] > 0:
                hash_count[char] -= 1
                continue
            if char not in hash_count or hash_count[char] == 0:
                return False
        return True
    
solution = Solution()
print(solution.canConstruct("a", "b"))
print(solution.canConstruct("aa", "ab"))
print(solution.canConstruct("aa", "aab"))
