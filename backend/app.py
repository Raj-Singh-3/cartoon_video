from flask import Flask, request, jsonify, Response
from flask_cors import CORS
import cv2
import numpy as np
import tempfile
from cartoonizer import cartoonize_video
from werkzeug.utils import secure_filename

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Allowed video extensions
ALLOWED_EXTENSIONS = {"mp4", "avi", "mov", "mkv"}

def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

# Upload and process video
@app.route("/upload", methods=["POST"])
def upload_video():
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["file"]
    if file.filename == "":
        return jsonify({"error": "No selected file"}), 400

    if not allowed_file(file.filename):
        return jsonify({"error": "Invalid file type. Allowed: mp4, avi, mov, mkv"}), 400

    filename = secure_filename(file.filename)

    # Create a temporary file for input and output
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp4") as temp_input:
        file.save(temp_input.name)
        temp_input_path = temp_input.name

    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp4") as temp_output:
        temp_output_path = temp_output.name

    try:
        # Process the video
        cartoonize_video(temp_input_path, temp_output_path)

        # Read the processed video and return it as a response
        def generate():
            with open(temp_output_path, "rb") as f:
                yield from f

        return Response(generate(), mimetype="video/mp4", headers={"Content-Disposition": f"attachment; filename=cartoon_{filename}"})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run Flask app
if __name__ == "__main__":
    app.run(debug=True)
