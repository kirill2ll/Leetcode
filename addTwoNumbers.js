//https://leetcode.com/problems/add-two-numbers/description/

function ListNode(val, next) {
  this.val = val === undefined ? 0 : val;
  this.next = next === undefined ? null : next;
}

/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
var addTwoNumbers = function (l1, l2) {
  //function listNode to Array
  let listNodeToArray = (listNode) => {
    const arrToReturn = [];
    let currentNode = listNode;

    while (currentNode != null) {
      arrToReturn.push(currentNode.val);
      currentNode = listNode.next;
      listNode = listNode.next;
    }

    return arrToReturn;
  };
  const l1Array = listNodeToArray(l1);
  const l2Array = listNodeToArray(l2);

  const longestList = l1Array.length >= l2Array.length ? l1Array : l2Array;
  const shortestList = l1Array.length >= l2Array.length ? l2Array : l1Array;
  let outputList = [];
  let remainder = 0;

  for (let i = 0; i < longestList.length; i++) {
    if (shortestList[i] == undefined) shortestList[i] = 0;

    let result = shortestList[i] + longestList[i] + remainder;

    //reset the remainder
    remainder = 0;
    if (result >= 10) (result -= 10), (remainder = 1);

    outputList.push(result);
  }

  if ((remainder == 1)) outputList.push(remainder);
  console.log(outputList);
  //   const remainderArr = longestList.slice(shortestList.length);
  //   outputList = [...outputList, ...remainderArr];

  //function Arr to listNode
  const arrToListNode = (arr) => {
    let listNode = null;

    for (let i = arr.length - 1; i >= 0; i--) {
      listNode = new ListNode(arr[i], listNode);
    }
    return listNode;
  };

  return arrToListNode(outputList);
};

//function Arr to listNode
const arrToListNode = (arr) => {
  let listNode = null;

  for (let i = arr.length - 1; i >= 0; i--) {
    listNode = new ListNode(arr[i], listNode);
  }
  return listNode;
};

const test = addTwoNumbers(
  arrToListNode([2,4,3]),
  arrToListNode([5,6,4])
);
console.log(test);
