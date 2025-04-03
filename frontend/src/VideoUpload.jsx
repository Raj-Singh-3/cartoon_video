import React, { useState } from "react";
import axios from "axios";

const VideoUpload = () => {
  const [file, setFile] = useState(null);
  const [processedFile, setProcessedFile] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
  };

  const handleUpload = async () => {
    if (!file) return alert("Please select a video");
    
    setLoading(true);
    const formData = new FormData();
    formData.append("file", file);

    try {
      const res = await axios.post("http://127.0.0.1:5000/upload", formData, {
        headers: { "Content-Type": "multipart/form-data" },
      });
      setProcessedFile(res.data.output_file);
    } catch (error) {
      console.error("Upload error:", error);
      alert("Upload failed");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{ textAlign: "center", marginTop: "50px" }}>
      <h2>Upload Video for Cartoon Effect</h2>
      <input type="file" accept="video/*" onChange={handleFileChange} />
      <button onClick={handleUpload} disabled={loading}>
        {loading ? "Processing..." : "Upload & Convert"}
      </button>

      {processedFile && (
        <div>
          <h3>Processed Video</h3>
          <video controls width="400">
            <source src={`http://127.0.0.1:5000/download/${processedFile}`} type="video/mp4" />
          </video>
          <a href={`http://127.0.0.1:5000/download/${processedFile}`} download>
            <button>Download</button>
          </a>
        </div>
      )}
    </div>
  );
};

export default VideoUpload;
