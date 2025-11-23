import os
import logging
import shutil
from typing import List, Dict, Any

from voice_generator import VoiceGenerator
from video_editor import DynamicVideoEditor
from image_downloader import ImageDownloader
from config import (
    DIALOGUE,
    VIDEO_TEMPLATE_PATH,
    OUTPUT_VIDEO_PATH,
    AUDIO_ASSETS_DIR,
    IMAGE_ASSETS_DIR,
    DOWNLOADED_IMAGES_DIR,
    RUNTIME_LOGS_DIR,
    VIDEO_TITLE,
    TITLE_SOUND_PATH,
)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler(
            os.path.join(RUNTIME_LOGS_DIR, "flow_log.log")
            if os.path.exists(RUNTIME_LOGS_DIR)
            else "flow.log"
        ),
    ],
)


def setup_directories() -> None:
    """Sets up necessary directories for the project."""
    if os.path.exists(AUDIO_ASSETS_DIR):
        shutil.rmtree(AUDIO_ASSETS_DIR)
    os.makedirs(AUDIO_ASSETS_DIR, exist_ok=True)

    os.makedirs(IMAGE_ASSETS_DIR, exist_ok=True)
    if not os.path.exists(
        os.path.join(IMAGE_ASSETS_DIR, "peter.png")
    ) or not os.path.exists(os.path.join(IMAGE_ASSETS_DIR, "stewie.png")):
        logging.warning(
            f"Make sure '{IMAGE_ASSETS_DIR}' contains 'peter.png' and 'stewie.png'."
        )

    if os.path.exists(DOWNLOADED_IMAGES_DIR):
        shutil.rmtree(DOWNLOADED_IMAGES_DIR)
    os.makedirs(DOWNLOADED_IMAGES_DIR, exist_ok=True)

    os.makedirs(RUNTIME_LOGS_DIR, exist_ok=True)


def main() -> None:
    # 1. Setup
    setup_directories()

    # 2. Initialize Tools
    voice_generator = VoiceGenerator()
    image_downloader = ImageDownloader(
        max_images=1, download_folder=DOWNLOADED_IMAGES_DIR
    )

    processed_dialogue: List[Dict[str, Any]] = []

    # 3. Process Dialogue (Audio & Images)
    logging.info("Starting audio generation and image gathering...")

    for idx, item in enumerate(DIALOGUE):
        # A. Generate Audio
        line = f"{item['character']}: {item['sentence']}"
        logging.info(f"Processing line {idx}: {line}")

        success = voice_generator.process_conversation(line, idx)

        if success:
            item_data = item.copy()
            item_data["id"] = idx

            # B. Download Context Image
            search_term = item.get("image_search")
            if search_term:
                logging.info(f"Searching for image: {search_term}")
                images = image_downloader.search_images(search_term)
                if images:
                    item_data["context_image_path"] = images[0]
                else:
                    logging.warning(f"No image found for: {search_term}")

            processed_dialogue.append(item_data)
        else:
            logging.error(f"Failed to generate audio for line {idx}: {line}")
            logging.error("Aborting video generation due to audio failure.")
            return

    logging.info("Audio and Image processing completed.")

    # 4. Edit Video
    logging.info("Starting video editing...")

    if not os.path.exists(VIDEO_TEMPLATE_PATH):
        logging.error(
            f"Video template not found at {VIDEO_TEMPLATE_PATH}. Please provide a background video."
        )
        return

    editor = DynamicVideoEditor(
        video_path=VIDEO_TEMPLATE_PATH,
        output_path=OUTPUT_VIDEO_PATH,
        dialogue_data=processed_dialogue,
        video_title=VIDEO_TITLE,
        title_sound_path=TITLE_SOUND_PATH,
    )

    try:
        editor.edit()
        logging.info(f"Video created successfully: {OUTPUT_VIDEO_PATH}")
    except Exception as e:
        logging.error(f"Error during video editing: {e}")


if __name__ == "__main__":
    main()
