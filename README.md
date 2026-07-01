# YT Premium Converter 🚀

O **YT Premium Converter** é uma aplicação desktop moderna e leve para descarregar e converter vídeos ou áudios do YouTube. Construída em Python com a biblioteca **PyQt6** para a interface gráfica e alimentada pelo **yt-dlp**, a ferramenta oferece um design focado na facilidade de utilização, alto contraste visual e alta performance.

---

## ✨ Funcionalidades Principais

*  **Extração de Áudio (MP3):** Descarrega músicas com seleção de qualidade ajustável (320 kbps, 192 kbps ou 128 kbps).
*  **Downloads de Vídeo em Alta Resolução (MP4):** Suporte total desde 480p até resoluções ultra-nítidas como **2K** e **4K (2160p)**.
*  **Sistema Anti-Bloqueio (Smart Fallback):** Execução otimizada que contorna restrições de "bot" do YouTube, extraindo cookies de sessão de vários navegadores (Firefox, Chrome, Edge, Brave, Opera) de forma totalmente invisível.
*  **Escolha de Destino:** Permite selecionar facilmente em que pasta do computador o ficheiro final será guardado.
*  **Interface Moderna (Dark Mode):** Visual escuro de alto contraste inspirado nas ferramentas de desenvolvimento modernas, otimizado para não cansar a vista.

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



