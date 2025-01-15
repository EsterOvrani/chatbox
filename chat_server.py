<<<<<<< HEAD
from flask import Flask, render_template, request
=======
from flask import Flask, send_file  # Import Flask and the send_file function

app = Flask(__name__)  # Initialize the Flask app
>>>>>>> bfd7115fdc163b8f8eed518349587c39e8624080


# Chava: Define a route to serve the room page
@app.route('/<room>')
def serve_room_for_room(room):
    # Return the 'index.html' file when the route is accessed
    return send_file('index.html')

<<<<<<< HEAD
# return home page to client
@app.route('/')
def home_page():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')



=======

# Run the app if this script is executed directly
if __name__ == '__main__':
    app.run()  # Start the Flask development server
>>>>>>> bfd7115fdc163b8f8eed518349587c39e8624080
