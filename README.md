# 🎬 AI Video Editor

**AI Video Editor** is a powerful, modular, and AI-enhanced video editing platform that automates key editing processes:
- 🎯 Hook detection
- 🎨 Color grading
- 🖼 Thumbnail generation
- 🌍 Multilingual dubbing
- 🎵 Speed & transition control
- 📦 Export in multiple formats

---

## 🚀 Features

| Feature             | Description |
|---------------------|-------------|
| 🎯 **Hook Detection** | Finds high-engagement clips in first 20 seconds |
| 🎨 **Color Grading** | Apply cinematic or vibrant LUTs |
| 🖼 **Thumbnail Generator** | Auto-pick keyframes and generate 3 thumbnails |
| 🎤 **Voice Translation** | Dub video in other languages using AI |
| 🎬 **Speed Control** | Add slow-mo, fast-forward effects |
| 🔀 **Scene Transitions** | Add cinematic transitions |
| 💾 **Export Options** | Export in MP4, MOV, MKV up to 4K |

---

## 🛠 Installation

```bash
git clone https://github.com/parasjarral01/ai-video-editor.git
cd ai-video-editor
pip install -r requirements.txt
```

---

## 🖥 Usage Options

### 1. 🖱 Run Desktop GUI

```bash
python gui/gui_app.py
```

### 2. 🌐 Run Streamlit Web App

```bash
streamlit run streamlit_app.py
```

---

## 🧪 Run Unit Tests

```bash
python -m unittest discover tests
```

---

## 📦 Build `.exe` (Windows only)

```bash
pip install pyinstaller
pyinstaller pyinstaller.spec
```

---

## ☁️ Deploy to Streamlit Cloud (Free)

1. Push this repo to GitHub ✅  
2. Go to [https://share.streamlit.io](https://share.streamlit.io)  
3. Select your repo → set file to `streamlit_app.py`  
4. Click **Deploy** 🚀

---

## 📸 Screenshots (optional)
*Add screenshots of GUI or features here.*

---

## 👤 Author

**Paras Jarral**  
GitHub: [@parasjarral01](https://github.com/parasjarral01)

---

## 🧠 Tech Stack

- Python, OpenCV, MoviePy, Pillow  
- Transformers, SpeechRecognition, gTTS  
- Streamlit, Tkinter, LangChain

---

## 📄 License

MIT License – use this project freely!
