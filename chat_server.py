from flask import Flask, render_template, request
import os

app = Flask(__name__)  # Initialize the Flask app

# chck the folder exist - ester ovrani
CHAT_DIR = "chats_massage"
if not os.path.exists(CHAT_DIR):
    os.makedirs(CHAT_DIR)

# get the room chat file - ester ovrani
def get_room_file(room):
    return os.path.join(CHAT_DIR, f"{room}.txt")

# Chava: Define a route to serve the room page
@app.route('/<room>')
def serve_room_for_room(room):
    # Return the 'index.html' file when the route is accessed
    return render_template('index.html')

    return os.path.join(CHAT_DIR, f"{room}.txt")

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

# Run the app if this script is executed directly
if __name__ == '__main__':
    app.run()  # Start the Flask development server
