from flask import Flask, request, jsonify

app = Flask(__name__)

# Define a route that takes user_id as a URL parameter
@app.route("/get-user/<user_id>")
def get_user(user_id):
    # Create a sample user data dictionary
    user_data = {
        "user_id": user_id,
        "name": "John Doe",
        "email": "john.doe@example.com"
    }
    
    # Check if there is an 'extra' query parameter in the request URL
    extra = request.args.get("extra")
    if extra:
        # Add the extra information to the user_data dictionary if provided
        user_data["extra"] = extra

    # Return a JSON response with a 200 status code
    return jsonify(user_data), 200

# Ensure the app runs only if this file is executed directly
if __name__ == "__main__":
    app.run(debug=True)
    
    
    #curl = http://localhost:5000/get-user/123?extra=admin