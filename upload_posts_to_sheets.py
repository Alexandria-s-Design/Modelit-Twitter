"""
Upload ModelIt K12 X posts from JSON to Google Sheets
"""

import json
import os
from google.oauth2.credentials import Credentials
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow

# Scopes for Google Sheets API
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

def get_credentials():
    """Get Google API credentials"""
    creds = None

    # Token file stores the user's access and refresh tokens
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)

    # If there are no (valid) credentials available, let the user log in
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)

        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    return creds

def create_spreadsheet(service, title: str = "ModelIt K12 X Posts - 2025"):
    """Create a new Google Sheet"""
    try:
        spreadsheet = {
            'properties': {
                'title': title
            }
        }
        spreadsheet = service.spreadsheets().create(
            body=spreadsheet,
            fields='spreadsheetId,spreadsheetUrl'
        ).execute()

        print(f"✅ Created spreadsheet: {spreadsheet.get('spreadsheetUrl')}")
        return spreadsheet.get('spreadsheetId')

    except HttpError as error:
        print(f"❌ An error occurred: {error}")
        return None

def format_sheet(service, spreadsheet_id: str, sheet_name: str = "X Posts"):
    """Format the sheet with headers and styling"""

    # Define header row
    headers = [
        "Post #",
        "Week #",
        "Post Order",
        "Category",
        "Main Text",
        "Hashtags",
        "Website Link",
        "TPT Link",
        "Full Post",
        "Scheduled Date"
    ]

    # Create header row
    header_data = [headers]

    # Update the sheet
    requests = [
        {
            # Rename Sheet1 to "X Posts"
            "updateSheetProperties": {
                "properties": {
                    "sheetId": 0,
                    "title": sheet_name
                },
                "fields": "title"
            }
        },
        {
            # Format header row (bold, frozen)
            "repeatCell": {
                "range": {
                    "sheetId": 0,
                    "startRowIndex": 0,
                    "endRowIndex": 1
                },
                "cell": {
                    "userEnteredFormat": {
                        "backgroundColor": {
                            "red": 0.2,
                            "green": 0.6,
                            "blue": 0.9
                        },
                        "textFormat": {
                            "bold": True,
                            "foregroundColor": {
                                "red": 1.0,
                                "green": 1.0,
                                "blue": 1.0
                            }
                        }
                    }
                },
                "fields": "userEnteredFormat(backgroundColor,textFormat)"
            }
        },
        {
            # Freeze header row
            "updateSheetProperties": {
                "properties": {
                    "sheetId": 0,
                    "gridProperties": {
                        "frozenRowCount": 1
                    }
                },
                "fields": "gridProperties.frozenRowCount"
            }
        },
        {
            # Auto-resize columns
            "autoResizeDimensions": {
                "dimensions": {
                    "sheetId": 0,
                    "dimension": "COLUMNS",
                    "startIndex": 0,
                    "endIndex": 10
                }
            }
        }
    ]

    body = {
        'requests': requests
    }

    try:
        service.spreadsheets().batchUpdate(
            spreadsheetId=spreadsheet_id,
            body=body
        ).execute()

        # Add header row
        service.spreadsheets().values().update(
            spreadsheetId=spreadsheet_id,
            range=f'{sheet_name}!A1:J1',
            valueInputOption='RAW',
            body={'values': header_data}
        ).execute()

        print(f"✅ Formatted sheet with headers")

    except HttpError as error:
        print(f"❌ Error formatting sheet: {error}")

def upload_posts(service, spreadsheet_id: str, posts_file: str, sheet_name: str = "X Posts"):
    """Upload posts from JSON to Google Sheet"""

    # Load posts from JSON
    with open(posts_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    posts = data['posts']

    print(f"📝 Uploading {len(posts)} posts...")

    # Convert posts to rows
    rows = []
    for post in posts:
        row = [
            post['post_number'],
            post['week_number'],
            post['post_order'],
            post['category'],
            post['main_text'],
            post['hashtags'],
            post['website_link'],
            post['tpt_link'],
            post['full_post'],
            post['scheduled_date']
        ]
        rows.append(row)

    # Upload data
    try:
        service.spreadsheets().values().update(
            spreadsheetId=spreadsheet_id,
            range=f'{sheet_name}!A2:J{len(rows)+1}',
            valueInputOption='RAW',
            body={'values': rows}
        ).execute()

        print(f"✅ Uploaded {len(posts)} posts to Google Sheet")

        # Get the spreadsheet URL
        spreadsheet = service.spreadsheets().get(
            spreadsheetId=spreadsheet_id
        ).execute()

        print(f"\n🔗 Spreadsheet URL: {spreadsheet['spreadsheetUrl']}")

        return spreadsheet['spreadsheetUrl']

    except HttpError as error:
        print(f"❌ Error uploading posts: {error}")
        return None

def main(posts_file: str = "modelit_x_posts.json", spreadsheet_id: str = None):
    """Main function to upload posts to Google Sheets"""

    print("🚀 Starting upload to Google Sheets...\n")

    # Get credentials
    creds = get_credentials()

    # Build the service
    service = build('sheets', 'v4', credentials=creds)

    # Create new spreadsheet or use existing
    if not spreadsheet_id:
        spreadsheet_id = create_spreadsheet(service)
        if not spreadsheet_id:
            print("❌ Failed to create spreadsheet")
            return

        # Format the sheet
        format_sheet(service, spreadsheet_id)
    else:
        print(f"📊 Using existing spreadsheet: {spreadsheet_id}")

    # Upload posts
    url = upload_posts(service, spreadsheet_id, posts_file)

    if url:
        print(f"\n✨ Success! Your posts are ready for automation.")
        print(f"\n📋 Next steps:")
        print(f"   1. Review the posts in the sheet")
        print(f"   2. Adjust scheduled dates as needed")
        print(f"   3. Set up automation (Zapier, Make.com, or Buffer)")
        print(f"   4. Monitor engagement and iterate on top performers")

if __name__ == "__main__":
    import sys

    posts_file = sys.argv[1] if len(sys.argv) > 1 else "modelit_x_posts.json"
    spreadsheet_id = sys.argv[2] if len(sys.argv) > 2 else None

    main(posts_file, spreadsheet_id)
