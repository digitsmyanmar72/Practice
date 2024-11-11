// Importing the express module
const express = require("express");

// Creating an express application instance
const app = express();

// Defining a route for "api/people" with a GET request
app.get("/api/people", function(req, res) {
    const data = [
        { name: "nay", age: 41 },
        { name: "john", age: 30 }
    ];
    return res.status(200).json(data);  // Fixed the comma issue
});

// Starting the server and listening on port 8000
app.listen(8000, function() {
    console.log("Server is running on port 8000");  // Fixed the typo in the message
});
