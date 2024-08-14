#pip install google-api-python-client
from googleapiclient.discovery import build
from google.oauth2 import service_account
import config as cf

SCOPES = cf.SCOPES
SERVICE_ACCOUNT_FILE = cf.SERVICE_ACCOUNT_FILE
PARENT_FOLDER_ID = cf.PARENT_FOLDER_ID

def authenticate():
    creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    return creds

def upload_file(file_path, file_name):
    creds = authenticate()
    service = build('drive', 'v3', credentials=creds)

    file_metadata = {
        'name' : file_name,
        'parents' : [PARENT_FOLDER_ID]
    }

    file = service.files().create(
        body=file_metadata,
        media_body=file_path
    ).execute()

#upload_file("config.py")

