import customtkinter as ctk
import yt_dlp
import os
from threading import Thread
from tkinter import messagebox

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Window configuration
        self.title("YouTube MP3/MP4 Converter")
        self.geometry("800x600")
        
        # Theme configuration
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        # Create widgets
        self.setup_ui()

    def setup_ui(self):
        # Main frame
        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.pack(padx=20, pady=20, fill="both", expand=True)

        # URL Input
        self.url_label = ctk.CTkLabel(self.main_frame, text="YouTube URL:")
        self.url_label.pack(pady=10)
        
        self.url_entry = ctk.CTkEntry(self.main_frame, width=400)
        self.url_entry.pack(pady=10)

        # Format buttons
        self.format_frame = ctk.CTkFrame(self.main_frame)
        self.format_frame.pack(pady=20)

        self.format_var = ctk.StringVar(value="video")
        self.video_radio = ctk.CTkRadioButton(self.format_frame, text="Video (MP4)", 
                                            variable=self.format_var, value="video")
        self.video_radio.pack(side="left", padx=10)
        
        self.audio_radio = ctk.CTkRadioButton(self.format_frame, text="Audio (MP3)", 
                                            variable=self.format_var, value="audio")
        self.audio_radio.pack(side="left", padx=10)

        # Quality dropdown
        self.quality_label = ctk.CTkLabel(self.main_frame, text="Quality:")
        self.quality_label.pack(pady=5)
        
        self.quality_var = ctk.StringVar(value="720p")
        self.quality_menu = ctk.CTkOptionMenu(self.main_frame, 
                                            values=["144p", "240p", "360p", "480p", "720p", "1080p"],
                                            variable=self.quality_var)
        self.quality_menu.pack(pady=5)

        # Download button
        self.download_button = ctk.CTkButton(self.main_frame, text="Download",
                                           command=self.start_download)
        self.download_button.pack(pady=20)

        # Progress bar
        self.progress_bar = ctk.CTkProgressBar(self.main_frame)
        self.progress_bar.pack(pady=20, fill="x", padx=40)
        self.progress_bar.set(0)

        # Status label
        self.status_label = ctk.CTkLabel(self.main_frame, text="")
        self.status_label.pack(pady=10)

    def progress_hook(self, d):
        if d['status'] == 'downloading':
            try:
                total = d.get('total_bytes', 0) or d.get('total_bytes_estimate', 0)
                if total > 0:
                    downloaded = d.get('downloaded_bytes', 0)
                    progress = (downloaded / total)
                    self.progress_bar.set(progress)
                    percentage = progress * 100
                    self.status_label.configure(text=f"Downloading: {percentage:.1f}%")
            except Exception:
                pass
        elif d['status'] == 'finished':
            self.status_label.configure(text="Finalizing...")

    def download_with_ytdlp(self, url):
        try:
            output_template = os.path.join("downloads", "%(title)s.%(ext)s")
            
            if self.format_var.get() == "video":
                # Use progressive format (combined audio + video)
                quality = self.quality_var.get()[:-1]  # Remove 'p' from '720p'
                format_spec = f'best[height<={quality}][ext=mp4]/best[ext=mp4]'
            else:
                # Audio format only
                format_spec = 'bestaudio[ext=m4a]/bestaudio'
            
            ydl_opts = {
                'format': format_spec,
                'progress_hooks': [self.progress_hook],
                'outtmpl': output_template,
                'quiet': True,
                'no_warnings': True
            }
            
            if self.format_var.get() == "audio":
                ydl_opts.update({
                    'postprocessors': [{
                        'key': 'FFmpegExtractAudio',
                        'preferredcodec': 'mp3',
                        'preferredquality': '192',
                    }],
                })

            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
                
            self.status_label.configure(text="Download completed!")
            messagebox.showinfo("Success", "Download completed successfully!")
            
        except Exception as e:
            self.status_label.configure(text=f"Error: {str(e)}")
            messagebox.showerror("Error", str(e))
        finally:
            self.progress_bar.set(0)
            self.download_button.configure(state="normal")

    def start_download(self):
        url = self.url_entry.get()
        if not url:
            messagebox.showerror("Error", "Please enter a valid YouTube URL")
            return

        self.download_button.configure(state="disabled")
        self.status_label.configure(text="Starting download...")
        
        # Create downloads folder if it doesn't exist
        if not os.path.exists("downloads"):
            os.makedirs("downloads")

        # Start download in a separate thread
        download_thread = Thread(target=self.download_with_ytdlp, args=(url,))
        download_thread.start()

if __name__ == "__main__":
    app = App()
    app.mainloop()
