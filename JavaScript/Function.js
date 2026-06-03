//// named Function(User Defined Function)

// function marriage(family){
//     console.log(`${family} welocme you...`)
//     console.log("Chinnu weds chinna")
//     console.log("Marriage ends")
//     console.log("\n")
// }

// marriage()
// // marriage()
// marriage("Mahato")


//// anonymous function

// const anotherMarriage=function (Bride,Groom){
//     console.log(`welocme you...`)
//     console.log(`${Bride} weds ${Groom}`)
//     console.log("Marriage ends")
//     console.log("\n")
// }
 
// const prompt=require("prompt-sync")({sigint:true})
// const B=prompt("Enter Bride name: ")
// const G=prompt("Enter Bride name: ")   
// anotherMarriage(B,G)

//// Arrow Function :- Shorter then anonymous


// const greet=()=>console.log("Hello")
// greet()

// let newMarriage=(...marriage)=>{

//     console.log(`${marriage[0]} welocme you...`)
//     console.log(`${marriage[1]} weds ${marriage[2]}`)
//     console.log("Marriage ends")
//     console.log("\n")

// }
// const Fa=prompt("Enter Family name: ")   
// const Gr=prompt("Enter Groom name: ")   
// const Br=prompt("Enter Bride name: ")
// newMarriage(Fa,Gr,Br) 


//// function with return keyword

// const add =(...nums)=>{
//     let res=0
//     for(let i of nums){
//         res+=i
//     }
//     console.log("hello i am before return")
//     return res
// }
// let result=add(1,2,3,4,5,6,7,8,9,10)
// console.log(result)


//// 4. Built-in Function

//// 5. ITFE - Immediately Invoked function Expression 
//// The Function which called themselves, when function invoked into JS program 

// (function(){
//     console.log("This is Life")
// })()

//// 6.Higher Ordered Function(HOF) 1.map() 2.
 
//// 7. map() - Iterate over array and returns another array

//// for in For Object 
//// for of For Array

// let nums=[5,3,2,9,10]
// const squares =nums.map((i)=>{ // i is iterate over each and every element of array // it is act like  (for i in iteration)
//     return i**2
// })
// console.log("Square of nums: ",squares)

// console.log("\n")
// Q Take Input(Number) from user Program ,Push it into Array Then Put The Square of the Number Into another Array

// const prompt=require("prompt-sync")({sigint:true})
// const n=prompt("Enter n: ")
// let nums1=[]
// for(let i=1;i<=n;i++){
//     nums1.push(prompt(`enter array element ${i}: `))
// }
// const squares1 =nums1.map((item)=>{ // item hold the value of num1 or it is act like  (for i in iteration)
//     return item**2
// })
// console.log("Square of nums: ",squares1)


//// Write a JS code to display product in E-commarce website UI

// const products=[  // products is array of object
//     { //object index 0
//         id:1,
//         category:"Electronics",
//         brand:"Bajaj",
//         title:"Edge HS Celling Fans",
//         discription:"fdslklkjfkjshkjshfkjfdhvkjhfkjssdfhgdjhdgfoiqfuoidgvjhvjhdcbdvk;jvh",
//         stock:15,
//         price:1234,
//         image:"https://m.media-amazon.com/images/I/31bysDp6YVL._SY300_SX300_QL70_FMwebp_.jpg"

//     },
//     { //object index 1
//         id:1,
//         category:"Electronics",
//         brand:"Coolers",
//         title:"Edge HS Celling Fans",
//         discription:"fdslklkjfkjshkjshfkjfdhvkjhfkjssdfhgdjhdgfoiqfuoidgvjhvjhdcbdvk;jvh",
//         stock:15,
//         price:1234,
//         image:"https://m.media-amazon.com/images/I/71+1buX7bxL._SX679_.jpg"

//     },
//     { //object index 2
//         id:3,
//         category:"Electronics",
//         brand:"Amazon Echo",
//         title:"Amazon Echo Dot (5th Gen)  Temperature Sensor, Alexa and Bluetooth| Blue",
//         discription:"5th (Latest) Generation Echo Dot with Alexa-The best sounding Echo Dot yet! With deeper bass and clearer vocals than all previous generations.",
//         stock:20,
//         price:5493,
//         image:"https://m.media-amazon.com/images/I/81hgjKwsdHL._SX569_.jpg"

//     }

// ]

// console.log(product)
// console.log(product[0])
// products.map((product)=>{
//     console.log(product)
//     console.log("Product :",product.id)
//     console.log("Category :",product.category)
//     console.log("brand :",product.brand)
//     console.log("Title :",product.title)
//     console.log("Discription :",product.discription)
//     console.log("stock :",product.stock  )
//     console.log("price :",product.price)
//     console.log("image :",product.image)



// })

// 13. filter()-Filter the array element based on given test case

// let nums=[1,2,3,4,5,6,7,8,9,10]
// let evenNums=nums.filter((item)=>{
//     return item%2==0
// })
// console.log("Even Nums :",evenNums)


// // Getting product based on condition
// const prompt=require("prompt-sync")({sigint:true})
// const price=prompt("Enter Price: ")

// let filters_prod=products.filter((product)=>{
//     if (product.price <= price){
//         return product
//     }
       
// })
// console.log(filters_prod.length ===0 ? "No items available ": filters_prod)



// 14 reducer()
let nums1=[1,2,3,4,5,6,7,8,9,10]
let SumNums=nums1.reduce((acc,curVal)=>{
    return acc+curVal
})
console.log("Sum of Nums :",SumNums)

// 15. for each Q.1 for each vs map 
// map() :- return array
// foreach() :- return individual element
// map()
let allnums=[1,2,3,4,5,6]
let res =allnums.map((element)=>{

    return element
})
console.log(res)

//  foreach()
allnums.forEach((element)=>{
    console.log(element)
})

// 16. some() :- Checks whether some of the array element passed the test return True

let something=allnums.some((item)=>{
    return item % 3 ===0
})
console.log(something ? "Atleast one of the values in array is divisible by 3":"No value is divisible by 3")

//17. every():- Checks whether all values of array satisfy given test case ,then return booleans
let allnums1=[1,2,3,4,5,6,-10]
let res2= allnums1.every((item)=>{
    return item>0
})
console.log(res2)




