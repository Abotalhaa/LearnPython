class Solution:
    def containsDuplicate(self, nums):
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False

ob1 = Solution()
print(ob1.containsDuplicate([1, 3, 4, 6, 5, 10]))
