//Longest Substring Without Repeating Characters
//https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function (s) {
  let maxRepeat = 0;
  let charSet = new Set();

  let currentRepeat = 0;
  let currentSubstring = "";

  const addCharsToSet = (str) => {
    let set = new Set();
    for (let ch of str) {
      set.add(ch);
    }

    return set;
  };

  for (let ch of s) {
    if (!charSet.has(ch)) {
      charSet.add(ch);
      currentSubstring += ch;
      currentRepeat++;
    } else {
      if (currentRepeat > maxRepeat) {
        maxRepeat = currentRepeat;
      }
      currentSubstring = currentSubstring.slice(
        currentSubstring.lastIndexOf(ch) + 1
      );
      currentRepeat = currentSubstring.length;
      charSet = addCharsToSet(currentSubstring);
      charSet.add(ch);
      currentSubstring += ch;
      currentRepeat++;
    }
  }

  if (currentRepeat > maxRepeat) {
    maxRepeat = currentRepeat;
  }

  return maxRepeat;
};

console.log(lengthOfLongestSubstring("wwewawbc"));
