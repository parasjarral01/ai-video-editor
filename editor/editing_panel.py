class EditingPanel:
    def hook_detection(self, video_path: str, hook_length_sec: int = 5, confidence_threshold: float = 0.7):
        import cv2
        import numpy as np

        cap = cv2.VideoCapture(video_path)
        fps = cap.get(cv2.CAP_PROP_FPS)
        total_frames = int(min(cap.get(cv2.CAP_PROP_FRAME_COUNT), fps * 20))  # Analyze only first 20s

        prev_gray = None
        motion_scores = []
        brightness_scores = []
        scene_cuts = []

        for i in range(total_frames):
            ret, frame = cap.read()
            if not ret:
                break

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            brightness_scores.append(np.mean(gray))

            if prev_gray is not None:
                flow = cv2.calcOpticalFlowFarneback(prev_gray, gray, None, 0.5, 3, 15, 3, 5, 1.2, 0)
                mag, _ = cv2.cartToPolar(flow[..., 0], flow[..., 1])
                motion_scores.append(np.mean(mag))

                diff = cv2.absdiff(prev_gray, gray)
                if np.mean(diff) > 30:
                    scene_cuts.append(i)

            prev_gray = gray

        cap.release()

        def normalize(arr):
            arr = np.array(arr)
            return (arr - np.min(arr)) / (np.ptp(arr) + 1e-5)

        motion_scores = normalize(motion_scores)
        brightness_scores = normalize(brightness_scores)
        engagement_scores = 0.5 * motion_scores[:len(brightness_scores)] + 0.5 * brightness_scores

        window_size = int(fps * hook_length_sec)
        max_score = 0
        best_frame = 0
        for i in range(len(engagement_scores) - window_size):
            score = np.mean(engagement_scores[i:i + window_size])
            if score > max_score:
                max_score = score
                best_frame = i

        best_time = best_frame / fps
        print(f"[HOOK DETECTED] Start at {best_time:.2f}s with score {max_score:.2f}")
        return best_time

    def color_grading(self, video_path: str, grading_style: str = "cinematic", intensity: float = 0.8):
        import cv2
        import numpy as np

        cap = cv2.VideoCapture(video_path)
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        out_path = "graded_output.mp4"
        fps = cap.get(cv2.CAP_PROP_FPS)
        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        out = cv2.VideoWriter(out_path, fourcc, fps, (width, height))

        while True:
            ret, frame = cap.read()
            if not ret:
                break

            if grading_style == "cinematic":
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
                frame[:, :, 2] = cv2.equalizeHist(frame[:, :, 2])
                frame = cv2.cvtColor(frame, cv2.COLOR_HSV2BGR)

            elif grading_style == "vibrant":
                lab = cv2.cvtColor(frame, cv2.COLOR_BGR2LAB)
                l, a, b = cv2.split(lab)
                l = cv2.equalizeHist(l)
                lab = cv2.merge((l, a, b))
                frame = cv2.cvtColor(lab, cv2.COLOR_LAB2BGR)

            frame = cv2.convertScaleAbs(frame, alpha=1 + intensity * 0.3, beta=10 * intensity)
            out.write(frame)

        cap.release()
        out.release()
        print(f"[COLOR GRADING DONE] Saved to {out_path}")

    def speed_control(self, video_path: str, speed_factor: float = 1.0, apply_to_segments: bool = False, auto_sync_to_audio: bool = False):
        from moviepy.editor import VideoFileClip

        clip = VideoFileClip(video_path)
        new_clip = clip.fx(VideoFileClip.speedx, speed_factor)
        output_path = "speed_adjusted.mp4"
        new_clip.write_videofile(output_path, codec="libx264", audio_codec="aac")
        print(f"[SPEED CONTROL DONE] Saved to {output_path}")

    def visual_transitions(self, clips: list, transition_type: str = "fade", duration_sec: float = 1.0):
        from moviepy.editor import concatenate_videoclips, VideoFileClip

        video_clips = [VideoFileClip(c) for c in clips]
        final = concatenate_videoclips(video_clips, method="compose")
        output_path = "transition_output.mp4"
        final.write_videofile(output_path, codec="libx264", audio_codec="aac")
        print(f"[TRANSITIONS DONE] Saved to {output_path}")
