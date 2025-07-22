from flask import Flask, render_template, request, jsonify
import subprocess

app = Flask(__name__)

current_label = ""  # To store the detected label

# Route for the start page
@app.route('/')
def start_page():
    return render_template('start.html')

# Route for the second page
@app.route('/second')
def second_page():
    return render_template('second.html')

# Route for the main application
@app.route('/main')
def index():
    return render_template('index.html')

@app.route('/run-face-detection')
def run_face_detection():
    subprocess.Popen(["python", r"C:\Users\manas\OneDrive\Desktop\DualSense_AI_For_Mental_Disorder_detection\main.py"])
    return "Face detection started!"

@app.route('/update-label', methods=['POST'])
def update_label():
    global current_label
    data = request.json
    current_label = data.get("label", "")
    return jsonify({"status": "Label updated!"})

@app.route('/get-label', methods=['GET'])
def get_label():
    global current_label
    return jsonify({"label": current_label})

if __name__ == '__main__':
    app.run(debug=True)
