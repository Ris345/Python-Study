// let S = 'abcabcbb'

// function subString(S) {
//     debugger;
//     newStr = ' '
//     for (let i = 0; i < S.length; i++){
//         for (let j = 0; j < S.length; j++){
//             if (S[i] !== S[j + 1]) {
//                 newStr =  S[j + 1]
//             }
//         }
//     }
//     return newStr
// }

// console.log(subString(S))

// L = [1, 2, 1, 6, 9, 4, 0, 1, 6, 2, 8, 1000, 1]

// function frequentNum(L) {
//     let obj = {}
//     // iterate over each item
//     //   run a nested loop
//     for (let i = 0; i < L.length; i++){
//         if (obj.hasOwnProperty(L[i])) {
//             obj[L[i]] = 1
//         } else {
//             obj[L[i]] += 1
//         }
//     }
//     return obj.keys()
// }

// num = [1, 1, 2]
// output = 2

// function removeDuplicates(num) {
//     i = 0
//     for (let j = 0; j < num.length; j++){
//         if (num[i] !== num[j]){
//             num[i + 1] = num[j]
//             i++
//         }
//     }
//     return i + 1
// }

// console.log(removeDuplicates(num))

// let nums = [1,1,2]
// const removeDuplicates = function (nums) {
//     debugger;
//     let i = 0
//     for (let j = 0; j < nums.length; j++){
//         if (nums[i] !== nums[j]) {
//             nums[i + 1] = nums[j]
//             i++
//         }
//     }
// return i + 1
// }

// console.log(removeDuplicates(nums))

// solved with O(n2) time complexity
// var containsDuplicate = function (nums) {
//     debugger;
//     for (let i = 0; i < nums.length; i++){
//         for (let j = 1; j < nums.length; j++){
//             if (nums[i] === nums[j]) {
//                 return true
//             }
//         }
//         return false
//     }
// };

// console.log(containsDuplicate(nums))

// O(n)
var containsDuplicate = function (nums) {
  debugger;
  let obj = {};
  for (let i = 0; i < nums.length; i++) {
    if (obj[nums[i]]) {
      obj[nums[i]] += 1;
    } else {
      obj[nums[i]] = 1;
    }
  }
  let values = Object.values(obj);

  if (Math.max(...values) > 1) {
    return true;
  }
  return false;
};
// console.log(containsDuplicate(nums))

// let s = "race a car"

// var isPalindrome = function (s) {
//     let regularStr = s.replace(/[^a-z0-9]/gi, '').toLowerCase()
//     let sortedStr =  s.replace(/[^a-z0-9]/gi, '').toLowerCase().split('').reverse().join('')
//     if (regularStr === sortedStr) {
//         return true
//     }
//    return false
// };

// console.log(isPalindrome(s))

// let s = "anagram";
let t = "nagaram";

var isAnagram = function (s, t) {
  sortS = s.split("").sort();
  console.log(sortS);
  sortT = t.split("").sort();
  console.log(sortT);
  return sortS === sortT ? true : false;
};

console.log(isAnagram(s));

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

let s = "loveleetcode";
var firstUniqChar = function (s) {
  let obj = {};
  let i = 0;
  for (i; i < s.length; i++) {
    if (obj[s[i]]) {
      obj[s[i]] += 1;
    } else {
      obj[s[i]] = 1;
    }
  }
  for (let k = 0; k < s.length; k++) {
    if (obj[s[k]] < 2) {
      return k;
    }
  }
  return -1;
};

console.log(firstUniqChar(s));

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



