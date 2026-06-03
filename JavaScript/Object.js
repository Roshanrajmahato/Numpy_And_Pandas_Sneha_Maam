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


}
// Object inbuilt Method 

// 1. keys() :- Return all keys of object into an array
let allKeys =Object.keys(patientDetails)
console.log("All Keys of pattientDetails :",allKeys)


// 2. values() :-
let allValues =Object.values(patientDetails)
console.log("All Values of pattientDetails :",allValues)


// 3. entries() :- Return array of all 
let allEntries =Object.entries(patientDetails)
console.log("All Key Values of pattientDetails :",allEntries)
let flatEntred=allEntries.flat(Infinity)
console.log(flatEntred)


// 4. assign()

let contact={
        mobile:9204775882,
        mail:"12527roshan@gmail.com"
    }

let copied=Object.assign(patientDetails,contact)
console.log(copied)




// 5. seal()

Object.seal(contact)
// After .seal() Adding New -Not Allowed
// contact.address="BTM Bangolore"
// console.log("Updated Contact: ",contact)

// Modifying is Allowed 
contact.mobile="Not Available"
console.log("Updated Contact: ",contact)

// Deletion Not Allowed
delete contact.mobile
console.log("Updated Contact: ",contact)


// 6. freeze() :- Prevent the Modification also
Object.freeze(contact)

// JSON :- Java Script Object Notation | All Keys And Values in String only
// 1. stringify :- convert as JS object into an JSON data
console.log("\n")
console.log(" .stringify() convert as JS object into an JSON data")
const JSON_Data=JSON.stringify(patientDetails)
console.log("Object :",patientDetails)
console.log("JSON :",JSON_Data)

// Q stringify vs parse 
// Q Barcode vs 
// 1. .stringify() :- JSON_Data = JSON.stringify(JS_Object) :- Convert JS_Object into JSON_Data(String only Keys And Values)
// 2. .parse() :- JS_Object = JSON.parse(JSON_Data)  :- Convert JSON_Data into JS_Object After Api Call

// JSON Declaration
// `{

// }`
console.log("\n")
console.log(" .parse()  Convert JSON into Object")
// JSON
let contactNew = `{
        "mobile":"9204775882",
        "mail":"12527roshan@gmail.com"
    }`

console.log("JSON :",contactNew)
let Obj_Data=JSON.parse(contactNew)
console.log("Object :",Obj_Data)

// Destructing
const {mobile,mail}=contact
console.log(mobile)

