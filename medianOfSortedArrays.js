//https://leetcode.com/problems/median-of-two-sorted-arrays/description/

/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */
var findMedianSortedArrays = function (nums1, nums2) {
  let median = nums1.length + nums2.length;

  let needTwoNumbers = false;

  if (median % 2 === 0) {
    //even, it means we need 2 numbers
    needTwoNumbers = true;
    median /= 2;
  } else {
    //number with remainder, means we need only one number
    median /= 2;
    median = Math.round(median);
  }
  median -= 1;

  let currentPosition = 0;
  let firstArrPosition = 0;
  let secondArrPosition = 0;

  let isFound = false;
  const outputNumbers = [];

  while (!isFound) {
    let firstArrNum =
      firstArrPosition < nums1.length
        ? nums1[firstArrPosition]
        : Number.MAX_SAFE_INTEGER;
    let secondArrNum =
      secondArrPosition < nums2.length
        ? nums2[secondArrPosition]
        : Number.MAX_SAFE_INTEGER;

    if (currentPosition === median) {
      if (needTwoNumbers) {
        median++;
      } else {
        outputNumbers.push(0);
      }
      const currentNumber = Math.min(firstArrNum, secondArrNum);
      outputNumbers.push(currentNumber);

      if (outputNumbers.length === 2) isFound = true;
    }

    if (firstArrNum <= secondArrNum) {
      firstArrPosition++;
    } else {
      secondArrPosition++;
    }

    currentPosition++;
  }

  let outputNumber = outputNumbers.reduce((a, b) => a + b, 0);
  if (needTwoNumbers) outputNumber /= 2;

  return outputNumber;
};

console.log(findMedianSortedArrays([], [1, 2, 3, 4, 5, 6]));
