class PromptVideoGenerator:
    def prompt_to_video(self, prompt: str, duration_limit_sec: int = 120, music_style: str = "cinematic", voiceover_enabled: bool = False):
        keywords = prompt.lower().split()
        visuals = self.fetch_visuals_from_pexels(keywords)
        return "generated_video.mp4"

    def fetch_visuals_from_pexels(self, keywords: list):
        return ["visual1.mp4", "visual2.mp4"]
