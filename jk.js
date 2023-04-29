

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
    let obj = {}
    for (let i = 0; i < nums.length; i++){
        if (obj[nums[i]]) {
            obj[nums[i]] += 1
        } else {
            obj[nums[i]] = 1
         }
    }  
    let values = (Object.values(obj))
    
    if ( Math.max(...values) > 1) {
        return true
    } 
    return false  
};
console.log(containsDuplicate(nums))



let s = "race a car"

var isPalindrome = function (s) {
    let regularStr = s.replace(/[^a-z0-9]/gi, '').toLowerCase()
    let sortedStr =  s.replace(/[^a-z0-9]/gi, '').toLowerCase().split('').reverse().join('')
    if (regularStr === sortedStr) {
        return true
    }
   return false 
};

console.log(isPalindrome(s))


