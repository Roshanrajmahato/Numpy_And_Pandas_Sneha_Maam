// 1. String
// Group of charecter enclosed with Quetes
// Quotes- ' ', " " , ``(Blackticks)
let Institute='Pyspiders'
console.log("Institute is : ",Institute)

let students="Pyspider's Students "
console.log("We are : ",students)

let place=`BTM Bangolore `
console.log("Location of Pyspider: ",place)

// Checking Data Types
console.log("Type Of Pyspider: " , typeof Institute)

// String interpolation
console.log("addition : 10+2 ")
console.log(`Addition : ${10+2}`) // Blacktick

console.log(`We are ${students},${Institute} ,is located in ${place}`) // Blacktick

// 2.Number 
let num=1001
console.log("Number: ",num)

let decNum=1001.111
console.log(typeof num , typeof decNum)

// Number
let  capacity1=12345679
console.log(capacity1)

// BigInt
let capacity2=BigInt("12345667890000012345678")
console.log(typeof capacity2)
//Or
let capacity3=12345677898946425346367772n
console.log(typeof capacity3)

// Boolean: can hold only 2 entity i.e true or false
 let AreStudentFeelingSleepy =false
 console.log("Are Student in web class feelin sleep:",AreStudentFeelingSleepy)
 console.log(typeof AreStudentFeelingSleepy)

 // Undefined
 // A variable without Value is known as undefined
 // Here Declaration of variable will be done, but won't be initialised with value

 let Age
console.log("Age is :", Age)
console.log(typeof Age)


// null


// object
let patientDetails={
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

console.log("Patient details in jayadeva hospital: ",patientDetails)
console.table(patientDetails)

// Accessing Value
console.log("Patient name :",patientDetails.contact)
console.log("Patient name :",patientDetails.bloodGroup)
console.log("Patient name :",patientDetails.height)

console.log("Patient name :",patientDetails["place"])
console.log("Patient name :",patientDetails["DOA"])
console.log("Mail Id :", patientDetails.contact.mail)

// Updating the Value of contact
console.log("Mail Id :", patientDetails.contact.mobile=9234775882)



// Adding New Key:Value to Object(Dictionary)
patientDetails.gender="Female"
console.log("Updated Patient details: ",patientDetails)
// Note:- if key is already existed then value will be overwritten , or else is will be overwritten or else it will be inserted 


// Delete the oject
delete patientDetails.height
console.log("Deleting The Property",patientDetails)


