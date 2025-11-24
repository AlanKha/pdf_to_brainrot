from typing import List, Dict, Any
import os
import textwrap
from moviepy import (
    VideoFileClip,
    AudioFileClip,
    CompositeAudioClip,
    CompositeVideoClip,
    ImageClip,
    TextClip,
)
from moviepy.video.fx import speedx
import PIL.Image

if not hasattr(PIL.Image, "ANTIALIAS"):
    PIL.Image.ANTIALIAS = PIL.Image.LANCZOS


class DynamicVideoEditor:
    """
    Edits the video by combining background video, audio, character avatars, and subtitles.
    """

    def __init__(
        self,
        video_path: str,
        output_path: str,
        dialogue_data: List[Dict[str, Any]],
        video_title: str = "PDF to Brainrot",
        title_sound_path: str = "audio_assests/title_sound.mp3",
    ) -> None:
        self.video_path = video_path
        self.output_path = output_path
        self.dialogue_data = dialogue_data
        self.video_title = video_title
        self.title_sound_path = title_sound_path
        self.audio_clips: List[AudioFileClip] = []
        self.image_clips: List[ImageClip] = []
        self.subtitle_clips: List[TextClip] = []
        self.current_start: float = 0.0

        # Load video - use the full duration to avoid black screens
        # Skip first 10 seconds to avoid any intro/transition
        full_video = VideoFileClip(video_path)
        self.video = full_video.subclipped(10, full_video.duration).fx(speedx, 2.0)

    def create_title_clip(self, text: str, duration: float) -> TextClip:
        return TextClip(
            text=text,
            font_size=60,
            color="white",
            text_align="center",
            size=(self.video.w - 200, 500),
        ).with_duration(duration)

    def add_full_sentence_subtitle(
        self, text: str, start_time: float, duration: float
    ) -> TextClip:
        """Create a subtitle clip showing the full sentence at once."""
        if not text:
            return None

        # Remove all non-alphanumeric and non-punctuation characters from text, and also remove asterisks
        import string
        text = "".join(c for c in text if (c.isalnum() or c in string.punctuation or c.isspace()) and c != "*")

        # Wrap text at word boundaries to prevent mid-word breaks
        # Approximate character width based on font size (rough estimate)
        chars_per_line = int(
            (self.video.w - 200) / 30
        )  # ~30 pixels per char at font_size=50
        wrapped_text = textwrap.fill(text, width=chars_per_line, break_long_words=False)

        clip = (
            TextClip(
                text=wrapped_text,
                font_size=50,
                color="white",
                stroke_color="black",
                stroke_width=4.0,
                vertical_align="center",
                text_align="center",
                horizontal_align="center",
                method="caption",
                size=(self.video.w - 200, 500),
            )
            .with_start(start_time)
            .with_duration(duration)
            .with_position(("center", self.video.h // 2))
        )
        return clip

    def edit(self) -> None:
        # Add title clip at the beginning
        title_duration = 1.0
        title_clip = (
            self.create_title_clip(self.video_title, title_duration)
            .with_start(0)
            .with_position("center")
        )
        self.subtitle_clips.append(title_clip)

        # Add title sound effect
        if os.path.exists(self.title_sound_path):
            title_audio = AudioFileClip(self.title_sound_path).with_start(0)
            self.audio_clips.append(title_audio)
        else:
            print(f"Title sound not found: {self.title_sound_path}")

        self.current_start = title_duration + 0.5

        for item in self.dialogue_data:
            # Construct audio path
            # The ID is added in main.py
            audio_filename = f"{item['character'].lower()}_audio_{item['id']}.mp3"
            audio_path = os.path.join("audio_assests", audio_filename)

            if not os.path.exists(audio_path):
                print(f"Audio file not found: {audio_path}, skipping.")
                continue

            # Construct Avatar Image Path
            image_path = f"image_assests/{item['image']}"

            subtitle_text = item["sentence"]

            # Load and position audio
            audio = AudioFileClip(audio_path).with_start(self.current_start)
            self.audio_clips.append(audio)

            # Position character image
            char_position = "left" if "peter" in image_path.lower() else "right"
            if os.path.exists(image_path):
                char_image = (
                    ImageClip(image_path)
                    .with_start(self.current_start)
                    .with_duration(audio.duration)
                    .resized(height=500)
                )

                y_position = max(0, self.video.h - 500 - 50)
                x_position = (
                    50
                    if char_position == "left"
                    else max(0, self.video.w - char_image.w - 50)
                )

                char_image = char_image.with_position((x_position, y_position))
                self.image_clips.append(char_image)
            else:
                print(f"Avatar image not found: {image_path}")

            # Subtitle
            subtitle_clip = self.add_full_sentence_subtitle(
                subtitle_text, self.current_start, audio.duration
            )
            if subtitle_clip:
                self.subtitle_clips.append(subtitle_clip)

            # Context Image (The one searched for)
            # Expecting 'context_image_path' to be populated by main.py if search was successful
            context_image_path = item.get("context_image_path")
            if context_image_path and os.path.exists(context_image_path):
                try:
                    searched_image = (
                        ImageClip(context_image_path)
                        .with_start(self.current_start)
                        .with_duration(audio.duration)
                        .resized(height=600)
                        .with_position(("center", 300))
                    )
                    self.image_clips.append(searched_image)
                except Exception as e:
                    print(f"Failed to process context image {context_image_path}: {e}")

            self.current_start += audio.duration + 0.5

        # Combine all clips
        if not self.audio_clips:
            print("No audio clips generated. Aborting video creation.")
            return

        # Include background video audio if it exists
        all_audio_clips = self.audio_clips.copy()
        if self.video.audio is not None:
            all_audio_clips.append(self.video.audio)

        final_audio = CompositeAudioClip(all_audio_clips)

        # Filter out None clips if any
        visual_clips = [self.video] + self.image_clips + self.subtitle_clips

        final_video = CompositeVideoClip(visual_clips).with_audio(final_audio)

        # Trim video to audio duration
        final_video = final_video.with_duration(self.current_start)

        final_video.write_videofile(
            self.output_path, codec="libx264", audio_codec="aac", fps=24
        )
