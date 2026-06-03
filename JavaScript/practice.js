
// function factorial(n){
//     fact=1;
//     for(let i=1;i<=n;i++){
//         fact*=i
//     }
//     return fact
// }

// console.log(factorial(6))

function factorial(n){
    fact=1;
    for (let i=1;i<=n;i++){
        fact*=i;
    }
    return fact
}
 function istrong(n){
    temp=n
    sum=0
    while(temp<0){
        let ld=n%10
        sum=sum+factorial(id)
        temp=Math.floor(temp/10)
    }
 }
// otp=Math.trunc(Math.random()*1000)


// let opt =Math.trunc(Math.random()*10000)
// console.log("OTP :",opt)


// const patientDetails={
//     name : "Ankhush",
//     place:"Bengaluru",
//     disease:"Heart Broken",
//     DOA:"01/01/2026",
//     age:42,
//     weight:"35kg",
//     height:"5F",
//     bloodGroup:"B+ve",
//     contact:{
//         mobile:9204775882,
//         mail:"12527roshan@gmail.com"
//     }

// }



// for(let i in patientDetails){
//     if(typeof patientDetails[i]==="object"){
//         for(let j in patientDetails[i]){
//             console.log(j,patientDetails[i][j])
//         }
//     }else{       
//         console.log(i,patientDetails[i])      
//     }
// }


// const person={
//     name:"Roshan",
//     rollno:12,
//     addres:"Dhanbad",
//     phone:{
//         personel_no:9204775882,
//         company_no:9234775882,
//     }
// }

// for(i in person ){
//     if(typeof person[i]=="object"){
//         console.log(person[i])
//         for (j in person[i]){
//             console.log(person[i][j])
//         }
//     }
// }