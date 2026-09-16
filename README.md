[README.md](https://github.com/user-attachments/files/32303646/README.md)
# YT Converter

A lightweight, local desktop application for downloading and converting YouTube videos to **MP4** (video) or **MP3** (audio) — built with Python and a clean dark-mode interface.

---# YT Converter

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


# ✨ Features

🎬 Video (MP4) or 🎵 Audio (MP3) downloads from a single YouTube link

🎚️ Adjustable video quality (up to 4K) and audio bitrate (up to 320 kbps)

🌙 Custom dark-mode interface

📂 Choose your own destination folder

📊 Live progress bar during download

🔄 One-click yt-dlp updater built into the app — no need to open a terminal when YouTube changes break older versions

🚫 Single-video downloads only (playlists are never downloaded by accident)

📦 Packaged as a standalone .exe — no Python installation required to run it

---

## 🛠️ Requisitos e Pré-requisitos

### Para Utilizadores Comuns (Executável)
Se fizeste o download da versão compilada (`.zip` na aba de Releases):
1.  **Windows 10 ou 11**.
2.  O ficheiro `ffmpeg.exe` deve estar guardado na mesma pasta do executável da aplicação.

### Para Programadores (Correr através do Código-Fonte)
Se pretendes executar ou modificar o código manualmente, vais precisar de:
* Python 3.8 ou superior instalado.
* FFmpeg instalado no sistema e configurado nas variáveis de ambiente (PATH).

---

## 🚀 Como Executar o Código-Fonte

1. Clone este repositório para o teu computador:
   ```bash
   git clone [https://github.com/Hugkio4435/Youtube_Converter.git](https://github.com/Hugkio4435/Youtube_Converter.git)
   cd yt-premium-converter


2. Instale as dependências necessárias através do gestor de pacotes do Python:
   ```bash
   pip install -r requirements.txt

   
3. Execute a aplicação:
   ```bash
   python main.py

##  Como Gerar o Executável (.exe)
```bash
   py -m PyInstaller --noconsole --onefile --name "Conversor YT Premium" --icon="logo.ico" main.py

# O ficheiro final compilado estará disponível dentro da pasta autogerada dist/.
