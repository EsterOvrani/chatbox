from flask import Flask, render_template, request

app = Flask(__name__)  # Initialize the Flask app# Chava: Define a route to serve the room page

@app.route('/<room>')
def serve_room_for_room(room):
    # Return the 'index.html' file when the route is accessed
    return render_template('index.html')

# return home page to client
@app.route('/')
def home_page():
    return render_template('index.html')


# Run the app if this script is executed directly
if __name__ == '__main__':
    app.run()  # Start the Flask development server
