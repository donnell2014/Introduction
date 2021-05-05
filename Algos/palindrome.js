 // Create a function that returns as boolean of true/false for whether or not an input string is a strict pallindrome. Do not ignore whitespaces!!

 // Example 1: "racecar" --> true
 // Example 2: "Dud" --> false
 // Example 3: "oho!" --> false

function isPallindrome(str){
    for (x=0;x<str.length/2;x++){
        if (str[x] !=str[str.length-x-1]){
            return false
        }
    } 
    return true
}


console.log(isPallindrome("racecar"));
console.log(isPallindrome("Dud"));
console.log(isPallindrome("oho!"));
console.log(isPallindrome("ohoo"));

// Given a String, return the longest pallindromic substring. Given "hello dada", return "dad". Given "not much" return "n". Include spaces as well!

// Example 1: "my favorite racecar erupted" --> "e racecar e"
// Example 2: "nada" --> "ada"
// Example 3: "nothing to see" --> "ee"

function longestPallindrome(str) {
    for (x=0;x<str.length/2;x++){
        for (j=0;x<str.legnth/2;j++){
            if (str[x] !=str[str.length-x-1]){
                    return true
            }
        }return false
    }
}
console.log(longestPallindrome("my favorite racecar erupted"));
console.log(longestPallindrome("nada"));
console.log(longestPallindrome("nothing to see"));