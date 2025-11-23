import asyncio
import os
import logging
import edge_tts
from config import AUDIO_ASSETS_DIR, RUNTIME_LOGS_DIR

# Define voice mappings
# Using expressive male voices that are somewhat similar in tone
PETER_VOICE = "en-US-GuyNeural"  # A generic American male voice
STEWIE_VOICE = (
    "en-GB-RyanNeural"  # A British male voice (since Stewie has a British accent)
)


class VoiceGenerator:
    """
    Generates audio using the edge-tts library (Microsoft Edge's free online TTS).
    No Selenium, no API keys, no rate limits (within reason).
    """

    def __init__(self, proxy: str = None) -> None:
        self.output_dir = AUDIO_ASSETS_DIR
        os.makedirs(self.output_dir, exist_ok=True)
        self.setup_logging()
        self.proxy = proxy

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

        self.logger.info("Logging initialized (edge-tts version).")

    async def _generate_audio_file(
        self, text: str, voice: str, output_file: str
    ) -> None:
        """
        Internal async method to generate audio using edge-tts.
        """
        try:
            communicate = edge_tts.Communicate(text, voice, proxy=self.proxy)
            await communicate.save(output_file)
        except Exception as e:
            self.logger.error(f"Error in edge-tts generation: {e}")
            raise

    def generate_audio(self, text: str, speaker: str, index: int) -> str:
        """
        Generates audio for a given text and speaker.
        Returns the path to the generated audio file.
        """
        try:
            # Select voice based on speaker name
            voice = PETER_VOICE if speaker.lower() == "peter" else STEWIE_VOICE

            filename = f"{speaker.lower()}_audio_{index}.mp3"
            output_path = os.path.join(self.output_dir, filename)

            self.logger.info(
                f"Generating audio for '{speaker}' using voice '{voice}'..."
            )

            # Run the async generation in a synchronous wrapper
            asyncio.run(self._generate_audio_file(text, voice, output_path))

            self.logger.info(f"Audio saved successfully at: {output_path}")
            return output_path

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
