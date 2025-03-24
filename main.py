import os
from downloader import download_video
from instagram import InstagramUploader
from google_sheet import get_links_from_sheet
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

PROCESSED_LINKS_FILE = "processed_links.txt"

def load_processed_links():
    """
    Load the list of already processed links from a file.
    """
    if not os.path.exists(PROCESSED_LINKS_FILE):
        return set()
    with open(PROCESSED_LINKS_FILE, "r") as file:
        return set(line.strip() for line in file)

def save_processed_links(processed_links):
    """
    Save the list of processed links to a file.
    """
    with open(PROCESSED_LINKS_FILE, "w") as file:
        file.write("\n".join(processed_links))

def main():
    # Instagram credentials from environment variables
    username = os.getenv("IG_USERNAME")
    password = os.getenv("IG_PASSWORD")

    if not username or not password:
        print("Error: Instagram credentials are missing in the .env file.")
        return

    # Google Sheet details
    sheet_id = os.getenv("SHEET_ID")  # Add your Google Sheet ID to the .env file
    range_name = os.getenv("SHEET_RANGE", "Sheet1!A2:B")  # Default range

    # Step 1: Fetch links from Google Sheet
    print("Fetching links from Google Sheet...")
    links = get_links_from_sheet(sheet_id, range_name)

    if not links:
        print("No links found in the Google Sheet.")
        return

    # Step 2: Load processed links
    processed_links = load_processed_links()

    # Step 3: Filter unprocessed links
    unprocessed_links = [(link, caption) for link, caption in links if link not in processed_links]

    if not unprocessed_links:
        print("No new links to process.")
        return

    # Step 4: Process only the first 2 unprocessed links
    uploader = InstagramUploader(username, password)
    for link, caption in unprocessed_links[:2]:
        print(f"Processing link: {link}")

        # Download the video
        video_path, extracted_caption = download_video(link)

        if not video_path:
            print(f"Skipping link due to download error: {link}")
            continue

        # Use the caption from the sheet if available, otherwise use the extracted caption
        final_caption = caption or extracted_caption

        # Upload to Instagram
        try:
            uploader.upload_video(video_path, final_caption)
            print(f"Video uploaded successfully: {link}")
            processed_links.add(link)  # Mark the link as processed
        except Exception as e:
            print(f"Failed to upload video for link {link}: {e}")
            continue

        # Cleanup: Delete the downloaded video
        if os.path.exists(video_path):
            os.remove(video_path)
            print(f"Deleted downloaded video: {video_path}")

    # Step 5: Save updated processed links
    save_processed_links(processed_links)

    print("All videos processed successfully!")

if __name__ == "__main__":
    main()