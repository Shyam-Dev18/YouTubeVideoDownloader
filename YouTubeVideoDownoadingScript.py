import yt_dlp
import re
import os
from urllib.parse import urlparse, parse_qs

DESTINATION_DIRECTORY = r"D:\HTML Projects\youtube-downloader"  # Set your download directory

def standardize_youtube_url(url):
    parsed_url = urlparse(url)
    query_params = parse_qs(parsed_url.query)
    
    if "v" in query_params and parsed_url.netloc in ["youtube.com", "www.youtube.com"]:
        return f"https://www.youtube.com/watch?v={query_params['v'][0]}"
    
    if parsed_url.path.startswith("/shorts/"):
        return f"https://www.youtube.com/watch?v={parsed_url.path.split('/')[-1]}"
    
    match = re.match(r"^https?://(?:www\.)?youtu\.be/([a-zA-Z0-9_-]{11})", url, re.IGNORECASE)
    return f"https://www.youtube.com/watch?v={match.group(1)}" if match else None


def fetch_video_info(video_url):
    """Fetch video metadata once and reuse."""
    try:
        with yt_dlp.YoutubeDL() as ydl:
            info = ydl.extract_info(video_url, download=False)
        return info
    except Exception as e:
        print(f"❌ Failed to fetch video info: {e}")
        return None


def list_best_mp4_formats(video_info):
    """Lists best MP4 video and M4A audio formats."""
    formats = video_info.get('formats', [])

    best_mp4_formats = {}
    best_audio_format = None

    for fmt in formats:
        if fmt['ext'] == 'mp4' and fmt['vcodec'] != 'none':
            resolution = fmt.get('height', 0)
            fps = int(fmt.get('fps', 30))
            if resolution >= 720:
                key = f"{resolution}p {fps}fps"
                best_mp4_formats[key] = fmt['format_id']

        if fmt['ext'] == 'm4a' and fmt['acodec'].startswith('mp4a'):
            if not best_audio_format or fmt.get('abr', 0) > best_audio_format.get('abr', 0):
                best_audio_format = fmt

    sorted_resolutions = sorted(best_mp4_formats.keys(), key=lambda x: int(x.split('p')[0]), reverse=True)
    resolution_labels = {1440: " (2K)", 2160: " (4K)", 4320: " (8K)"}

    print("\n📌 **Available MP4 (H.264) + M4A (AAC) Formats from 720p to Highest**\n")
    print(f"{'S.NO':<5} {'Resolution':<16} {'FPS':<6} {'Video Format ID':<15} {'Audio Format ID':<15}")
    print("=" * 65)
    
    resolution_options = []
    for i, res in enumerate(sorted_resolutions, start=1):
        res_value, fps = res.split()
        res_value_int = int(res_value.replace("p", ""))
        label = resolution_labels.get(res_value_int, "")
        resolution_text = f"{res_value}{label}"
        video_format_id = best_mp4_formats[res]
        audio_format_id = best_audio_format['format_id'] if best_audio_format else 'N/A'
        resolution_options.append((video_format_id, audio_format_id))  
        print(f"{i:<5} {resolution_text:<16} {fps:<6} {video_format_id:<15} {audio_format_id:<15}")

    while True:
        try:
            choice = int(input("\n🔹 Enter the S.NO of the resolution you want to download: "))
            if 1 <= choice <= len(resolution_options):
                return resolution_options[choice - 1]
            else:
                print("❌ Invalid choice! Please enter a valid number from the list.")
        except ValueError:
            print("❌ Please enter a numeric value.")


def get_video_name(video_info):
    """Fetches and sanitizes the video title for a valid filename."""
    try:
        video_title = video_info.get('title', 'Unknown Video')

        invalid_chars = r'[<>:"/\\|?*\x00-\x1F]'
        sanitized_title = re.sub(invalid_chars, '_', video_title).strip()
        sanitized_title = sanitized_title[:100]  # Limit filename length

        return sanitized_title
    except Exception as e:
        print(f"❌ Error fetching video title: {e}")
        return "Downloaded_Video"


def download_video(video_format, audio_format, video_url, video_name):
    """Downloads the video with the given formats."""
    
    if not os.path.exists(DESTINATION_DIRECTORY):
        try:
            os.makedirs(DESTINATION_DIRECTORY)
            print(f"📂 Created directory: {DESTINATION_DIRECTORY}")
        except Exception as e:
            print(f"❌ Error creating directory: {e}")
            return
    
    output_path = os.path.join(DESTINATION_DIRECTORY, f"{video_name}.mp4")

    print(f"\n🚀 Downloading Video in Format: {video_format} + {audio_format} ...")
    print(f"📂 Saving to: {output_path}\n")

    ydl_opts = {
        'format': f"{video_format}+{audio_format}",
        'outtmpl': output_path,
        'merge_output_format': 'mp4'
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])
        print(f"\n✅ Download Complete! Saved as '{output_path}'.")
    except Exception as e:
        print(f"❌ Download failed: {e}")


# Main script
if __name__ == "__main__":
    video_url = input("🔗 Enter the YouTube video URL: ")
    
    # Standardize the URL
    video_url = standardize_youtube_url(video_url)
    if not video_url:
        print("❌ Invalid URL. Please enter a valid YouTube video link.")
        exit()

    # Fetch video metadata only ONCE
    video_info = fetch_video_info(video_url)
    if not video_info:
        exit()

    # Get video title
    video_name = get_video_name(video_info)

    # Get format selection
    selected_video, selected_audio = list_best_mp4_formats(video_info)

    # Download the selected format
    download_video(selected_video, selected_audio, video_url, video_name)
