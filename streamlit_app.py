import streamlit as st
from editor.editing_panel import EditingPanel
from editor.thumbnail_generator import ThumbnailGenerator
from editor.translator import Translator
from editor.export_system import ExportSystem
from PIL import Image
import tempfile
import os

st.title("🎬 AI Video Editor (Streamlit Edition)")

uploaded_file = st.file_uploader("Upload a video", type=["mp4", "mov", "mkv"])
editor = EditingPanel()
thumb_gen = ThumbnailGenerator()
translator = Translator()
exporter = ExportSystem()

if uploaded_file:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp4") as temp_video:
        temp_video.write(uploaded_file.read())
        video_path = temp_video.name

    st.video(video_path)

    st.markdown("### ✨ Choose Enhancements:")
    if st.button("Apply Color Grading"):
        editor.color_grading(video_path)
        st.success("Color grading applied.")

    if st.button("Detect Hook"):
        start = editor.hook_detection(video_path)
        st.success(f"Hook detected starting at {start:.2f} seconds.")

    if st.button("Generate Thumbnails"):
        thumbs = thumb_gen.generate_thumbnails(video_path)
        for img in thumbs:
            if os.path.exists(img):
                image = Image.open(img)
                st.image(image, caption=img)
            else:
                st.warning(f"Thumbnail {img} not found.")

    if st.button("Translate & Dub (Spanish)"):
        translator.translate_and_dub(video_path, ["es"])
        st.success("Dubbed video generated.")

    if st.button("Export Final Video"):
        out_path = exporter.export_video(video_path)
        st.success(f"Exported to {out_path}")
        if os.path.exists(out_path):
            with open(out_path, "rb") as f:
                st.download_button("Download Exported Video", f, file_name="final_video.mp4")
