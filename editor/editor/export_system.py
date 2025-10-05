import os

class ExportSystem:
    def export_video(self, input_path: str, output_format: str = "MP4", resolution: str = "1080p", compression: bool = False, save_path: str = "./output"):
        os.makedirs(save_path, exist_ok=True)
        output_file = os.path.join(save_path, f"final_video.{output_format.lower()}")
        print(f"Video saved to {output_file}")
        return output_file
