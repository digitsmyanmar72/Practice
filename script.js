// Import express
const express = require("express");

// Create app
const app = express();

// Define a route for "/api/people" and get request handler
app.get("/api/people", function(req, res) {
    const data = [
        { name: "Nay", age: 41 },
        { name: "John", age: 30 }  // Adding another object to demonstrate consistent structure
    ];
    res.status(200).json(data);
});

// Listen on port 8000
app.listen(8000, function() {
    console.log("Server is running on port 8000");
});
