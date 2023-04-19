

let S = 'abcabcbb'

function subString(S) {
    debugger; 
    newStr = ' '
    for (let i = 0; i < S.length; i++){
        for (let j = 0; j < S.length; j++){
            if (S[i] !== S[j + 1]) {
                newStr =  S[i]
            }
        }
    }
    return newStr 
}

console.log(subString(S))