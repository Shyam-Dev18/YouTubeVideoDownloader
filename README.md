# 🎬 YouTube Video Downloader (MP4 + M4A)

This is a Python-based **YouTube Video Downloader** that allows users to **download high-quality MP4 (H.264) video** and **M4A (AAC) audio** formats from YouTube. It utilizes `yt-dlp` for efficient extraction and downloading while ensuring minimal API calls.

## 🚀 Features
- **Supports 720p, 1080p, 2K, 4K, and 8K resolutions** (if available).
- **Efficient execution** – Fetches video metadata only once to reduce redundant API calls.
- **Auto-merging of video & audio formats** (into a single MP4 file).
- **User-friendly format selection**.
- **Automatic sanitization of filenames** (removes invalid characters).
- **Cross-platform compatibility** – Works on Windows, macOS, and Linux.

---

## 📌 Requirements  
Before running the script, ensure you have the following installed:  

### 1️⃣ **Python 3.7+**  
- Download and install **Python** from the official website: [python.org/downloads](https://www.python.org/downloads/)  
- During installation, check the box **"Add Python to PATH"** for easy access from the command line.  
- Verify installation by running:  
  ```sh
  python --version
2️⃣ FFmpeg (Required for merging audio & video)
FFmpeg is a multimedia framework used for processing audio and video files.

🛠 Windows Installation:
Download the latest FFmpeg build from: https://ffmpeg.org/download.html

Extract the files to a location (e.g., C:\ffmpeg).

Add FFmpeg to your system's PATH:

Search for "Environment Variables" in the Windows Start Menu.

Under System Variables, find Path, then click Edit.

Click New and add the bin folder path (e.g., C:\ffmpeg\bin).

Click OK to save the changes.

Verify installation by running:

sh
Copy
Edit
ffmpeg -version
🛠 Linux / macOS Installation:
For Debian/Ubuntu:

sh
Copy
Edit
sudo apt update && sudo apt install ffmpeg
For macOS (using Homebrew):

sh
Copy
Edit
brew install ffmpeg
Verify installation with:

sh
Copy
Edit
ffmpeg -version
Once both Python and FFmpeg are installed, you're ready to run the script! 🚀

markdown
Copy
Edit

This will **properly format** in GitHub’s Markdown and provide **clear installation instructions**. 🎯


Install the required dependencies using:

```bash
pip install -r requirements.txt
```

---

## 🎯 Usage
1. **Run the script**:
   ```bash
   python youtube_downloader.py
   ```
2. **Enter the YouTube video URL** when prompted.
3. **Choose a resolution** from the available options.
4. **The video will be downloaded** and saved in the specified folder.

---

## 🛠 Installation Guide
### 🔹 Windows / macOS / Linux
1. **Clone the repository** (or download the script):
   ```bash
   git clone https://github.com/yourusername/youtube-downloader.git
   cd youtube-downloader
   ```
2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the script**:
   ```bash
   python youtube_downloader.py
   ```

---

## 📂 Download Location
By default, videos are saved in:
```
D:\YouTubeVideoDownloader
```
You can change this path by modifying the `DESTINATION_DIRECTORY` variable inside the script.

---

## ⚡ Dependencies
This script uses:
- [`yt-dlp`](https://github.com/yt-dlp/yt-dlp) – for extracting and downloading YouTube videos.
- [`FFmpeg`](https://ffmpeg.org/) – for merging audio and video files.
- [`urllib`](https://docs.python.org/3/library/urllib.html) – for URL parsing.
- [`os`](https://docs.python.org/3/library/os.html) – for handling file paths.
- [`re`](https://docs.python.org/3/library/re.html) – for sanitizing filenames.

---

## ⚠️ Disclaimer
This script is **intended for personal use only**. Downloading videos without permission may violate YouTube’s **Terms of Service**. Use responsibly.

---
## ⚠️ Owner [Shyam Developer]

## 📝 License
This project is open-source under the **MIT License**.

---

## 💡 Contributing
Pull requests are welcome! Feel free to submit improvements or bug fixes. 😊
