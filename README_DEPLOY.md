# 🚀 AI Video Editor - Deployment Instructions

## 🛠️ 1. Build `.exe` with PyInstaller
### Requirements:
- Python 3.10+
- pip install pyinstaller

### Build Command:
```bash
pyinstaller pyinstaller.spec
```

Output is in `dist/AI_Video_Editor/`

---

## 🌐 2. Run as Streamlit Web App (Local or Cloud)

### Install:
```bash
pip install -r requirements.txt
pip install streamlit
```

### Run:
```bash
streamlit run streamlit_app.py
```

---

## ☁️ 3. Deploy to Streamlit Cloud (Free)
1. Push code to GitHub
2. Visit: https://share.streamlit.io/
3. Link repo + set file as: `streamlit_app.py`
4. Click “Deploy”

---

## 🎤 Optional: Deploy to Hugging Face or Render
See platform docs:
- https://huggingface.co/spaces
- https://render.com/deploy

---

Happy Editing!
