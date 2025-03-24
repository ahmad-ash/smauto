from googleapiclient.discovery import build
from google.oauth2.service_account import Credentials

# Define the scope for accessing Google Sheets
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

def get_links_from_sheet(sheet_id, range_name):
    """
    Fetches video links and optional captions from a Google Sheet.
    :param sheet_id: The ID of the Google Sheet.
    :param range_name: The range of cells to read (e.g., "Sheet1!A2:B").
    :return: A list of tuples (link, caption).
    """
    try:
        # Authenticate using the service account credentials
        creds = Credentials.from_service_account_file('smauto-454307-4cb11bfeae46.json', scopes=SCOPES)
        service = build('sheets', 'v4', credentials=creds)
        sheet = service.spreadsheets()

        # Read data from the sheet
        result = sheet.values().get(spreadsheetId=sheet_id, range=range_name).execute()
        rows = result.get('values', [])

        # Return links and captions (if available)
        return [(row[0], row[1] if len(row) > 1 else "") for row in rows]
    except Exception as e:
        print(f"Error fetching data from Google Sheet: {e}")
        return []