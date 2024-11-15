/*importing express module*/
const express = require("express")

// creating an express application instance
const app = express()
//defining a route for "/api/people" with get result handler
app.get("/api/people",function(req,res){
    const data = [
        {name:"nay",age:41},
        {name:"aye",age:40},
        {name:"thant",age:11}
    ]
    return res.status(200).json(data)
})
//Starting the server and listening on port 8000
app.listen(8000,function(){
    console.log("Server is running on port 8000, Saryar Gyi Ko Nay Win Aung")
})