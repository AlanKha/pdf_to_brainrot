import os
import re
import shutil
import logging
from datetime import datetime
from typing import List


class Utils:
    """
    A utility class providing common helper functions for various tasks.
    """

    @staticmethod
    def get_ordered_audio_files(folder_path: str) -> List[str]:
        """
        Returns a list of .mp3 filenames from the folder, ordered by the number in the filename.

        Args:
            folder_path (str): The directory path to search for audio files.

        Returns:
            List[str]: A list of sorted filenames.

        Example:
            Input: ['peter_audio_1.mp3', 'stewie_audio_2.mp3', 'peter_3.mp3']
            Output: ['peter_audio_1.mp3', 'stewie_audio_2.mp3', 'peter_3.mp3']
        """
        try:
            if not os.path.exists(folder_path):
                logging.warning(f"Folder not found: {folder_path}")
                return []

            audio_files = [
                f
                for f in os.listdir(folder_path)
                if os.path.isfile(os.path.join(folder_path, f)) and f.endswith(".mp3")
            ]

            def extract_number(filename: str) -> float:
                match = re.search(r"(\d+)", filename)
                return int(match.group(1)) if match else float("inf")

            sorted_files = sorted(audio_files, key=extract_number)
            return sorted_files

        except OSError as e:
            logging.error(
                f"[Utils] Error reading audio files from '{folder_path}': {e}"
            )
            return []

    @staticmethod
    def archive_audio_assets(
        source_dir: str = "audio_assests", archive_root: str = "archives_audios"
    ) -> None:
        """
        Moves all files from 'audio_assets/' to 'archive/YYYY-MM-DD/' and ensures the source folder is empty.

        Args:
            source_dir (str): Directory to archive files from.
            archive_root (str): Root directory to store archives.
        """
        today_str = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        target_dir = os.path.join(archive_root, today_str)

        try:
            if not os.path.exists(source_dir):
                logging.warning(
                    f"Source directory for archiving does not exist: {source_dir}"
                )
                return

            os.makedirs(target_dir, exist_ok=True)

            files = os.listdir(source_dir)
            if not files:
                logging.info("No files to archive.")
                return

            for filename in files:
                src_path = os.path.join(source_dir, filename)
                if os.path.isfile(src_path):
                    shutil.move(src_path, os.path.join(target_dir, filename))

            logging.info(f"Archived {len(files)} files to {target_dir}.")
        except OSError as e:
            logging.error(f"[Utils] Error archiving audio assets: {e}")
