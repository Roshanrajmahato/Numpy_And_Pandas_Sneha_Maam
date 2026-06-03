// inbuilt method of string
let insti = "pyspider";
// for (let i = 0; i < insti.length; i++) {
//   console.log(insti[i]);
// }

// WAP To Reverse a string using a loop
// let res = "";
// for (let j = insti.length - 1; j >= 0; j--) {
//   // console.log(insti[j])
//   res += insti[j];
// }
// console.log(res);

// Built In Method
// 1. toUpperCase()

let name1 = "Roshan";
// console.log(toUpperCase(name1))

// 2. toLowerCase()
// console.log(toLowerCase(name1))

// 3. length

// console.log(length.name1)

// 4. slice()
// name1.slice(name1.slice(-1))

// 5. concat()

let concatinatedStr=name1.concat("Raj")
// console.log(concatinatedStr)

// 6. replace()

// console.log(concatinatedStr.replace("Raj","Mahato"))

// 7. split()

// console.log(insti.split(""))

// WAJSP to reverse a string using built-in Method

// let splitting=name1.split("")
// let reverse1=splitting.reverse() // built-in method 
// let revSting=reverse1.join("")
// console.log(revSting)

// console.log(name1.split(""))

// 8. trim() :- Removes white space from string
// let str="        ceilling fann    "
// console.log(str)
// console.log(str.trim())


// 9. padStart() :-


const prompt=require("prompt-sync")({sigint:true})
// const num=prompt("Enter The Number: ")

// if (num.length !== 10){
//   console.log("Please enter 10 digits ")
// }else{
//   const maskedMob = num.slice(-3).padStart(num.length,"*")
//   console.log("OTP Has Been Sent To ",maskedMob)
// }



// 10. padEnd()


// 11. indexof() :- Returns the index of given character

// console.log(name1.indexOf("o"))

// 12. charAt() :- Return the Character which is Present at Mentioned index



// 13. .charCodeAt() :- Return the ASCII Value of the character which is present at specified index

// console.log(name1.charAt(1))

// 14. .fromCharCode()

// console.log(name1.fromCharCode(80))

// Q Enter A/a print a to z  or A to Z

// let alpha = prompt("Enter a/A:")

// if (alpha==="A"){
//   for(let i=65;i<91;i++){
//   console.log(String.fromCharCode(i))
// }
// }

// 14. includes() :- Checks whether the given string pattern is included in original string and return boolean

console.log(concatinatedStr.includes("Raj"))
console.log(concatinatedStr.includes("Rash"))

// 15. startsWith() :- 


// 16. endsWith() :- Checks whether the string ends with given pattern or not ,return boolean

console.log(insti.endsWith("ers"))
console.log(insti.endsWith("ersz"))







