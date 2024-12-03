# YouTube MP3/MP4 Converter

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Platform](https://img.shields.io/badge/platform-Windows-lightgrey.svg)

A simple and elegant desktop application to download YouTube videos in MP4 or MP3 format, developed in Python.

## 🛠️ Technologies Used

- **Language:** Python 3.x
- **GUI Framework:** CustomTkinter
- **Main Libraries:**
  - `yt-dlp`: For YouTube downloading
  - `customtkinter`: For modern GUI interface
  - `threading`: For asynchronous download handling

## ✨ Features

- Modern GUI with CustomTkinter
- Download YouTube videos in MP4 format
- Extract audio in MP3 format
- Video quality selection (144p to 1080p)
- Real-time progress bar
- User-friendly interface

## 📋 Prerequisites

- Python 3.x installed on your system
- Internet connection

## 🚀 Installation

1. Clone the repository:
```bash
git clone https://github.com/Ad2m1109/convertisseur_MP3_MP4.git
cd convertisseur_MP3_MP4
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## 💻 Usage

1. Launch the application:
```bash
python main.py
```

2. Paste the YouTube URL in the input field
3. Choose the format (MP4 Video or MP3 Audio)
4. Select video quality for videos
5. Click "Download"

Files will be saved in the "downloads" folder.

## 📁 Project Structure

```
convertisseur_MP3_MP4/
├── main.py              # Main program
├── requirements.txt     # Python dependencies
├── install_ffmpeg.py    # ffmpeg installation script
├── README.md           # Documentation
└── LICENSE             # MIT License
```

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Developer

- [@Ad2m1109](https://github.com/Ad2m1109)
