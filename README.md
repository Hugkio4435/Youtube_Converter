[README.md](https://github.com/user-attachments/files/32305861/README.md)
# YT Converter

A lightweight, local desktop application for downloading and converting YouTube videos to **MP4** (video) or **MP3** (audio) — built with Python and a clean dark-mode interface.

![Platform](https://img.shields.io/badge/platform-Windows-blue)
![Python](https://img.shields.io/badge/python-3.13-yellow)
![License](https://img.shields.io/badge/license-MIT-green)

---

## ✨ Features

- 🎬 **Video (MP4)** or 🎵 **Audio (MP3)** downloads from a single YouTube link
- 🎚️ Adjustable **video quality** (up to 4K) and **audio bitrate** (up to 320 kbps)
- 🌙 Custom **dark-mode** interface
- 📂 Choose your own destination folder
- 📊 Live progress bar during download
- 🔄 One-click **yt-dlp updater** built into the app — no need to open a terminal when YouTube changes break older versions
- 🚫 Single-video downloads only (playlists are never downloaded by accident)
- 📦 Packaged as a standalone **.exe** — no Python installation required to run it

---

## 🖼️ Preview

*(Add a screenshot of the app here — drag an image into this section on GitHub or replace this line with `![App Screenshot](assets/screenshot.png)`)*

---

## 🛠️ Built With

- [Python 3.13](https://www.python.org/)
- [Tkinter](https://docs.python.org/3/library/tkinter.html) — GUI framework
- [yt-dlp](https://github.com/yt-dlp/yt-dlp) — YouTube download engine
- [FFmpeg](https://ffmpeg.org/) — audio/video processing
- [PyInstaller](https://pyinstaller.org/) — packaging into a standalone executable

---

## 🚀 Getting Started

### Option 1 — Run the compiled app (recommended)

1. Download the latest `.exe` from the [Releases](../../releases) page
2. Make sure [FFmpeg](https://www.gyan.dev/ffmpeg/builds/) is installed and added to your system PATH
3. Run the `.exe` — no installation needed

### Option 2 — Run from source

**Requirements:**
- Python 3.13+
- FFmpeg installed and available on your system PATH

**Steps:**

```bash
# Clone the repository
git clone https://github.com/YOUR-USERNAME/youtube-converter.git
cd youtube-converter

# Install dependencies
pip install yt-dlp

# Run the app
python youtube_downloader.py
```

---

## 📖 Usage

1. Paste a YouTube video link into the input field
2. Choose **MP4** (video) or **MP3** (audio)
3. Select your preferred quality
4. Choose a destination folder
5. Click **Download**

If a download fails with an error like `HTTP 403: Forbidden`, click **⟳ Update yt-dlp** — YouTube frequently changes its systems, and this usually resolves the issue instantly.

---

## 📦 Building the Executable

To package the app into a standalone `.exe` yourself:

```bash
pip install pyinstaller
python -m PyInstaller --onefile --windowed --name ConversorYouTube youtube_downloader.py
```

The compiled executable will be created inside the generated `dist/` folder.

---

## ⚠️ Disclaimer

This tool is intended for **personal, local use only** (e.g. archiving your own content or downloading material you have the rights to). Downloading copyrighted content from YouTube may violate YouTube's [Terms of Service](https://www.youtube.com/t/terms). Use responsibly and at your own risk.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).
