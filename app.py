# Import the Flask module to create a web application
from flask import Flask

# Import the render_template module for rendering HTML templates
from flask import render_template

# Import the request module for handling HTTP requests
from flask import request

# Import the flash module for flashing messages to the user
from flask import flash

# Import the Python 'secrets' module, which is not part of Flask, for generating secure tokens
import secrets

# Create a Flask web application instance
app = Flask(__name__)

# Set a secret key for app
secret_key = secrets.token_hex(
    16
)  # Generate a 32-character (16 bytes) random hexadecimal key
app.secret_key = secret_key


@app.route("/")
def index():
    flash("What's your name?")
    return render_template("index.html")


@app.route("/greet", methods=["POST", "GET"])
def greet():
    flash("Hi " + str(request.form["name_input"]) + ", great to see you")
    return render_template("index.html")


# Check if this script is the main entry point (not imported as a module)
if __name__ == "__main__":
    # Run the Flask app in debug mode on port 8000
    app.run(debug=True)
