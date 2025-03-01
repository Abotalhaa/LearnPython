"""
https://leetcode.com/problems/two-sum

# Write a function takes list & target number
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

# Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

# Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

# Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]

Constraints:
2 <= nums.length <= 10ˆ4
-10ˆ9 <= nums[i] <= 10ˆ9
-10ˆ9 <= target <= 10ˆ9
Only one valid answer exists.
"""


def twoSum(nums: [int], target: int) -> [int]:
    for i in range(len(nums)):  # O(n) #4
        for j in range(i + 1, len(nums)):  # O(n)
            if nums[i] + nums[j] == target:  # O(1)
                return [i, j]


print(twoSum([2, 7, 11, 15], 9))

