
// for loop
const prompt=require("prompt-sync")({sigint:true})
const num=prompt("Enter The Number")
for(let i=1;i<=10;i++){

    console.log(`${num} x ${i} = ${num*i}`)

}

// for in  :- used to iterate though object
// for(iterator in object){
//                    //iterator
//                   }
//
console.log("-----for in loop------")
const patientDetails={
    name : "Ankhush",
    place:"Bengaluru",
    disease:"Heart Broken",
    DOA:"01/01/2026",
    age:42,
    weight:"35kg",
    height:"5F",
    bloodGroup:"B+ve",
    contact:{
        mobile:9204775882,
        mail:"12527roshan@gmail.com"
    }

}

for(let i in patientDetails){
    if(typeof patientDetails[i]==="object"){
        for(let j in patientDetails[i]){
            console.log(j,patientDetails[i][j])
        }
    }else{       
        console.log(i,patientDetails[i])      
    }
}

console.log("---adding new email in contact---")
for(let i in patientDetails){
    if(typeof patientDetails[i]==="object"){
        patientDetails[i].personal_mail="rjm123445@gmail.com"
    }
}

console.log("--- printing after adding email ---")
for(let i in patientDetails){
    if(typeof patientDetails[i]==="object"){
        for(let j in patientDetails[i]){
            console.log(j,patientDetails[i][j])
        }
    }else{       
        console.log(i,patientDetails[i])      
    }
}


// for of -used to iterate through array
console.log("\n")
let patient=["Ankhush","Heart Broken","01/01/2026","Bengaluru","object"]
for(let i of patient){
    console.log(i)
}


// while loop
// Type Casting 
// const n=parseInt(prompt("Enter number :")) Method 1
// let i=Number(prompt("Enter the number: ")) Method 2

console.log("\n")
let n = +prompt("Enter number :") // Method 3
let i=-n
while( n>=i){
    console.log(n)
    n--
}

// do while loop
// Q. while Vs do while

let num1=15
do{
    console.log("I am do-while loop")
}while(num1<=17)







