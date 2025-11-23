import os
import logging
import requests
from typing import List
from ddgs import DDGS
from config import RUNTIME_LOGS_DIR, DOWNLOADED_IMAGES_DIR


class ImageDownloader:
    """
    Handles searching and downloading images using DuckDuckGo.
    """

    def __init__(
        self, max_images: int = 10, download_folder: str = DOWNLOADED_IMAGES_DIR
    ) -> None:
        """
        Initialize the ImageDownloader.

        Args:
            max_images (int): Maximum number of images to download per search term.
            download_folder (str): Directory to save downloaded images.
        """
        self.max_images = max_images
        self.download_folder = download_folder

        # Create required folders
        os.makedirs(self.download_folder, exist_ok=True)
        self._setup_logging()

    def _setup_logging(self) -> None:
        """Sets up the logger for this class."""
        os.makedirs(RUNTIME_LOGS_DIR, exist_ok=True)
        log_path = os.path.join(RUNTIME_LOGS_DIR, "image_downloader.log")

        self.logger = logging.getLogger("ImageDownloader")
        self.logger.setLevel(logging.DEBUG)

        # Prevent adding multiple handlers if instantiated multiple times
        if not self.logger.handlers:
            file_handler = logging.FileHandler(log_path)
            formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
            file_handler.setFormatter(formatter)
            self.logger.addHandler(file_handler)

        self.logger.info("Logger initialized.")

    def search_images(self, term: str) -> List[str]:
        """
        Search for images and download them.

        Args:
            term (str): The search keyword.

        Returns:
            List[str]: A list of file paths for the downloaded images.
        """
        self.logger.info(f"Starting search for: {term}")
        downloaded_image_paths: List[str] = []

        try:
            # Add a delay to respect rate limits if necessary, though DDGS handles some internally
            # Using a fresh DDGS instance for each search
            with DDGS() as ddgs:
                # ddgs.images returns an iterator of dicts
                # Added error handling specifically for the generator
                try:
                    search_results = ddgs.images(
                        query=term, max_results=self.max_images
                    )
                    # search_results is a generator, so we iterate directly
                    for idx, item in enumerate(search_results):
                        url = item.get("image")
                        if not url:
                            continue

                        try:
                            self.logger.info(f"Downloading image {idx + 1}: {url}")
                            # Add a generic user-agent to avoid basic blocking
                            headers = {
                                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
                            }
                            response = requests.get(url, timeout=10, headers=headers)
                            response.raise_for_status()

                            # Sanitize filename
                            safe_term = "".join(
                                c for c in term if c.isalnum() or c in (" ", "_")
                            ).rstrip()
                            img_name = f"{safe_term.replace(' ', '_')}_{idx + 1}.jpg"
                            img_path = os.path.join(self.download_folder, img_name)

                            with open(img_path, "wb") as img_file:
                                img_file.write(response.content)

                            downloaded_image_paths.append(img_path)

                        except requests.RequestException as e:
                            self.logger.error(f"Request error for image {idx + 1}: {e}")
                        except Exception as e:
                            self.logger.error(
                                f"Failed to download image {idx + 1}: {e}"
                            )

                except Exception as e:
                    self.logger.error(f"Error retrieving search results: {e}")

        except Exception as e:
            self.logger.critical(f"Image search failed: {e}")

        self.logger.info(
            f"Downloaded {len(downloaded_image_paths)} images successfully."
        )
        return downloaded_image_paths
