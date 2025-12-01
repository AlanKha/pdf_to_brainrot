import os
import logging
import torch
from TTS.api import TTS
from TTS.utils import io
from TTS.utils.generic_utils import get_user_data_dir
from pydub import AudioSegment
from config import AUDIO_ASSETS_DIR, RUNTIME_LOGS_DIR
import string
import fsspec

# Voice sample paths
PETER_VOICE_SAMPLE = "video_assests/peter.mp3"
STEWIE_VOICE_SAMPLE = "video_assests/stewie.mp3"


def _patch_load_fsspec():
    """
    Monkey patch TTS.utils.io.load_fsspec to fix PyTorch 2.6+ compatibility.
    PyTorch 2.6+ changed torch.load default to weights_only=True, which breaks
    loading TTS checkpoints that contain custom classes.
    """

    def patched_load_fsspec(path, map_location=None, cache=True, **kwargs):
        """Patched version that adds weights_only=False for PyTorch 2.6+ compatibility"""
        # Ensure weights_only is False if not explicitly set
        if "weights_only" not in kwargs:
            kwargs["weights_only"] = False

        is_local = os.path.isdir(path) or os.path.isfile(path)
        if cache and not is_local:
            with fsspec.open(
                f"filecache::{path}",
                filecache={"cache_storage": str(get_user_data_dir("tts_cache"))},
                mode="rb",
            ) as f:
                return torch.load(f, map_location=map_location, **kwargs)
        else:
            with fsspec.open(path, "rb") as f:
                return torch.load(f, map_location=map_location, **kwargs)

    io.load_fsspec = patched_load_fsspec


# Apply the patch before importing TTS model
_patch_load_fsspec()


class VoiceGenerator:
    """
    Generates audio using Coqui TTS XTTS v2 for voice cloning.
    Clones voices from peter.mp3 and stewie.mp3 samples.
    """

    def __init__(self, proxy: str = None) -> None:
        self.output_dir = AUDIO_ASSETS_DIR
        os.makedirs(self.output_dir, exist_ok=True)
        self.proxy = proxy  # Not used with XTTS, but kept for compatibility
        self.setup_logging()

        # Setup device (use GPU if available)
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.logger.info(f"Using device: {self.device}")

        # Load XTTS v2 model (will download ~2GB on first run)
        self.logger.info("Loading XTTS v2 model...")
        self.tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2").to(self.device)
        self.logger.info("XTTS v2 model loaded successfully.")

        # Convert and cache voice samples
        self.peter_wav = self._prepare_voice_sample(PETER_VOICE_SAMPLE, "peter")
        self.stewie_wav = self._prepare_voice_sample(STEWIE_VOICE_SAMPLE, "stewie")

    def setup_logging(self) -> None:
        """Set up logging configuration"""
        os.makedirs(RUNTIME_LOGS_DIR, exist_ok=True)
        self.logger = logging.getLogger("VoiceGenerator")
        self.logger.setLevel(logging.DEBUG)

        if not self.logger.handlers:
            log_file = os.path.join(RUNTIME_LOGS_DIR, "voice_generator.log")
            handler = logging.FileHandler(log_file)
            handler.setLevel(logging.DEBUG)
            formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
            handler.setFormatter(formatter)
            self.logger.addHandler(handler)

        self.logger.info("Logging initialized (XTTS v2 voice cloning version).")

    def _prepare_voice_sample(self, mp3_path: str, speaker_name: str) -> str:
        """
        Converts MP3 voice sample to WAV format for XTTS.
        Returns path to the WAV file.
        """
        if not os.path.exists(mp3_path):
            raise FileNotFoundError(
                f"Voice sample not found: {mp3_path}. "
                f"Please ensure {speaker_name}.mp3 exists in video_assests/ directory."
            )

        # Create a cache directory for converted samples
        cache_dir = os.path.join(self.output_dir, "voice_samples_cache")
        os.makedirs(cache_dir, exist_ok=True)

        wav_path = os.path.join(cache_dir, f"{speaker_name}_sample.wav")

        # Convert MP3 to WAV if not already converted
        if not os.path.exists(wav_path):
            self.logger.info(f"Converting {mp3_path} to WAV format...")
            audio = AudioSegment.from_mp3(mp3_path)
            audio.export(wav_path, format="wav")
            self.logger.info(f"Voice sample converted: {wav_path}")

        return wav_path

    def generate_audio(self, text: str, speaker: str, index: int) -> str:
        """
        Generates audio for a given text and speaker using voice cloning.
        Returns the path to the generated audio file (MP3 format).
        """
        try:
            # Clean text
            text = "".join(
                c
                for c in text
                if (c.isalnum() or c in string.punctuation or c.isspace()) and c != "*"
            )

            # Select voice sample based on speaker name
            speaker_lower = speaker.lower()
            if speaker_lower == "peter":
                speaker_wav = self.peter_wav
            elif speaker_lower == "stewie":
                speaker_wav = self.stewie_wav
            else:
                self.logger.warning(
                    f"Unknown speaker '{speaker}', defaulting to peter voice."
                )
                speaker_wav = self.peter_wav

            # Generate WAV file first
            wav_filename = f"{speaker_lower}_audio_{index}.wav"
            wav_output_path = os.path.join(self.output_dir, wav_filename)

            # Final MP3 output path
            mp3_filename = f"{speaker_lower}_audio_{index}.mp3"
            mp3_output_path = os.path.join(self.output_dir, mp3_filename)

            self.logger.info(
                f"Generating audio for '{speaker}' using voice cloning from {speaker_wav}..."
            )

            # Generate audio using XTTS v2
            self.tts.tts_to_file(
                text=text,
                speaker_wav=speaker_wav,
                language="en",
                file_path=wav_output_path,
            )

            # Convert WAV to MP3 for compatibility with video_editor
            self.logger.info(f"Converting {wav_filename} to MP3...")
            audio = AudioSegment.from_wav(wav_output_path)
            audio.export(mp3_output_path, format="mp3")

            # Clean up temporary WAV file
            if os.path.exists(wav_output_path):
                os.remove(wav_output_path)

            self.logger.info(f"Audio saved successfully at: {mp3_output_path}")
            return mp3_output_path

        except Exception as e:
            self.logger.error(f"Failed to generate audio: {e}")
            raise

    def process_conversation(self, line: str, dialogue_id: int) -> bool:
        """
        Process a single conversation line to generate an audio file.
        Matches the interface expected by main.py.
        """
        try:
            if ":" not in line:
                self.logger.warning(f"Skipping malformed line: '{line}'")
                return False

            speaker, sentence = map(str.strip, line.split(":", 1))

            self.logger.info(
                f"Processing line {dialogue_id}: {speaker} says '{sentence}'"
            )

            # Generate the audio
            self.generate_audio(sentence, speaker, dialogue_id)

            return True

        except Exception as e:
            self.logger.error(f"Error processing conversation ID {dialogue_id}: {e}")
            return False
