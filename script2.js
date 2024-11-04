const express = require("express");
const app = express();

app.get("/api/people/",function(req,res){
    const data = [
                 {name:"nay",age : 41 },
                 {name: "aye", age: 40}]
                 return res.status(200).json(data);
              })

app.listen(8000,function(){
    console.log("sever is running on port 8000");
})          