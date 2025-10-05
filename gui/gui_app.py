import tkinter as tk
from tkinter import filedialog, messagebox
from editor.editing_panel import EditingPanel
from editor.export_system import ExportSystem

class VideoEditorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("AI Video Editor")
        self.editor = EditingPanel()
        self.exporter = ExportSystem()
        self.video_path = None

        self.label = tk.Label(master, text="Select a video file:")
        self.label.pack(pady=5)

        self.select_button = tk.Button(master, text="Browse", command=self.load_video)
        self.select_button.pack(pady=5)

        self.color_button = tk.Button(master, text="Apply Color Grading", command=self.apply_color_grading)
        self.color_button.pack(pady=5)

        self.hook_button = tk.Button(master, text="Detect Hook", command=self.detect_hook)
        self.hook_button.pack(pady=5)

        self.speed_button = tk.Button(master, text="Apply Speed Control", command=self.apply_speed_control)
        self.speed_button.pack(pady=5)

        self.transition_button = tk.Button(master, text="Apply Visual Transitions", command=self.apply_transitions)
        self.transition_button.pack(pady=5)

        self.export_button = tk.Button(master, text="Export Final Video", command=self.export_video)
        self.export_button.pack(pady=10)

    def load_video(self):
        self.video_path = filedialog.askopenfilename(title="Select Video", filetypes=[("Video Files", "*.mp4 *.mov *.mkv")])
        if self.video_path:
            messagebox.showinfo("Video Loaded", f"Loaded: {self.video_path}")

    def apply_color_grading(self):
        if self.video_path:
            self.editor.color_grading(self.video_path)
            messagebox.showinfo("Done", "Color grading applied.")

    def detect_hook(self):
        if self.video_path:
            self.editor.hook_detection(self.video_path)
            messagebox.showinfo("Done", "Hook detected.")

    def apply_speed_control(self):
        if self.video_path:
            self.editor.speed_control(self.video_path, speed_factor=1.5)
            messagebox.showinfo("Done", "Speed adjusted.")

    def apply_transitions(self):
        if self.video_path:
            self.editor.visual_transitions([self.video_path])
            messagebox.showinfo("Done", "Transitions applied.")

    def export_video(self):
        if self.video_path:
            output_path = filedialog.askdirectory(title="Select Export Folder")
            if output_path:
                self.exporter.export_video(self.video_path, save_path=output_path)
                messagebox.showinfo("Exported", "Video exported successfully.")

if __name__ == "__main__":
    root = tk.Tk()
    app = VideoEditorApp(root)
    root.mainloop()
