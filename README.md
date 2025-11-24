# PDF to Brainrot 🧠🎮

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
Simple tool to turn an educational script into a meme "brainrot" video, Family Guy style (Peter & Stewie banter), with game footage and AI-generated voices.

## What is This?

This makes fast-paced meme videos popular on TikTok/YouTube Shorts: background gameplay, character heads, goofy AI voices, word-by-word subtitles, and images that match the topic.

## Features

- Uses Edge TTS for free, decent AI voices (Peter: `en-US-GuyNeural`, Stewie: `en-GB-RyanNeural`)
- Word-by-word subtitles
- Swaps character overlays left/right automatically
- Puts relevant Google/DuckDuckGo images in as context
- Loops background video if needed

## Quick Start

Requirements:

- Python 3.8+
- ImageMagick for subtitles (`convert -version` should work)
- Basic Python setup (`pip`, virtualenv recommended)

1. Clone the repo  
2. Make a virtual env and install dependencies:  

   ```
   python -m venv venv
   source venv/bin/activate  # Or venv\Scripts\activate on Windows
   pip install -r requirements.txt
   ```

3. Install ImageMagick using your package manager (`brew`, `apt`, etc)

4. Prepare your assets:
   - Put `peter.png`, `stewie.png` in `image_assests/`
   - Put a gameplay video in `video_assests/` (example: `minecraft_background.mp4`)

   *(Optional: Download a Minecraft background with `yt-dlp`)*

5. Edit `config.py` -- the `DIALOGUE` list controls the conversation.

6. Run:

   ```
   python main.py
   ```

7. Your video appears as `output_final_video.mp4`.

## Editing/Customization

- All script/settings in `config.py`
- Edit voices or add new characters in `voice_generator.py`
- Tweak video style or subtitle look in `video_editor.py` (`TextClip`)

## Troubleshooting

- If moviepy/ImageMagick not working:  
  `pip install -r requirements.txt` & make sure `convert -version` works
- For missing voices or audio issues:  
  `edge-tts --list-voices`
- For image/search issues:  
  Check your connection, try again, or see logs in `runtime_logs/`

## License

MIT. See [LICENSE](LICENSE).

## Credits

- edge-tts (Microsoft)
- MoviePy
- DuckDuckGo Search
- Family Guy (parody/fan use only)

## Disclaimer

Not affiliated with or endorsed by Family Guy, Fox, or related. Meme/educational use.
