import os
import datetime
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload
from google_auth_oauthlib.flow import InstalledAppFlow
import schedule
import time


def get_credentials():
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', ['https://www.googleapis.com/auth/drive'])
    return creds

def create_folder(name, parent_folder_id=None):
    service = build('drive', 'v3', credentials=get_credentials())
    folder_metadata = {'name': name, 'parents': parent_folder_id, 'mimeType': 'application/vnd.google-apps.folder'}
    folder = service.files().create(body=folder_metadata, fields='id').execute()
    print(f'Folder has been created with Name "{name}" and URL: "https://drive.google.com/drive/folders/{folder.get("id")}"')
    return folder.get('id')

def upload_folder(local_folder_path, google_drive_folder_id):
    service = build('drive', 'v3', credentials=get_credentials())
    for item in os.listdir(local_folder_path):
        item_path = os.path.join(local_folder_path, item)
        if os.path.isfile(item_path):
            file_metadata = {'name': item, 'parents': [google_drive_folder_id]}
            media = MediaFileUpload(item_path)
            file = service.files().create(body=file_metadata, media_body=media, fields='id').execute()
            print(f'File "{item}" has been uploaded with URL: "https://drive.google.com/file/d/{file.get("id")}"')
        elif os.path.isdir(item_path):
            subfolder_id = create_folder(item, [google_drive_folder_id])
            upload_folder(item_path, subfolder_id)

if __name__ == '__main__':
    # Prompt the user for local folder path and Google Drive folder ID
    local_folder_path = input('Enter the path of the local folder you want to backup: ')
    google_drive_folder_id = input('Enter the ID of the Google Drive folder you want to backup to: ')

    # Check if the user wants to reset credentials
    reset_credentials = input('Do you want to reset your current credentials? (y/n) ')
    if reset_credentials.lower() == 'y':
        os.remove('token.json')

    # Authenticate with Google Drive API
    creds = get_credentials()
    if not creds:
        flow = InstalledAppFlow.from_client_secrets_file('credentials.json', ['https://www.googleapis.com/auth/drive'])
        creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    # Check current date and create a new folder with the current date as its name
    current_date = datetime.datetime.now().strftime('%Y-%m-%d')
    backup_folder_id = create_folder(current_date, parent_folder_id=[google_drive_folder_id])

    # Upload the local folder to the newly created Google Drive folder
    upload_folder(local_folder_path, backup_folder_id)
def backup_files():
    current_date = datetime.datetime.now().strftime('%Y-%m-%d')
    backup_folder_id = create_folder(current_date, parent_folder_id=[google_drive_folder_id])

    # Upload the local folder to the newly created Google Drive folder
    upload_folder(local_folder_path, backup_folder_id)
schedule.every(24).hours.do(backup_files)

