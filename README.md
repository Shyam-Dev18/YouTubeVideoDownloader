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
Before running the script, ensure you have **Python 3.7+** installed.

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
D:\HTML Projects\youtube-downloader
```
You can change this path by modifying the `DESTINATION_DIRECTORY` variable inside the script.

---

## ⚡ Dependencies
This script uses:
- [`yt-dlp`](https://github.com/yt-dlp/yt-dlp) – for extracting and downloading YouTube videos.
- [`urllib`](https://docs.python.org/3/library/urllib.html) – for URL parsing.
- [`os`](https://docs.python.org/3/library/os.html) – for handling file paths.
- [`re`](https://docs.python.org/3/library/re.html) – for sanitizing filenames.

---

## ⚠️ Disclaimer
This script is **intended for personal use only**. Downloading videos without permission may violate YouTube’s **Terms of Service**. Use responsibly.

---

## 📝 License
This project is open-source under the **MIT License**.

---

## 💡 Contributing
Pull requests are welcome! Feel free to submit improvements or bug fixes. 😊
