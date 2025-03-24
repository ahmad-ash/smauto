import os
import yt_dlp

def download_video(url):
    """
    Downloads a video from the given URL and extracts its description.
    Returns the path to the downloaded video and the description as caption.
    """
    output_path = "downloads/reel.mp4"
    ydl_opts = {
        "outtmpl": output_path,
        "format": "bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4",
        "quiet": True,
        "postprocessors": [{"key": "FFmpegVideoConvertor", "preferedformat": "mp4"}],
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            caption = info.get("description", "")  # Extract description as caption
            if caption is None:
                caption = ""  # Fallback to an empty string if description is missing
        return output_path, caption.strip()
    except Exception as e:
        print(f"Error downloading video from {url}: {e}")
        return None, None