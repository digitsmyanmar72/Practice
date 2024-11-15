from flask import Flask, render_template

# Create an instance of the Flask class
app = Flask(__name__)

# Define a route for the home page
@app.route('/')
def home():
    return "<h1>Welcome to My Simple Web App</h1>"

# Define a route for the about page
@app.route('/about')
def about():
    return "<h1>About Page</h1><p>This is a simple web app built using Flask.</p>"

# Start the Flask application
if __name__ == "__main__":
    app.run(debug=True)
