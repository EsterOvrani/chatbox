from flask import Flask, send_file  # Import Flask and the send_file function

app = Flask(__name__)  # Initialize the Flask app


# Chava: Define a route to serve the room page
@app.route('/<room>')
def serve_room_for_room(room):
    # Return the 'index.html' file when the route is accessed
    return send_file('index.html')


# Run the app if this script is executed directly
if __name__ == '__main__':
    app.run()  # Start the Flask development server
