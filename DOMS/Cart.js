document.addEventListener("DOMContentLoaded",()=>{

    document.querySelector("form").addEventListener("submit",(event)=>{
    event.preventDefault() // To Prevent Re Loading
    const prodTitle=document.getElementById("title").value
    const imgURL=document.getElementById("img-url").value
    const description=document.getElementById("desc").value

    // Product Objct // Convert The Vairaible into The Object(Product) 
    const product={
        title:prodTitle,
        imgURL:imgURL,
        decs:description
    }

    Prod_JSON=JSON.stringify(product) // Convert Product Object into JSON With the help of JSON.stringify(product)
    localStorage.setItem(prodTitle,Prod_JSON) 
    // localStorage :- To Store data in Browser Local Storage  
    // .setItem(KEY,JSON) :- setItem Method help to store the data in local storage in the Form of KEY,JSON in our Browser                 
    // .setItem(prodTitle,Prod_JSON))
            
    document.addEventListener("DOMContentLoaded",()=>{
    const prodFromStorage=localStorage.getItem("Apple Airdrops")
    console.log(prodFromStorage)
    })
    
    })

})



