// // let S = 'abcabcbb'

// // function subString(S) {
// //     debugger;
// //     newStr = ' '
// //     for (let i = 0; i < S.length; i++){
// //         for (let j = 0; j < S.length; j++){
// //             if (S[i] !== S[j + 1]) {
// //                 newStr =  S[j + 1]
// //             }
// //         }
// //     }
// //     return newStr
// // }

// // console.log(subString(S))

// // L = [1, 2, 1, 6, 9, 4, 0, 1, 6, 2, 8, 1000, 1]

// // function frequentNum(L) {
// //     let obj = {}
// //     // iterate over each item
// //     //   run a nested loop
// //     for (let i = 0; i < L.length; i++){
// //         if (obj.hasOwnProperty(L[i])) {
// //             obj[L[i]] = 1
// //         } else {
// //             obj[L[i]] += 1
// //         }
// //     }
// //     return obj.keys()
// // }

// // num = [1, 1, 2]
// // output = 2

// // function removeDuplicates(num) {
// //     i = 0
// //     for (let j = 0; j < num.length; j++){
// //         if (num[i] !== num[j]){
// //             num[i + 1] = num[j]
// //             i++
// //         }
// //     }
// //     return i + 1
// // }

// // console.log(removeDuplicates(num))

// // let nums = [1,1,2]
// // const removeDuplicates = function (nums) {
// //     debugger;
// //     let i = 0
// //     for (let j = 0; j < nums.length; j++){
// //         if (nums[i] !== nums[j]) {
// //             nums[i + 1] = nums[j]
// //             i++
// //         }
// //     }
// // return i + 1
// // }

// // console.log(removeDuplicates(nums))

// // solved with O(n2) time complexity
// // var containsDuplicate = function (nums) {
// //     debugger;
// //     for (let i = 0; i < nums.length; i++){
// //         for (let j = 1; j < nums.length; j++){
// //             if (nums[i] === nums[j]) {
// //                 return true
// //             }
// //         }
// //         return false
// //     }
// // };

// // console.log(containsDuplicate(nums))

// // O(n)
// var containsDuplicate = function (nums) {
//   debugger;
//   let obj = {};
//   for (let i = 0; i < nums.length; i++) {
//     if (obj[nums[i]]) {
//       obj[nums[i]] += 1;
//     } else {
//       obj[nums[i]] = 1;
//     }
//   }
//   let values = Object.values(obj);

//   if (Math.max(...values) > 1) {
//     return true;
//   }
//   return false;
// };
// // console.log(containsDuplicate(nums))

// // let s = "race a car"

// // var isPalindrome = function (s) {
// //     let regularStr = s.replace(/[^a-z0-9]/gi, '').toLowerCase()
// //     let sortedStr =  s.replace(/[^a-z0-9]/gi, '').toLowerCase().split('').reverse().join('')
// //     if (regularStr === sortedStr) {
// //         return true
// //     }
// //    return false
// // };

// // console.log(isPalindrome(s))

// // let s = "anagram";
// let t = "nagaram";

// var isAnagram = function (s, t) {
//   sortS = s.split("").sort();
//   console.log(sortS);
//   sortT = t.split("").sort();
//   console.log(sortT);
//   return sortS === sortT ? true : false;
// };

// console.log(isAnagram(s));

// let x = 123

// var reverse = function(x) {
//   //  convert x into an array
//   // run a reverse for loop
//   // convert the array to string and then  integer
//   // return the result

//   console.log(Array.from(x))

// };

// console.log(reverse(x))

// let x = 1
// let num = 0
// while (x != 0) {
//   num += x
//   console.log(x)
// }

// let s = "loveleetcode"

// let keepTrack = 0
// var firstUniqChar = function (s) {
//   debugger;
//   for (let i = 0; i < s.length; i++){
//     for (let j = i + 1; j < s.length; j++){
//       if (s[i] != s[j]) {
//         keepTrack += i
//       }
//     }
//   }
// return keepTrack.toString()
// };

// console.log(firstUniqChar(s))

// let s = "loveleetcode";
// var firstUniqChar = function (s) {
//   let obj = {};
//   let i = 0;
//   for (i; i < s.length; i++) {
//     if (obj[s[i]]) {
//       obj[s[i]] += 1;
//     } else {
//       obj[s[i]] = 1;
//     }
//   }
//   for (let k = 0; k < s.length; k++) {
//     if (obj[s[k]] < 2) {
//       return k;
//     }
//   }
//   return -1;
// };

// console.log(firstUniqChar(s));

// let digits = [9,9]

// var plusOne = function (digits) {
//   for (let i = digits.length - 1; i >= 0; i--){
//     if (digits[i] < 9) {
//       digits[i]++
//       return digits
//     } else {
//       digits[i] = 0
//     }
//   }
//   digits.unshift(1)
//   return digits
// };

// console.log(plusOne(digits));

// let digits = [9]
// var plusOne = function(digits) {
//   for (let i = 0; i < digits.length; i++){
//     if (digits[i] < 9) {
//       digits[digits.length - 1]++
//       return digits
//     } else {
//       digits[i] = 0
//      }
//   }
//   digits.unshift(1)
//   return digits;
// };

// console.log(plusOne(digits));

// let nums = [3,0,1]
// var missingNumber = function (nums) {
//   for (let i = 0; i < nums.length; i++) {
//     console.log(i)
//   }

// };
// console.log(missingNumber(nums))

// trying to solve without using  any inbuilt methods

// function largestNum(arr) {
//   debugger;
//   let min = arr[0]
//   let i = 0
//   while (arr.length > i) {
//     i += 1
//     if (arr[i] > min) {
//       min = arr[i]
//     }
//   }
//   return min
// }

// console.log(largestNum(arr));

// let arr = [-1, 3, 5, 6, 99, 12, 2];
// const largestNum = (arr, i = 0) => {
//   debugger;
//   let min = arr[i]
//   let j = i + 1
//   if (i < arr.length - 1) {
//     if (arr[j] > min) {
//       i += 1
//        min = arr[j]
//     } else {
//       largestNum(arr, i)
//     }
//   }
//   return min
// }

// const largestNumTwo = (arr, i = 0, max = -Infinity) => {
//   if (i < arr.length) {
//     if (arr[i] > max) {
//       max = arr[i];
//     }
//     return largestNumTwo(arr, i + 1, max);
//   }
//   return max;
// };

// console.log(largestNumTwo(arr));

// function largestNum(arr) {
//   debugger;
//   let min = arr[0];
//   for (let i = 1; i < arr.length; i++) {
//     if (arr[i] > min)  min = arr[i];
//   }
//  return min
// }

// practicing factorial problem
// const factorize = (n) => {
//   if (n < 0) {
//    return - 1
//   } else if (n === 0) {
//     return 1
//   } else {
//     return (n * factorize(n - 1))
//  }
// }

// console.log(factorize(4))

// const factorial = (n) => {
//   let result = n
//   if (n === 0 || n === 1) return 1;
//     while (n > 1) {
//       n--
//       result *= n
//     }
//     return result

// }

// console.log(factorial(3))

//  chunk array
// let array = [1, 9, 6, 3, 2],
//   size = 1;
// const chunkArray = (array, size) => {
//   debugger;
//   if (size <= 0 || array.length === 0) {
//     return [];
//   }

//   let newArr = [];
//   let i = 0;
//   while (i < array.length) {
//     newArr.push(array.slice(i, i + size));
//     i += size;
//   }
//   return newArr;
// };

// console.log(chunkArray(array, size))

// const chunking = (arr, size) => {
//   if (arr <= size || arr.length === 0) return []
//   let i = 0
//   let chunkArray = []
//   while (i < arr.length) {
//     chunkArray.push(arr.slice(i, i + size))
//     i += size
//   }
//   return chunkArray
// }

// let  numbers = [2,3,4], target = 6
// var twoSum = function (numbers, target) {
//   debugger;
//   let sum = 0
//   let arr = []
//   let i = 0
//   let idxOne = 0
//   let idxTwo = 0
//   for (i; i < numbers.length; i++){
//     console.log(i)
//     sum = numbers[i] + numbers[i + 1]
//     if (sum === target) {
//       arr.push(i + 1, i + 1)
//     }
//   }
//   return arr
// };
// console.log(twoSum(numbers, target))

// let numbers = [2, 3, 4], target = 6

// var twoSum = function (numbers, target) {
//   debugger;
//   let right = numbers.length - 1
//   let left = 0
//   let sum = 0
//   let arr = []
//   while (left < right) {
//     sum = numbers[left] + numbers[right]
//     if (sum === target) {
//       return  [left + 1, right + 1]
//     } else if (sum < target) {
//       left++
//     } else {
//       right--
//     }
//   }
// };

// console.log(twoSum(numbers,target))

// two pointer problem
// let numbers = [-1, 0],
//   target = -1;
// var twoSum = function (numbers, target) {
//   let sum = 0;
//   let arr = [];
//   for (let i = 0; i < numbers.length; i++) {
//     for (let j = numbers.length - 1; j >= i; j--) {
//       sum = numbers[i] + numbers[j];
//       if (sum === target) {
//         return [i + 1, j + 1];
//       }
//     }
//   }
// };

// console.log(twoSum(numbers, target));

// Arrays -- have cache locality
// linked lists -- extra memory assocaited with and have more dynamic memory

// Queuses -- linked lists only

// let nums = [2, 7, 11, 15]
// let target = 9
// var twoSum =  function (nums, target)  {
//   debugger;
//   let left = 0
//   let right = nums.length - 1
//   let sum = 0
//   while (left < right) {
//     sum = nums[left] + nums[right]
//     if (sum === target) {
//        return [left + 1, right + 1]
//     } else if (sum > target) {
//       right--
//     } else {
//       left++
//      }
//   }
// }

// console.log(twoSum(nums,target))

// k is the length of the repeated item is repeated
// most frequent k items
// let nums = [4,1,-1,2,-1,2,3]
// let k = 2;
// var topKFrequent = function (nums, k) {
//   debugger;
//   let obj = {};
//   for (let i = 0; i < nums.length; i++) {
//     //  keep track of how many times a number repeats
//     if (obj[nums[i]]) {
//       obj[nums[i]] += 1;
//     } else {
//       obj[nums[i]] = 1;
//     }
//   }
//   let arr = [];
//   // sort the keys from the obj
//   let sortKeys = Object.keys(obj).sort((a,b)=>obj[b]-obj[a]);
//   for (let i = 0; i < k; i++){
//     arr.push(sortKeys[i])
//   }
//   return arr;
// };

// console.log(topKFrequent(nums, k));

//  repracticing the ame problem

// var topKFrequent = function(nums, k) {
//   let obj = {}
//   // O(n)
//   for (let i = 0; i < nums.length; i++){
//     if (obj[nums[i]]) {
//       obj[nums[i]] = 1
//     } else {
//       obj[nums[i]] += 1
//     }
//   }
//   let arr = []
//   //  O(n)
//   let sortKeys = Object.keys((a, b) => obj[b] - obj[b])
//   // O(n)
//   for (let i = 0; i < k; i++){
//     arr.push(sortKeys[i])
//   }
//   return arr;
// };

// let height = [1, 8, 6, 2, 5, 4, 8, 3, 7];
// var maxArea = function (height) {
//   debugger;
//   let x = 0;
//   let j = height.length - 1
//   //  height has length of n
//   // n vertical lines drawn such taht the ith line are (i, 0)
//   // and (i, height[i])
//   // find two lines on x-axis that make a container that hold a lot of water
//   for (let i = 0; i < height.length; i++) {
//     //   find difference between two numbers
//     let amountOfwater = Math.abs(j - i) * Math.min(height[i], height[height.length - 1]);
//     console.log("waterContainer", amountOfwater);
//     if (amountOfwater > x) {
//       x = amountOfwater;
//     }
//     if (height[i] < height[height.length - 1]) {
//       i++
//     } else {
//       j--
//     }
//   }
//   return x;
// };
// console.log(maxArea(height));

// let height = [1,8,6,2,5,4,8,3,7]
// var maxArea = function (height) {
//   debugger;
//   let total = 0
//   let left = 0
//   let right = height.length - 1

//   while (left < right){
//       let smallestSide = Math.min(height[left], height[right])
//       let area = (right - left) * smallestSide;

//       if (area > total) total = area

//       if (height[left] < height[right]) left++
//       else right--
//   }
//   return total
// };

// console.log(maxArea(height))

// let heig = [1,8,6,2,5,4,8,3,7]
// var maxAreas = function(heig) {
//   let left = 0
//   let right = heig.length - 1
//   let difference = 0
//   while (left < right) {
//     if (heig[left] === heig[right]) {
//       difference = height[left]
//     } else {
//       difference = heig[left] - heig[right]
//       console.log(difference)
//     }
//   }
// };

// console.log(maxAreas(heig))

// let nums = [100, 4, 200, 1, 3, 2];
// var longestConsecutive = function (nums) {
//   debugger;
//   //  handle the edge case
//   if (nums.length === 0) return 0;
//   // sort the array and remove any non squentialnumber
//   //  and return the length of that array with sequential numbers
//   let difference = 0;
//   let count = 1;
//   let max_count = 1;
//   let sortedArr = nums.sort((a, b) => a - b);
//   for (let i = 0; i < sortedArr.length - 1; i++) {
//     difference = sortedArr[i + 1] - sortedArr[i];
//     if (difference === 1) {
//       count++;
//     } else {
//       count = 1;
//     }
//     max_count = Math.max(max_count, count);
//   }
//   return max_count;
// };

// console.log(longestConsecutive(nums));

// let nums = [100, 4, 200, 1, 3, 2];
// var longestConsecutive = function (nums) {
//   let difference = 0;
//   let count = 1;
//   let max_count = 1;
//   // sort
//   nums.sort((a, b) => a - b);
//   for (let i = 0; i < nums.length - 1; i++) {
//     difference = nums[i + 1] - nums[i];
//     if (difference === 1) {
//       count++;
//     } else {
//       count = 1;
//     }
//     max_count = Math.max(count, max_count);
//   }
//   return max_count;
// };

// console.log(longestConsecutive(nums))

// var isValid = function (s) {
//   debugger;
//   //  key value pair
//   let char = {
//     "(": ")",
//     "{": "}",
//     "[": "]",
//   };
//   let stack = [];
//   //  if '()" return true"
//   //  else {] return false
//   for (let c in s) {
//     if (char[c]) {
//       stack.push(char[c]);
//     } else if (stack.length > 0 && stack[stack.length - 1] === k) {
//       stack.pop();
//     } else {
//       return false
//     }
//   }
//   return stack.length === 0;
// };

// console.log(isValid("(}"));

// var isValid = function (s) {
//   //  key value pair
//   let char = {
//     "(": ")",
//     "{": "}",
//     "[": "]",
//   };
//   //  if '()" return true"
//   //  else {] return false
//   let stack = [];
//   for (let c of s) {
//     if (char[c]) {
//       stack.push(char[c]);
//       console.log(stack)
//     } else if (stack.length > 0 && stack[stack.length - 1] === c) {
//       stack.pop();
//     } else {
//       return false;
//     }
//   }
//   return stack.length === 0;
// };

// console.log(isValid("(}"));

// var isValid = function (s) {
//   debugger;
//   //  key value pair
//   //
//   let char = {
//     "(": ")",
//     "{": "}",
//     "[": "]",
//   };
//   //  if '()" return true"
//   //  else {] return false
//   let stack = [];
//   for (let c of s) {
//     if (char[c]) {
//       stack.push(char[c]);
//     } else if (stack.length > 0 && stack[stack.length - 1] === c) {
//       stack.pop();
//     } else {
//       return false;
//     }
//   }

//   return stack.length === 0;
// };

// console.log(isValid("[]"));

// let nums = [1, 2, 3, 4];
// // output [24, 12, 8, 6]
// var productExceptSelf = function (nums) {
//   debugger;
//   let right = 1;
//   let left = 1;
//   let arr = [];
//   for (let i = 0; i < nums.length; i++) {
//     arr.push(right);
//     right *= nums[i];
//   }
//   for (let j = nums.length - 1; j >= 0; j--) {
//     arr[j] *= left
//     left *= nums[j];
//   }
//   return arr;
// };

// console.log(productExceptSelf(nums));

// let board = [
//   ["5", "3", ".", ".", "7", ".", ".", ".", "."],
//   ["6", ".", ".", "1", "9", "5", ".", ".", "."],
//   [".", "9", "8", ".", ".", ".", ".", "6", "."],
//   ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
//   ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
//   ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
//   [".", "6", ".", ".", ".", ".", "2", "8", "."],
//   [".", ".", ".", "4", "1", "9", ".", ".", "5"],
//   [".", ".", ".", ".", "8", ".", ".", "7", "9"],
// ];

// var isValidSudoku = function (board) {
//   debugger;
//   let hash = new Object();
//   console.log(hash);
//   for (let i = 0; i < board.length; i++) {
//     for (let j = 1; j < board.length - 1; j++) {
//       if (hash[board[i][j]]) {
//         hash[board[i][j]] += 1;
//       } else {
//         hash[board[i][j]] = 1;
//       }
//       console.log(i, hash);
//     }

//     // let columnZero = ('columns', board[i][0])
//     // let columnOne = ('columns', board[i][1])
//     // let columnTwo = ('columns', board[i][2])
//     // let columnThree = ('columns', board[i][3])
//     // let columnFour = ('columns', board[i][4])
//     // let columnFive = ('columns', board[i][5])
//     // let columnSix = ('columns', board[i][6])
//     // let columnSeven = ('columns', board[i][7])
//     // let columnEight = ('columns', board[i][8])
//     // let columnNine = ('columns', board[i][9])
//   }
// };

// console.log(isValidSudoku(board));

// const array = [];

// var isValidSudoku = function (board) {
//   // check vertically
//   for (let i = 0; i < board[0].length; i++) {
//     for (let j = 0; j < board.length; j++) {
//       console.log("vertical check", board[j][i]);
//     }
//   }
//   //  check horizantally
//   for (let j = 0; j < board.length; j++) {
//     console.log("horizantal check", board[j]);
//   }
// };

// console.log(isValidSudoku(board));

// var isValidSudoku = function (board) {
//   debugger;
//   //  iterate over the row , one by one meaning first row, second row etc
//   //  iterate over the coloum by iterating on eacgh row index board[0], board[1]
//   //  it needs to know what row I am at inorder to iterate over the column
//   // row
//   let result = false;
//   let hash = {};
//   for (let i = 0; i < board.length; i++) {
//     for (let j = 1; j < board.length; j++) {
//       console.log("board row", board[i][i]);
//       console.log("board column", board[j][j]);
//       if (board[i][j]) {
//         hash[board[i][j]] = 1;
//       } else {
//         hash[board[i][j]] += 1;
//       }
//       console.log(hash);
//       if (board[i][j] <= 9 || board[i][j] >= 1) {
//         result = true;
//       }
//       return result;
//     }
//   }
//   return result;
// };

// console.log(isValidSudoku(board));

let s = "ab";
let goal = "ab";
var buddyStrings = function (s, goal) {
  debugger;
  //  we have two variables s and goal
  //  s = 'ab', goal = 'ba'
  // return true if I can make s = 'ba'  else return false

  //  step1 iterate through each variable
  //  reverse the indexes
  //  return if that index is reversible
  let newStr = "";
  if (s !== goal) {
    for (let i = s.length - 1; i >= 0; i--) {
      newStr += s[i];
      console.log(newStr);
    }
    if (newStr === goal) {
      return true;
    } else {
      return false;
    }
  } else {
    return true;
  }
};

console.log(buddyStrings(s, goal));

// for await (let question of questions) {
//   console.log(answer(question));
// }
// console.log("Thanks");
