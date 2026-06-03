let skills=["Web Tech","Python","SQL","Django","DSA","Devops"]
console.log("List of Skills: ",skills)
console.log(typeof skills)
console.log("First skill in list: ",skills[0])

// Built-in Method
// 1.toString() - Convert whole array into a string of comma 

let strskills = skills.toString
console.log("1. to string",strskills)
console.log(typeof strskills)

// 2. .joins() -join all elements of array using given seperator

console.log("2.join: ",skills.join("-"))

// 3. pop()

console.log("3. pop",skills.pop())

//4. push()

console.log("4. push",skills.push("Google")) // Push at end
console.log("Skills",skills)

//5. shift

console.log("5. shift",skills.shift("Microsoft")) // removing the beggining of array and returm the remove beginging value
console.log("Skills",skills)

// 6.unShift :- adding at the begning of array


// 7. slice()
// Normal Slicing  


// 8.splice()

// used to remove multiple elements from array based on given index

let num=[1,2,3,4,5,6,7]
console.log(num)
let res=num.splice(3,3,"Hi","Hello","Bye","Good Bye")// .splice(Start indexing,No of element To remove, Replace By Values To That Place(optional) )
console.log(res)
console.log("After splice:",num)


// Q . What is function ? Type of Function?
// Q . Arrow function ?
// Q . Higher order function ?
// Q . Call Back Function ?


let randNums=[111,99,1000,121,7]
const sorted =randNums.sort((a,b)=>{
    return a-b
})

console.log("Sorted rendom Numbers: ",sorted)

// Destructuring :-Assigning a value to a distinct variable by unpacking collection is known as desctructing
// or
// It is a process of unpacking 

let class_001=["Shubham","Roshan","Vivek","Anmol","Raj","Munna","Abhishek"]
const [std1,std2,std3,std4,...stds]=class_001
console.log(std1)
console.log(stds)
