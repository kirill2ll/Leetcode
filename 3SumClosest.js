// https://leetcode.com/problems/3sum-closest/submissions/1778393318/

var threeSumClosest = function (nums, target) {
  let currentClosest = Number.MAX_SAFE_INTEGER;
  nums.sort((a, b) => a - b);

  for (let i = 0; i < nums.length; i++) {
    let left = i + 1;
    let right = nums.length - 1;

    while (left < right) {
        let currentSum = nums[i] + nums[left] + nums[right];

        if(Math.abs(target - currentSum) < Math.abs(target - currentClosest)){
            currentClosest = currentSum;
        }

        if (currentSum < target){
            left++;
        } else {
            right--;
        }
    }
  }
  return currentClosest;
};

console.log(threeSumClosest([-1, 2, 1, -4], 1));
