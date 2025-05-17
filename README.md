
# 🎨 Cartoonify Video Web App  

Convert normal videos into **animated cartoon-style videos** directly in your browser! Built with Flask and OpenCV, this app processes videos frame-by-frame to apply artistic cartoon filters.  

---

## 🚀 Features  
- 🎞️ Upload MP4, AVI, or MOV videos  
- 🖌️ Apply real-time cartoonification using computer vision  
- ⚡ Fast processing with OpenCV optimizations  
- 🌐 Web interface + API endpoint support  

---

## 🛠️ Tech Stack  
| Layer       | Technology               |  
|-------------|--------------------------|  
| **Backend** | Python + Flask           |  
| **CV**      | OpenCV (`cv2`) + NumPy   |  
| **Utils**   | Werkzeug, tempfile       |  
| **Core**    | Custom `cartoonizer.py`  |  

---


## ⚡ Quick Start  

### 1. Clone & Setup  
```bash  
git clone https://github.com/Raj-Singh-3/cartoon_video  
cd cartoon_video  

# Create virtual environment (recommended)  
python -m venv venv  
source venv/bin/activate  # Windows: venv\Scripts\activate  

# Install dependencies  
pip install flask flask-cors opencv-python numpy  
```  

### 2. Run the App  
```bash  
python app.py  
```  
➡️ Access at: `http://localhost:5000`  

---

## 🧠 How It Works  
1. **Upload**: User submits a video via web form/API  
2. **Process**: Each frame is cartoonified via `cartoonizer.py`  
3. **Output**: Downloadable cartoon video generated  
---

## 🛣️ Future Roadmap  
- [ ] Real-time webcam cartoonification  
- [ ] Multiple art styles (comic, sketch, oil painting)  
- [ ] React frontend integration  
- [ ] Cloud deployment (AWS/GCP)  

---

## 👨‍💻 Author  
**Raj Singh**  
[![GitHub](https://img.shields.io/badge/GitHub-Profile-blue)](https://github.com/Raj-Singh-3)  
*Contributions welcome!*  

---

## 📜 License  
MIT © 2023 - Free for open-source use  

---

✨ **Tip**: For a live demo, check out our [deployed version](https://cartoon-video.vercel.app/)! 

--- 
