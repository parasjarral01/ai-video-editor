from editor.editing_panel import EditingPanel
from editor.metadata_generator import MetadataGenerator
from editor.thumbnail_generator import ThumbnailGenerator
from editor.prompt_video_generator import PromptVideoGenerator
from editor.translator import Translator
from editor.export_system import ExportSystem

class AIVideoEditor:
    def __init__(self):
        self.editor = EditingPanel()
        self.metadata = MetadataGenerator()
        self.thumbnail = ThumbnailGenerator()
        self.prompt_gen = PromptVideoGenerator()
        self.translator = Translator()
        self.exporter = ExportSystem()

    def full_pipeline(self, video_path: str, prompt: str = None):
        self.editor.color_grading(video_path)
        meta = self.metadata.generate_metadata("sample transcript")
        print("Metadata:", meta)
        thumbs = self.thumbnail.generate_thumbnails(video_path)
        print("Thumbnails:", thumbs)
        self.translator.translate_and_dub(video_path, target_languages=["es", "fr"])
        final_path = self.exporter.export_video(video_path)
        print("Exported to:", final_path)

if __name__ == "__main__":
    editor = AIVideoEditor()
    editor.full_pipeline("sample_video.mp4")
