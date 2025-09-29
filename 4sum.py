# https://leetcode.com/problems/4sum/description/

from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        output = []
        nums.sort()

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, len(nums)):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                left = j + 1
                right = len(nums) - 1
                while left < right:
                    num1 = nums[i]
                    num2 = nums[j]
                    num3 = nums[left]
                    num4 = nums[right]
                    sum = num1 + num2 + num3 + num4
                    if(sum == target):
                        output.append([num1, num2, num3, num4])
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        left += 1
                        right -= 1
                    if sum < target:
                        left += 1
                    if sum > target:
                        right -= 1

        return output


s = Solution()
print(s.fourSum([1,0,-1,0,-2,2], 0))
print(s.fourSum([2,2,2,2,2], 8))
    