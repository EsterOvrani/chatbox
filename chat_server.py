from flask import Flask, render_template, request
from datetime import datetime
import os

app = Flask(__name__)  # Initialize the Flask app

# chck the folder exist - ester ovrani
CHAT_DIR = "chats_massage"
if not os.path.exists(CHAT_DIR):
    os.makedirs(CHAT_DIR)

# get the room chat file - ester ovrani
def get_room_file(room):
    return os.path.join(CHAT_DIR, f"{room}.txt")


@app.route('/<room>')
def serve_room_for_room(room):
    # Return the 'index.html' file when the route is accessed
    return render_template('index.html')

# return the room chat massage file - ester ovrani
@app.route('/api/chat/<room>', methods=['GET'])
def go_room_page(room):
    try:
        with open(get_room_file(room), 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
            return ""

# return home page to client - ester ovrani
@app.route('/')
def home_page():
    return render_template('index.html')

# Chava
@app.route('/api/chat/<room>', methods=['POST'])
def post_message(room):
    try:
        # Retrieve data from the incoming POST request (form-data)
        username = request.form.get('username')  # The username sent in the form
        message = request.form.get('msg')       # The message sent in the form

        # Print the request data for debugging purposes
        print(f"Received POST request for room {room}")
        print(f"Form data: {request.form}")
        print(f"Username: {username}, Message: {message}")

        # Check if both username and message are provided
        if not username or not message:
            print("Missing username or message")  # If missing any of the required fields
            return 'Missing username or message', 400  # Return a 400 Bad Request error

        # Define the file path for the chat room's file
        room_file = os.path.join(CHAT_DIR, f"{room}.txt")

        # Create a timestamp for the message
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # Format the message with timestamp, username, and message
        chat_line = f"[{timestamp}] {username}: {message}\n"

        # Write the message to the room's file
        with open(room_file, 'a', encoding='utf-8') as f:
            f.write(chat_line)

        # Print a success message to confirm that the message was saved
        print(f"Message saved successfully to {room_file}")
        return 'Message saved successfully', 200  # Return success response with status code 200

    except Exception as e:
        # If an error occurs during the process, catch it and print the error
        print(f"Error saving message: {str(e)}")
        return 'Internal server error', 500  # Return a 500 Internal Server Error

# Run the app if this script is executed directly
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
