from flask import Flask

# Create a Flask application instance
app = Flask(__name__)

# Define a route for the homepage
@app.route('/')
def hello_world():
    return "My name is Jatin shah"

# Start the server
if __name__ == '__main__':
    app.run(debug=True)
