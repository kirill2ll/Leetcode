# https://leetcode.com/problems/3sum/description/

from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        nums.sort()
        target = 0

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left = i + 1
            right = len(nums) - 1
            while left < right:
                num1 =nums[i]
                num2 = nums[left]
                num3 = nums[right]
                sum = num1 + num2 + num3
                if  sum == target:
                            output.append([num1, num2, num3])
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
print(s.threeSum([-1,0,1,2,-1,-4]))    #-5 -2 -1 0 2 5 10
print(s.threeSum([0,1,1]))
print(s.threeSum([0,0,0]))
print(s.threeSum([-2,0,0,2,2]))