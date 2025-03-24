# SMAUTO

This project automates the process of uploading videos to Instagram by fetching video links and captions from a Google Sheet, downloading the videos, and posting them to an Instagram account all by itself. It is designed to run on a schedule, processing a limited number of videos at a time, making it ideal for managing content uploads efficiently.

---

## Features ✅

- ✅ Fetches video links and captions from **Google Sheets**.
- ✅ Downloads videos automatically using **yt-dlp**.
- ✅ Uploads videos to **Instagram** with description and hashtags(from the original video).
- ✅ Deletes processed videos after successful uploads.
- ✅ Supports **persistent Instagram sessions** to avoid repeated logins.
- ✅ Processes a configurable number of videos per run.

---

## Installation & Setup 💻

Follow these steps to set up and run the project locally or in a Docker container.

### Step 1: Clone the Repository
```bash
git clone https://github.com/ahmad-ash/smauto
cd smauto
```

### Step 2: Set Up a Virtual Environment (Optional but Recommended)
```bash
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Add Required Credentials
1. **Google Sheets API Credentials**:
   - Download the `credentials.json` file for your Google Service Account.
   - Place it in the root directory of the project.

2. **Instagram Session**:
   - The program will automatically create a `session.json` file after the first login.
   - Ensure this file is stored securely and excluded from version control.

3. **Environment Variables**:
   - Create a `.env` file in the root directory and add the following:
     ```plaintext
     IG_USERNAME=your_instagram_username
     IG_PASSWORD=your_instagram_password
     SHEET_ID=your_google_sheet_id
     SHEET_RANGE=Sheet1!A2:B
     ```

---

## Usage Instructions 🚀

### Run Locally
To run the project locally:
```bash
python main.py
```

### Run with Docker
To build and run the project in a Docker container:
```bash
docker build -t smauto .
docker run --rm smauto
```
---

## File Structure 📂

```
.
├── main.py                 # Main script to run the bot
├── instagram.py            # Handles Instagram login and uploads
├── downloader.py           # Downloads videos using yt-dlp
├── google_sheet.py         # Fetches links and captions from Google Sheets
├── requirements.txt        # Python dependencies
├── Dockerfile              # Docker configuration
├── .env                    # Environment variables (excluded from Git)
├── session.json            # Instagram session file (excluded from Git)
├── credentials.json        # Google Sheets API credentials (excluded from Git)
└── processed_links.txt     # Tracks processed links (excluded from Git)
```

---

## Contribution Guidelines 🤝

Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new branch for your feature or bug fix:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add feature-name"
   ```
4. Push to your fork and submit a pull request.

---

## License 📜

This project is licensed under the **MIT License**.

---

## Contact & Support 📧

For issues or feedback, feel free to reach out:
- 📧 Email: salamitsahmad@gmail.com
- 🚀 LinkedIn: [@Ahmad Ashfaq](https://www.linkedin.com/in/ahmad-ishfaq-a14685301/)

---
