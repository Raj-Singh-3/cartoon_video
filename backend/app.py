# from flask import Flask, request, jsonify, send_from_directory
# import os
# import cv2
# import numpy as np
# from cartoonizer import cartoonize_video
# from werkzeug.utils import secure_filename

# app = Flask(__name__)

# UPLOAD_FOLDER = "uploads"
# PROCESSED_FOLDER = "processed"
# os.makedirs(UPLOAD_FOLDER, exist_ok=True)
# os.makedirs(PROCESSED_FOLDER, exist_ok=True)

# app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
# app.config["PROCESSED_FOLDER"] = PROCESSED_FOLDER

# @app.route("/upload", methods=["POST"])
# def upload_video():
#     if "file" not in request.files:
#         return jsonify({"error": "No file uploaded"}), 400

#     file = request.files["file"]
#     if file.filename == "":
#         return jsonify({"error": "No selected file"}), 400

#     filename = secure_filename(file.filename)
#     file_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
#     file.save(file_path)

#     output_path = os.path.join(app.config["PROCESSED_FOLDER"], "cartoon_" + filename)
#     cartoonize_video(file_path, output_path)

#     return jsonify({"message": "Video processed", "output_file": "cartoon_" + filename})

# @app.route("/download/<filename>", methods=["GET"])
# def download_video(filename):
#     return send_from_directory(app.config["PROCESSED_FOLDER"], filename)

# if __name__ == "__main__":
#     app.run(debug=True)



from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os
import cv2
import numpy as np
from cartoonizer import cartoonize_video
from werkzeug.utils import secure_filename

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Create necessary directories
UPLOAD_FOLDER = "uploads"
PROCESSED_FOLDER = "processed"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(PROCESSED_FOLDER, exist_ok=True)

# Configure upload folder paths
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["PROCESSED_FOLDER"] = PROCESSED_FOLDER

# Allowed video extensions
ALLOWED_EXTENSIONS = {"mp4", "avi", "mov", "mkv"}

def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

# Upload route
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
    file_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
    file.save(file_path)

    output_filename = "cartoon_" + filename
    output_path = os.path.join(app.config["PROCESSED_FOLDER"], output_filename)

    try:
        cartoonize_video(file_path, output_path)
        return jsonify({"message": "Video processed", "output_file": output_filename})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Download processed video
@app.route("/download/<filename>", methods=["GET"])
def download_video(filename):
    return send_from_directory(app.config["PROCESSED_FOLDER"], filename)

# Run Flask app
if __name__ == "__main__":
    app.run(debug=True)
