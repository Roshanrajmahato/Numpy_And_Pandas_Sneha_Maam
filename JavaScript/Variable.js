// Declacartion of variable
 // Q. Why we can't used var

// 1.using var
// Used to declare global scoped variable

var trainerName   // Declaration
console.log(trainerName)
// 
// Initailization
trainerName="Yalaguresh"
console.log("Trainer name after initialization",trainerName)

{
    console.log("******************************************")
    var User_Name_Is_Active="Roshan" // Snake Case
    var UserNameIsActive="Roshan Raj Mahato" // Camel Case Or Title Case // Recommand
    console.log("Active user name inside the block",UserNameIsActive)
    console.log("******************************************")

}
console.log("Active user name outside the block",UserNameIsActive)

// Re-initialization
trainerName="Irshan Sir" // Without var Keyword
console.log("Trainer name after Re-initialization",trainerName)

// Re-declaration
var trainerName="Rahul Sir" // With var
console.log("Trainer name after Re-declaration",trainerName)





// ************************Using let keywod*****************************//
{
    let insti="Pysider"
    console.log("Inside the block :",insti)

}

console.log("Inside the block :",insti)

// Re-initailization
insti="Q Spider" // Without let Keyword
console.log("Institute after Re-initialization",insti)


// Re-Declaration
let insti="Q Spider" // With let Keyword
console.log("Institute after Re-initialization",insti)



//************************Using const keywod b *************************** */