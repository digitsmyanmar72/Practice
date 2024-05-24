//import express
const express = require ("express");
//create app
const app = express();
//define a route for "/api/people" and get request handler
app.get("/api/people") , function (req,res){
    const data = [
        {name:"nay"},
        {age:41}]
    return res.status(200).json(data);
};
//listen on port 8000
app.listen(8000,function(){
    console.log("server is running on port 8000")
});