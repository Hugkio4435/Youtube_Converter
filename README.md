# YT Converter

A lightweight, local desktop application for downloading and converting YouTube videos to **MP4** (video) or **MP3** (audio) — built with Python and a clean dark-mode interface.

---

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
