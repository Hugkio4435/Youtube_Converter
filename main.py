"""
YouTube to MP4/MP3 Converter
-----------------------------------
Local desktop application with a GUI that uses yt-dlp to download
YouTube videos as MP4 (video) or MP3 (audio).

REQUIREMENTS (install before running):
    pip install yt-dlp

    FFmpeg must also be installed on your system, since it is used
    to convert audio to MP3 and to merge video+audio into MP4.
    - Windows: https://www.gyan.dev/ffmpeg/builds/ (download "essentials",
      extract it, and add the "bin" folder to your system PATH)
    - macOS: brew install ffmpeg
    - Linux: sudo apt install ffmpeg  (or your distro's equivalent)

HOW TO RUN:
    python youtube_downloader.py
"""

import os
import subprocess
import sys
import threading
import tkinter as tk
from tkinter import ttk, filedialog, messagebox

try:
    import yt_dlp
except ImportError:
    yt_dlp = None


class YoutubeDownloaderApp:
    # Color palette (dark mode)
    BG = "#1e1e2e"
    BG_ALT = "#2a2a3c"
    FG = "#e4e4ef"
    FG_MUTED = "#9a9ab0"
    ACCENT = "#e0304a"
    ACCENT_HOVER = "#c4283f"
    BORDER = "#3a3a4d"

    def __init__(self, root):
        self.root = root
        self.root.title("YouTube Converter → MP4/MP3")
        self.root.geometry("560x430")
        self.root.resizable(False, False)
        self.root.configure(bg=self.BG)

        self.output_dir = tk.StringVar(value=os.path.join(os.path.expanduser("~"), "Downloads"))
        self.format_choice = tk.StringVar(value="mp4")
        self.status_text = tk.StringVar(value="Ready.")

        # Quality options
        self.video_quality_options = ["Best available", "2160p (4K)", "1440p (2K)", "1080p", "720p", "480p", "360p"]
        self.audio_quality_options = ["320 kbps", "256 kbps", "192 kbps", "128 kbps", "96 kbps"]
        self.video_quality = tk.StringVar(value=self.video_quality_options[0])
        self.audio_quality = tk.StringVar(value=self.audio_quality_options[0])

        self._setup_style()
        self._build_ui()
        self._update_quality_visibility()

    def _setup_style(self):
        style = ttk.Style()
        style.theme_use("clam")

        style.configure(
            "TCombobox",
            fieldbackground=self.BG_ALT,
            background=self.BG_ALT,
            foreground=self.FG,
            arrowcolor=self.FG,
            bordercolor=self.BORDER,
            lightcolor=self.BG_ALT,
            darkcolor=self.BG_ALT,
            padding=4,
        )
        style.map(
            "TCombobox",
            fieldbackground=[("readonly", self.BG_ALT)],
            foreground=[("readonly", self.FG)],
        )
        # The Combobox dropdown list uses the option database, not ttk.Style
        self.root.option_add("*TCombobox*Listbox.background", self.BG_ALT)
        self.root.option_add("*TCombobox*Listbox.foreground", self.FG)
        self.root.option_add("*TCombobox*Listbox.selectBackground", self.ACCENT)
        self.root.option_add("*TCombobox*Listbox.selectForeground", "white")

        style.configure(
            "TProgressbar",
            troughcolor=self.BG_ALT,
            background=self.ACCENT,
            bordercolor=self.BG_ALT,
            lightcolor=self.ACCENT,
            darkcolor=self.ACCENT,
        )

    def _build_ui(self):
        pad = {"padx": 12, "pady": 8}
        label_kwargs = {"bg": self.BG, "fg": self.FG, "font": ("Segoe UI", 10, "bold")}
        entry_kwargs = {
            "bg": self.BG_ALT,
            "fg": self.FG,
            "insertbackground": self.FG,
            "relief": "flat",
            "highlightthickness": 1,
            "highlightbackground": self.BORDER,
            "highlightcolor": self.ACCENT,
        }

        # Video link
        tk.Label(self.root, text="YouTube link:", **label_kwargs).grid(
            row=0, column=0, sticky="w", **pad
        )
        self.url_entry = tk.Entry(self.root, width=55, **entry_kwargs)
        self.url_entry.grid(row=1, column=0, columnspan=3, sticky="we", padx=12, ipady=4)

        # Format
        tk.Label(self.root, text="Output format:", **label_kwargs).grid(
            row=2, column=0, sticky="w", **pad
        )
        frame_fmt = tk.Frame(self.root, bg=self.BG)
        frame_fmt.grid(row=3, column=0, columnspan=3, sticky="w", padx=12)
        radio_kwargs = {
            "bg": self.BG,
            "fg": self.FG,
            "selectcolor": self.BG_ALT,
            "activebackground": self.BG,
            "activeforeground": self.FG,
            "highlightthickness": 0,
        }
        tk.Radiobutton(
            frame_fmt, text="Video (MP4)", variable=self.format_choice, value="mp4",
            command=self._update_quality_visibility, **radio_kwargs,
        ).pack(side="left", padx=(0, 20))
        tk.Radiobutton(
            frame_fmt, text="Audio (MP3)", variable=self.format_choice, value="mp3",
            command=self._update_quality_visibility, **radio_kwargs,
        ).pack(side="left")

        # Quality
        self.quality_label = tk.Label(self.root, text="Quality:", **label_kwargs)
        self.quality_label.grid(row=4, column=0, sticky="w", **pad)

        self.video_quality_menu = ttk.Combobox(
            self.root, textvariable=self.video_quality, values=self.video_quality_options,
            state="readonly", width=20,
        )
        self.audio_quality_menu = ttk.Combobox(
            self.root, textvariable=self.audio_quality, values=self.audio_quality_options,
            state="readonly", width=20,
        )
        # Both occupy the same spot; only one is visible at a time
        self.video_quality_menu.grid(row=5, column=0, columnspan=3, sticky="w", padx=12)
        self.audio_quality_menu.grid(row=5, column=0, columnspan=3, sticky="w", padx=12)

        # Destination folder
        tk.Label(self.root, text="Destination folder:", **label_kwargs).grid(
            row=6, column=0, sticky="w", **pad
        )
        frame_dir = tk.Frame(self.root, bg=self.BG)
        frame_dir.grid(row=7, column=0, columnspan=3, sticky="we", padx=12)
        self.dir_entry = tk.Entry(frame_dir, textvariable=self.output_dir, width=42, **entry_kwargs)
        self.dir_entry.pack(side="left", fill="x", expand=True, ipady=4)
        tk.Button(
            frame_dir, text="Browse...", command=self._choose_dir,
            bg=self.BG_ALT, fg=self.FG, activebackground=self.BORDER, activeforeground=self.FG,
            relief="flat", padx=10, cursor="hand2",
        ).pack(side="left", padx=(6, 0))

        # Download button + update button
        frame_actions = tk.Frame(self.root, bg=self.BG)
        frame_actions.grid(row=8, column=0, columnspan=3, pady=(20, 8))

        self.download_btn = tk.Button(
            frame_actions,
            text="Download",
            font=("Segoe UI", 11, "bold"),
            bg=self.ACCENT,
            fg="white",
            activebackground=self.ACCENT_HOVER,
            activeforeground="white",
            relief="flat",
            cursor="hand2",
            command=self._start_download,
        )
        self.download_btn.pack(side="left", ipadx=10, ipady=6, padx=(0, 10))

        self.update_btn = tk.Button(
            frame_actions,
            text="⟳ Update yt-dlp",
            font=("Segoe UI", 10),
            bg=self.BG_ALT,
            fg=self.FG,
            activebackground=self.BORDER,
            activeforeground=self.FG,
            relief="flat",
            cursor="hand2",
            command=self._start_update,
        )
        self.update_btn.pack(side="left", ipadx=8, ipady=6)

        # Progress bar
        self.progress = ttk.Progressbar(
            self.root, orient="horizontal", length=520, mode="determinate", style="TProgressbar"
        )
        self.progress.grid(row=9, column=0, columnspan=3, padx=12)

        # Status
        tk.Label(self.root, textvariable=self.status_text, bg=self.BG, fg=self.FG_MUTED).grid(
            row=10, column=0, columnspan=3, pady=(8, 0)
        )

    def _update_quality_visibility(self):
        if self.format_choice.get() == "mp3":
            self.video_quality_menu.grid_remove()
            self.audio_quality_menu.grid()
        else:
            self.audio_quality_menu.grid_remove()
            self.video_quality_menu.grid()

    def _start_update(self):
        self.download_btn.config(state="disabled")
        self.update_btn.config(state="disabled")
        self.status_text.set("Updating yt-dlp...")
        self.progress.config(mode="indeterminate")
        self.progress.start(12)

        thread = threading.Thread(target=self._update_ytdlp, daemon=True)
        thread.start()

    def _update_ytdlp(self):
        global yt_dlp
        try:
            result = subprocess.run(
                [sys.executable, "-m", "pip", "install", "--upgrade", "yt-dlp"],
                capture_output=True,
                text=True,
            )
            if result.returncode == 0:
                self.status_text.set("yt-dlp updated successfully!")
                # Reload the already-updated library, no need to restart the app
                import importlib
                if yt_dlp is not None:
                    importlib.reload(yt_dlp)
                else:
                    import yt_dlp as _yt_dlp
                    yt_dlp = _yt_dlp
            else:
                self.status_text.set("Failed to update yt-dlp.")
                messagebox.showerror(
                    "Update error",
                    f"Could not update yt-dlp:\n\n{result.stderr[-800:]}",
                )
        except Exception as e:
            self.status_text.set("Failed to update yt-dlp.")
            messagebox.showerror("Update error", f"An error occurred:\n\n{e}")
        finally:
            self.progress.stop()
            self.progress.config(mode="determinate")
            self.progress["value"] = 0
            self.download_btn.config(state="normal")
            self.update_btn.config(state="normal")

    def _choose_dir(self):
        chosen = filedialog.askdirectory(initialdir=self.output_dir.get())
        if chosen:
            self.output_dir.set(chosen)

    def _start_download(self):
        url = self.url_entry.get().strip()
        if not url:
            messagebox.showwarning("Warning", "Please paste a YouTube link.")
            return
        if yt_dlp is None:
            messagebox.showerror(
                "Missing dependency",
                "The 'yt-dlp' library is not installed.\n\nOpen a terminal and run:\n\npip install yt-dlp",
            )
            return

        self.download_btn.config(state="disabled")
        self.status_text.set("Starting...")
        self.progress["value"] = 0

        thread = threading.Thread(target=self._download, args=(url,), daemon=True)
        thread.start()

    def _progress_hook(self, d):
        if d["status"] == "downloading":
            total = d.get("total_bytes") or d.get("total_bytes_estimate")
            downloaded = d.get("downloaded_bytes", 0)
            if total:
                pct = downloaded / total * 100
                self.progress["value"] = pct
                self.status_text.set(f"Downloading... {pct:.1f}%")
        elif d["status"] == "finished":
            self.status_text.set("Converting/processing final file...")

    def _download(self, url):
        out_template = os.path.join(self.output_dir.get(), "%(title)s.%(ext)s")

        if self.format_choice.get() == "mp3":
            # Extract only the digits, e.g. "192 kbps" -> "192"
            kbps = "".join(ch for ch in self.audio_quality.get() if ch.isdigit())
            ydl_opts = {
                "format": "bestaudio/best",
                "outtmpl": out_template,
                "postprocessors": [
                    {
                        "key": "FFmpegExtractAudio",
                        "preferredcodec": "mp3",
                        "preferredquality": kbps,
                    }
                ],
                "progress_hooks": [self._progress_hook],
                "quiet": True,
                "noprogress": True,
                "noplaylist": True,
            }
        else:
            quality_map = {
                "Best available": None,
                "2160p (4K)": 2160,
                "1440p (2K)": 1440,
                "1080p": 1080,
                "720p": 720,
                "480p": 480,
                "360p": 360,
            }
            max_height = quality_map.get(self.video_quality.get())

            if max_height:
                fmt = (
                    f"bestvideo[height<={max_height}][ext=mp4]+bestaudio[ext=m4a]"
                    f"/best[height<={max_height}][ext=mp4]/best[height<={max_height}]"
                )
            else:
                fmt = "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best"

            ydl_opts = {
                "format": fmt,
                "outtmpl": out_template,
                "merge_output_format": "mp4",
                "progress_hooks": [self._progress_hook],
                "quiet": True,
                "noprogress": True,
                "noplaylist": True,
            }

        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            self.progress["value"] = 100
            self.status_text.set("Done! File saved successfully.")
        except Exception as e:
            self.status_text.set("An error occurred.")
            messagebox.showerror("Error", f"Could not download the video:\n\n{e}")
        finally:
            self.download_btn.config(state="normal")


if __name__ == "__main__":
    root = tk.Tk()
    app = YoutubeDownloaderApp(root)
    root.mainloop()
