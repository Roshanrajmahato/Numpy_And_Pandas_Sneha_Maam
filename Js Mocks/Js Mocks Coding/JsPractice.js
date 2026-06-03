// for (var i=0;i<5;i++){
//     setTimeout(function(){
//         console.log(i,`Roshan`)
//     })
// }

// let i=0
// while(i<5){
//     console.log(i,`RoshanRajMahato`)
//     i++
// }


// let arr=[2,3,4,5,6,7]
// let even=[]
// let odd=[]
// for(let num in arr){
//     if(arr[num]%2==0){
//         even.push(arr[num])
//     }
//     else{
//         odd.push(arr[num])
//     }
// }

// console.log(even)
// console.log(odd)


// const stu ={
//     "Name":"Roshan",
//     "Age":65,
//     "Place":"Dhanbad",
//     "Phono":9204775882

// }


// for(let ele in stu){
//     console.log(ele,stu[ele])
// }


// let arr=[1,2,3,4,5,6,7]
// for(let ele of arr){
//     console.log(ele)
// }
// let even=[]
// let odd=[]
// arr.forEach((num)=>{
//     if(num%2==0){
//         even.push(num)
//     }
//     else{
//         odd.push(num)
//     }
// })

// console.log(even)
// console.log(odd)

// function add(a,b){
//     return a+b
// }

// let a=(a,b)=>{
//     return a+b
// }


// console.log(a(45,78))


// let mul =(c,d)=>{
//     return c*d
// }

// const mul1=function(d,e){
//     return d*e
// }

// console.log(mul1(5,6))

// Name Functions
// function greet(Name){
//     return "hello " + Name

// }

// console.log(greet("Roshan"))

// Anonamous Functions

// let greet=function(name){
//     return "Hello " + name
// }

// console.log(greet("Roshan"))

// Arrow Functions

// let greet=(name)=>{
//     return "Hello " + name
// }

// console.log(greet("Roshan"))

// Additions

// function add(a,b){
//     return a+b
// }

// console.log(add(7,8))

// let add=function(a,b){
//     return a+b
// }
// console.log(add(7,9))

// let add=(a,b)=>{
//     return a+b
// }
// console.log(add(8,9))

// const num=[2,3,4,5,6,7]

// const res=num.filter(function(n){
//     if (n>5){
//         return n
//     }
// })

// console.log(res)


// let numbers=[1,2,3,4,5,6,7]

// const res=numbers.map((n)=>{
//     return n*2
// })

// console.log(res)

// setTimeout(()=>{
//     console.log("Hi After 10 Sec")
// },4000)

// for(let i=0;i<5;i++){
//     if(i===2){
//         break
        
//     }
//     console.log(i)
// }


// let obj = {
//   name: "Roshan",
//   show: function(){
//     console.log(this.name);
//   }
// };

// obj.show();   // Roshan

// let obj={
//   name:"Roshan",
//   show:function(){
//     console.log(this.name)
//   }
// }
// obj.show()


// let obj={
//   name:"Roshan",
//   show:()=>{
//     console.log(this.name)
//   }
// }
 
// obj.show()


// function fact(n){
//   let fac=1
//   for (let i=1;i<=n;i++){
//     fac*=i
//   }
//   return fac

// }

// console.log(fact(5))


// function factorial(n){
//   fact=1
//   for(let i=1;i<=n;i++){
//     fact*=i
//   }
//   return fact
// }

// function strong(digits){
//     sumfact=0
//     temp=digits
//     while(digits>0){
//       ld=digits%10
//       fact=factorial(ld)
//       sumfact+=fact
//       digits=Math.floor(digits/10)
//     }
//     if (sumfact==temp){
//       return true
//     }
    
// }

// if (strong(145)){
//   console.log("It is a Strong Numbers")
// }
// else{
//   console.log("Its Not a Strong Numbers")
// }


// function perfectnum(num){
//   let sumdiv=0
//   for(let i=1;i<num;i++){
//     if(num%i==0){
//       sumdiv+=i
//     }
//   }
//   return sumdiv === num
// }

// if(perfectnum(7)){
//   console.log("Its is Perfect Number")
// }
// else{
//   console.log("Its Not a Perfect numbers")
// }

// function prime(num){
//   if (num<2) return false

//   for(let i=2;i<num;i++){
//     if(num%i==0){
//       return false
//     }
//   }
//   return true
// }

// console.log(prime(17))
// console.log(prime(18))





