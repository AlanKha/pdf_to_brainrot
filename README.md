# PDF to Brainrot 🧠🎮

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

An automated video generator that transforms educational content into engaging "brainrot" style videos featuring **Peter Griffin** and **Stewie Griffin** from Family Guy. Perfect for creating TikTok/YouTube Shorts style educational content with background gameplay footage and AI-generated dialogue.

## 🎥 What is "Brainrot" Content?

"Brainrot" refers to highly engaging, fast-paced social media videos that combine:

- 🎮 Background gameplay footage (Minecraft, Subway Surfers, etc.)
- 🗣️ AI-generated dialogue or narration
- 📝 Word-by-word subtitles
- 🖼️ Dynamic contextual images

This style has become incredibly popular on platforms like TikTok and YouTube Shorts for educational content, keeping viewers engaged while learning.

## ✨ Features

### 🎙️ AI Voice Generation

- Powered by **Microsoft Edge TTS** (`edge-tts`) for high-quality, free neural voices
- Peter Griffin voice: `en-US-GuyNeural`
- Stewie Griffin voice: `en-GB-RyanNeural`
- No API costs or rate limits

### 🎬 Dynamic Video Editing

- Automatic character overlay positioning (left/right alternating)
- Word-by-word subtitle generation for maximum engagement
- Seamless audio-video synchronization
- Background video looping (Subway Surfers, Minecraft, etc.)

### 🖼️ Contextual Image Search

- Automated image searching via DuckDuckGo
- Context-aware image placement based on dialogue content
- Automatic image downloading and caching
- Smart image overlay timing

### ⚡ Fast & Modular

- Clean, type-hinted codebase
- Modular architecture for easy customization
- Comprehensive logging for debugging
- Parallel processing where possible

## 📁 Project Structure

```txt
pdf_to_brainrot/
├── main.py                   # Entry point - orchestrates the entire pipeline
├── config.py                 # Configuration, paths, and dialogue script
├── voice_generator.py        # Text-to-speech audio generation
├── image_downloader.py       # Image search and download
├── video_editor.py           # Video composition and editing
├── utils.py                  # Helper functions
├── requirements.txt          # Python dependencies
├── CHANGELOG.md             # Project history
│
├── audio_assests/           # Generated audio files (auto-created)
├── image_assests/           # Character images (peter.png, stewie.png)
├── downloaded_images/       # Downloaded context images (auto-created)
├── video_assests/           # Background videos (minecraft, subway surfers)
├── runtime_logs/            # Application logs (auto-created)
└── output_final_video.mp4   # Final generated video
```

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- ImageMagick (required for text rendering)
- ~500MB free disk space

### Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/yourusername/pdf_to_brainrot.git
   cd pdf_to_brainrot
   ```

2. **Create a virtual environment (recommended)**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Python dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Install ImageMagick**
   - **macOS:**

     ```bash
     brew install imagemagick
     ```

   - **Ubuntu/Debian:**

     ```bash
     sudo apt update && sudo apt install imagemagick
     ```

   - **Windows:**
     Download from [imagemagick.org](https://imagemagick.org/script/download.php)
     - ⚠️ Important: Check "Install legacy utilities (e.g., convert)" during installation

5. **Verify installation**

   ```bash
   python -c "import edge_tts; print('✓ edge-tts installed')"
   python -c "import moviepy; print('✓ moviepy installed')"
   convert -version  # Should show ImageMagick version
   ```

### Basic Usage

1. **Prepare your assets**
   - Add character images to `image_assests/`:
     - `peter.png` (Peter Griffin character image)
     - `stewie.png` (Stewie Griffin character image)
   - Add background video to `video_assests/`:
     - `minecraft_background.mp4` or `subway_surfers.mp4`

2. **Edit the dialogue script**
   Open `config.py` and modify the `DIALOGUE` list:

   ```python
   DIALOGUE = [
       {
           "character": "Peter",
           "sentence": "Hey Stewie, let me explain this cool thing...",
           "image_search": "peter griffin explaining something",
           "image": "peter.png",
           "id": None,
       },
       {
           "character": "Stewie",
           "sentence": "Fascinating. Let me add some technical details...",
           "image_search": "stewie griffin with blueprints",
           "image": "stewie.png",
           "id": None,
       },
   ]
   ```

3. **Run the generator**

   ```bash
   python main.py
   ```

4. **Find your video**
   The final video will be saved as `output_final_video.mp4` in the project root.

## ⚙️ Configuration

All configuration is centralized in `config.py`:

### File Paths

```python
VIDEO_TEMPLATE_PATH = "video_assests/minecraft_background.mp4"  # Background video
OUTPUT_VIDEO_PATH = "output_final_video.mp4"                    # Output filename
AUDIO_ASSETS_DIR = "audio_assests"                              # Generated audio
IMAGE_ASSETS_DIR = "image_assests"                              # Character images
DOWNLOADED_IMAGES_DIR = "downloaded_images"                     # Context images
```

### Dialogue Structure

Each dialogue item supports:

- `character`: Speaker name (determines voice)
- `sentence`: Text to speak
- `image_search`: Search query for contextual image
- `image`: Character image filename
- `id`: Auto-assigned during processing

### Advanced Customization

Edit `voice_generator.py` to change:

- Voice models (see [Edge TTS voices](https://github.com/rany2/edge-tts#list-available-voices))
- Audio processing parameters

Edit `video_editor.py` to change:

- Video dimensions and layout
- Subtitle styling (font, size, colors)
- Character positioning
- Timing and transitions

## 🎯 Use Cases

- 📚 **Educational Content**: Explain complex topics in an engaging format
- 📖 **PDF Summarization**: Convert academic papers into digestible videos
- 🎓 **Study Material**: Create review content for exams
- 📱 **Social Media**: Generate viral-style educational content
- 🎪 **Edutainment**: Make learning fun and engaging

## 🔧 Troubleshooting

### Common Issues

**Problem: `ModuleNotFoundError: No module named 'moviepy'`**

```bash
# Solution: Reinstall dependencies
pip install -r requirements.txt
```

**Problem: `ImageMagick not found` or text rendering errors**

```bash
# macOS
brew install imagemagick

# Linux
sudo apt install imagemagick

# Verify installation
convert -version
```

#### **Problem: Video is too short or cuts off**

- Check that your background video (`VIDEO_TEMPLATE_PATH`) is long enough
- The system will loop the video if needed, but ensure it's at least 30 seconds

#### **Problem: No images downloaded**

- Check internet connection
- DuckDuckGo may rate limit; add delays between searches
- Check `runtime_logs/image_downloader.log` for details

#### **Problem: Poor audio quality or wrong voices**

- Verify Edge TTS is working: `edge-tts --list-voices`
- Check voice names in `voice_generator.py`
- Ensure internet connection for TTS API

#### **Problem: Video rendering is slow**

```txt
# In video_editor.py, reduce video quality temporarily:
# Change preview_factor or reduce FPS
```

### Logs

Check the `runtime_logs/` directory for detailed logs:

- `flow_log.log` - Main execution flow
- `voice_generator.log` - Audio generation details
- `image_downloader.log` - Image search and download activity

## 🎨 Customization Examples

### Change Character Voices

Edit `voice_generator.py`:

```python
VOICE_MAP = {
    "Peter": "en-US-ChristopherNeural",  # Different male voice
    "Stewie": "en-GB-RyanNeural",         # Keep Stewie
}
```

### Add More Characters

1. Add character to `config.py`:

   ```python
   {
       "character": "Brian",
       "sentence": "As a sophisticated dog, I must interject...",
       "image_search": "brian griffin reading book",
       "image": "brian.png",
       "id": None,
   }
   ```

2. Add voice mapping in `voice_generator.py`
3. Add character image to `image_assests/brian.png`

### Change Subtitle Style

Edit `video_editor.py` - look for `TextClip` parameters:

```python
subtitle_clip = TextClip(
    word,
    fontsize=60,          # Increase font size
    color='yellow',       # Change color
    stroke_color='black', # Outline color
    stroke_width=3,       # Outline thickness
    font='Arial-Bold'     # Change font
)
```

## 📊 Performance

Typical generation time (on M1 Mac):

- Audio generation: ~5-10 seconds for 2 minutes of dialogue
- Image downloading: ~5-15 seconds (depends on internet)
- Video rendering: ~1-3 minutes for a 2-minute video

**Total**: ~2-5 minutes for a complete 2-minute video

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Fork the repository**
2. **Create a feature branch**

   ```bash
   git checkout -b feature/amazing-feature
   ```

3. **Make your changes**
4. **Test thoroughly**
5. **Commit your changes**

   ```bash
   git commit -m "Add amazing feature"
   ```

6. **Push to your fork**

   ```bash
   git push origin feature/amazing-feature
   ```

7. **Open a Pull Request**

### Development Setup

```bash
# Clone and setup
git clone https://github.com/yourusername/pdf_to_brainrot.git
cd pdf_to_brainrot
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Make changes and test
python main.py
```

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Credits & Acknowledgments

- **Microsoft Edge TTS** ([edge-tts](https://github.com/rany2/edge-tts)) - Free, high-quality neural voices
- **MoviePy** ([moviepy](https://zulko.github.io/moviepy/)) - Video editing and composition
- **DuckDuckGo Search** ([ddgs](https://github.com/deedy5/duckduckgo_search)) - Image search functionality
- **Family Guy** - Character inspiration (Peter & Stewie Griffin)

## ⚠️ Disclaimer

This project is for educational and personal use only. The use of character names and likenesses from Family Guy is for parody and educational purposes. This is not affiliated with or endorsed by Family Guy, Fox, or any related entities.

## 🔮 Roadmap

- [ ] PDF parsing and automatic dialogue generation
- [ ] Web interface for easier configuration
- [ ] Support for more characters and voices
- [ ] Video template library
- [ ] Batch processing for multiple videos
- [ ] GPU acceleration for faster rendering
- [ ] Export presets for different platforms (TikTok, YouTube Shorts, Instagram Reels)

## 📞 Support

Having issues? Here's how to get help:

1. Check the [Troubleshooting](#-troubleshooting) section
2. Review existing [GitHub Issues](https://github.com/yourusername/pdf_to_brainrot/issues)
3. Check logs in `runtime_logs/`
4. Open a new issue with:
   - Your Python version (`python --version`)
   - Operating system
   - Full error message
   - Relevant log files

## 🌟 Show Your Support

If you find this project useful, please consider:

- ⭐ Starring the repository
- 🐛 Reporting bugs
- 💡 Suggesting new features
- 🔀 Contributing code
- 📢 Sharing with others
