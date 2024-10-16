from flask import Flask, render_template

# Initialize the Flask app
app = Flask(__name__)

# Define the route for the homepage
@app.route("/")
def home():
    return render_template("index.html")

# Run the app on localhost
if __name__ == "__main__":
    app.run(debug=True)
    
    
@app.route("/about")
def about():
    return render_template("about.html")

