import React, { useState } from "react";
import axios from "axios";
import { FaCloudUploadAlt } from "react-icons/fa";
import "./VideoUpload.css"; // Import external CSS

const VideoUpload = () => {
    const [selectedFile, setSelectedFile] = useState(null);
    const [isProcessing, setIsProcessing] = useState(false);
    const [buttonClicked, setButtonClicked] = useState(false);

    const handleFileChange = (event) => {
        setSelectedFile(event.target.files[0]);
    };

    const handleUpload = async () => {
        if (!selectedFile) {
            alert("Please select a file first!");
            return;
        }

        const formData = new FormData();
        formData.append("file", selectedFile);

        setIsProcessing(true);
        setButtonClicked(true); // Change button color

        try {
            const response = await axios.post("http://127.0.0.1:5000/upload", formData, {
                responseType: "blob", // Expect a binary file (video)
            });

            // Create a download link for the video
            const url = window.URL.createObjectURL(new Blob([response.data], { type: "video/mp4" }));
            const link = document.createElement("a");
            link.href = url;
            link.setAttribute("download", "cartoon_video.mp4"); // Set download filename
            document.body.appendChild(link);
            link.click();
            link.remove();

        } catch (error) {
            console.error("Upload error:", error);
            alert("Error processing video!");
        } finally {
            setIsProcessing(false);
        }
    };

    return (
        <div className="upload-container">
            <h2 className="upload-title">🎨 Convert Your Video to Cartoon</h2>

            <label className="upload-box">
                <FaCloudUploadAlt className="upload-icon" />
                <input type="file" onChange={handleFileChange} className="file-input" />
                <p>Click or Drag to Upload Video</p>
            </label>

            {selectedFile && (
                <p className="file-name">📂 Selected: {selectedFile.name}</p>
            )}

            <button
                className={`upload-button ${buttonClicked ? "clicked" : ""}`}
                onClick={handleUpload}
                disabled={isProcessing}
            >
                {isProcessing ? "⏳ Processing..." : "🎥 Convert to Cartoon"}
            </button>
        </div>
    );
};

export default VideoUpload;
