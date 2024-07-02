//importing the express module
const express = require("express");
//Createing an express application instance
const app = express();
//Defining a route for "api/people" with a get result
app.get("../api/people",function(req,res){
    const data = [
        {name: "nay"},
        {age : 41},
    ];
    return res.status(200),json(data);

})
//starting the server and listenting on port 8000
app.listen(8000,function(){
    console.log("serving is runnign on port 8000")
});

